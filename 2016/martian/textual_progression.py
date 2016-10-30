#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: textual_progression.py
# Author: #cf, 2016.

"""
Script to visualize edits over textual progression.
"""

import re
import pandas as pd
import pygal
from pygal import Config
from scipy.signal import savgol_filter as sf
#print("pygal version", pygal.__version__)
#print(help(pygal))

WorkDir = "/media/christof/data/Dropbox/0-Analysen/2016/martians/progression/"
DataFile = WorkDir+"DiffTable.csv"



def mold_data(DataFile): 
    print("--mold_data...")

    # Getting the data
    with open(DataFile, "r") as infile:
        AllData = infile.read()
        AllData = re.split("\n", AllData)
        
        # Fill in empty entries for lines without edits.
        theo = 1
        real = 1
        FullData = []
        while theo < 11478: 
            TheoID = theo
            RealID = int(float(AllData[real][0:5]+".0"))
            #print(TheoID, RealID)
            RealLine = AllData[real]
            if TheoID == RealID: 
                #print(TheoID, RealID, "-- Matching IDs.")
                FullData.append(RealLine.split("\t")[0:8])
                theo += 1
                real += 1
            elif TheoID < RealID: 
                #print(TheoID, RealID, "-- Missing RealID.")
                FullData.append(str('{:05d}'.format(TheoID)+"x\t0\t-\t-\t0\t0\t0\t0").split("\t"))
                theo += 1
                real += 0
            elif TheoID > RealID:
                #print(TheoID, RealID, "-- Multiple RealIDs.")
                FullData.append(RealLine.split("\t")[0:7])
                theo += 0
                real += 1        
 
        RightData = FullData
        RightData = pd.DataFrame(RightData, columns=["line-id","edit-no","category","type","analysis","levenshtein","char-diff","char-diff-abs"])
        return(RightData)


def using_pygal(DataFile):
    print("--using_pygal...")
    # Get the data as dataframe
    RightData = mold_data(DataFile)  
    
    # Remove unnecessary information
    RightData = RightData.drop("edit-no", axis=1)
    RightData = RightData.drop("type", axis=1)
    RightData = RightData.drop("analysis", axis=1)
    RightData = RightData.drop("char-diff", axis=1)
    RightData = RightData.drop("char-diff-abs", axis=1)

    # RightData1: set levenshtein to zero for substantives (effectively ignoring them) 
    RightData1 = RightData.copy(deep=True)
    RightData1.loc[RightData1["category"] =="other","levenshtein"] = 0
    # Fix some details: levenshtein as numerical, remove x from line-id
    RightData1["levenshtein"] = RightData1["levenshtein"].astype(str).convert_objects(convert_numeric=True)
    RightData1["line-id"] = RightData1["line-id"].map(lambda x: x.rstrip("x"))
    RightData1 = RightData1.groupby("line-id").sum()
    #print(RightData1.head(20))

    # RightData2: set levenshtein to zero for copyedits (effectively ignoring them) 
    RightData2 = RightData.copy(deep=True)
    RightData2.loc[RightData2["category"] =="copyedit","levenshtein"] = 0
    # Fix some details: levenshtein as numerical, remove x from line-id
    RightData2["levenshtein"] = RightData2["levenshtein"].astype(str).convert_objects(convert_numeric=True)
    RightData2["line-id"] = RightData2["line-id"].map(lambda x: x.rstrip("x"))
    RightData2 = RightData2.groupby("line-id").sum()
    #print(RightData2.head(20))
        
    # Select the range of data we want
    Lines = RightData1.index.values
    Copyedits = RightData1.loc[:,"levenshtein"]
    Substantives = RightData2.loc[:,"levenshtein"]
    
    # Apply some interpolation    
    CopyeditsSF = sf(Copyedits, 35, 1, mode="nearest")
    SubstantivesSF = sf(Substantives, 35, 1, mode="nearest")

    # Graph general configuration
    config = Config()
    config.show_legend = False
    config.human_readable = True
    config.fill = False

    # Line chart
    LineChart = pygal.StackedLine(config, 
                           height=1000,
                           width = 2000,
                           x_label_rotation=300, 
                           show_legend=False,
                           x_labels_major_every=200,
                           show_minor_x_labels=False,
                           show_dots=False,
                           fill=True,
                           logarithmic=False,
                           range=(0, 60))
    LineChart.title ="The Martian Modifications (copyedits and substantives)"
    LineChart.y_title = "Levenshtein distance (smoothed)"
    LineChart.x_title = "Lines in the novel"
    LineChart.x_labels = Lines
    LineChart.add("Copyedits", CopyeditsSF)
    LineChart.add("Substantives", SubstantivesSF)
    LineChart.render_to_file("MartianMods_copyedits+substantives.svg")


def textual_progression(DataFile):
    print("textual_progression.")
    using_pygal(DataFile)


textual_progression(DataFile)

