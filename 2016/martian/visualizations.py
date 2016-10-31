#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: visualizations.py
# Author: #cf, 2016.

"""
Script to create graphs using Python.
"""

import pandas as pd
import pygal
from pygal import Config
#print("pygal version", pygal.__version__)
#print(help(pygal))

WorkDir = "/media/christof/data/Dropbox/0-Analysen/2016/martians/viz/"
DataFile = WorkDir+"DiffTable.csv"


def using_pygal(DataFile):
    print("using_pygal...")
    
    ## Getting the data
    with open(DataFile, "r") as infile:
        AllData = pd.read_table(infile)
        #print(AllData.head())
                        
        # Select the data we want
        Lines = AllData.loc[:,"line-no"][0:50]
        ItemIDs = AllData.loc[:,"item-id"][0:50]
        Version1s = AllData.loc[:,"version1"][0:50]
        Version2s = AllData.loc[:,"version2"][0:50]
        Categories = AllData.loc[:,"category"][0:50]
        Types = AllData.loc[:,"type"][0:50]
        LevDists = AllData.loc[:,"levenshtein"][0:50]
        CharDiffsAbs = AllData.loc[:,"char-delta-abs"][0:50]
        CharDiffs = AllData.loc[:,"char-delta"][0:50]

        # Apply very simple smoothing to LevDists 
        LevDistsSmth = []
        Smthp0 = (LevDists[0] + LevDists[1])/2
        Smthp1 = (LevDists[1] + LevDists[2])/2
        LevDistsSmth.append(Smthp0)
        LevDistsSmth.append(Smthp1)
        for i in range(2, len(LevDists)-2): 
            NewValue = (LevDists[i-2]/2 + LevDists[i-1] + LevDists[i] + LevDists[i+1] + LevDists[i+2]/2) / 4
            LevDistsSmth.append(NewValue)
        Smthm0 = (LevDists[len(LevDists)-2] + LevDists[len(LevDists)-3]) / 2
        Smthm1 = (LevDists[len(LevDists)-1] + LevDists[len(LevDists)-2]) / 2
        LevDistsSmth.append(Smthm0)
        LevDistsSmth.append(Smthm1)
    
        # Graph general configuration
        config = Config()
        config.show_legend = False
        config.human_readable = True
        config.fill = False
    
        # Graphing: bar chart
        BarChart1 = pygal.Bar(config)
        BarChart1.title = "The Martian Modifications (Char-Diff)"
        BarChart1.x_labels = map(str, range(0, 50))
        #BarChart.add("Levenshtein", LevDists)
        BarChart1.add("Char-Diff", CharDiffs)
        #chart.add("Char-Diff-Abs", CharDiffsAbs)
        BarChart1.render_to_file("BarChart1.svg")
        
        # Graphing: another bar chart
        BarChart2 = pygal.Bar(config, x_label_rotation=270)
        BarChart2.title ="The Martian Modifications (Labels)"
        #LineChart.x_labels = map(str, ItemIDs)
        for i in range(0,30): 
            BarChart2.add(ItemIDs[i], [{"value" : CharDiffs[i], "label" : str(Version1s[i])+" => "+str(Version2s[i]), 'color': 'red'}])
        BarChart2.render_to_file("BarChart2.svg")
               
        # Line chart
        LineChart1 = pygal.Line(config, x_label_rotation=270, show_legend=True)
        LineChart1.title ="The Martian Modifications (smoothed)"
        LineChart1.add("LevDists", LevDists)
        LineChart1.add("LevDistsSmth", LevDistsSmth)
        LineChart1.render_to_file("LineChart1.svg")
        
using_pygal(DataFile)





















