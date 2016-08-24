#!/usr/bin/env python3
# Filename: sentencelength.py

"""
# Function calculate sentence length statistics for a text collection.
"""


# Import statements

import re
import glob
import os
import pandas as pd
import numpy as np
import pygal

# Parameter definitions

DataFile = "AllResults+Metadata.csv"
GraphFile = "toutsimenon.svg"

# Functions

def read_data(DataFile):
    with open(DataFile,"r") as InFile:
        Data = pd.DataFrame.from_csv(InFile)
        #print(Data.head(6))
        return Data

def make_datedata(Data):
    #print(Data)
    Data = Data.groupby("cf-class")
    Autob = Data.get_group("autob")
    #print(Autob)
    #print(len(Autob))
    AutobTitles = []
    AutobYears = []
    AutobMeans = []
    for i in range(0,26): 
        Title= Autob.iloc[i,7]
        Year = Autob.iloc[i,9]
        Mean = Autob.iloc[i,2]
        AutobTitles.append(Title)
        AutobYears.append(Year)
        AutobMeans.append(Mean)
    #print(AutobTitles)
    #print(AutobYears)
    #print(AutobMeans)
    Maigr = Data.get_group("maigr")
    #print(Maigr)
    #print(len(Maigr))
    MaigrTitles = []
    MaigrYears = []
    MaigrMeans = []
    for i in range(0,46): 
        Title= Maigr.iloc[i,7]
        Year = Maigr.iloc[i,9]
        Mean = Maigr.iloc[i,2]
        MaigrTitles.append(Title)
        MaigrYears.append(Year)
        MaigrMeans.append(Mean)
    #print(MaigrTitles)
    #print(MaigrYears)
    #print(MaigrMeans)
    Roman = Data.get_group("romans")
    #print(Roman)
    #print(len(Roman))
    RomanTitles = []
    RomanYears = []
    RomanMeans = []
    for i in range(0,55): 
        Title= Roman.iloc[i,7]
        Year = Roman.iloc[i,9]
        Mean = Roman.iloc[i,2]
        RomanTitles.append(Title)
        RomanYears.append(Year)
        RomanMeans.append(Mean)
    #print(RomanTitles)
    #print(RomanYears)
    #print(RomanMeans)
    return AutobTitles, AutobYears, AutobMeans, MaigrTitles, MaigrYears, MaigrMeans, RomanTitles, RomanYears, RomanMeans    
    
from pygal.style import BlueStyle
from pygal.style import TurquoiseStyle
from pygal.style import LightSolarizedStyle
from pygal.style import CleanStyle
from pygal.style import RedBlueStyle

def make_scatterplot(AutobTitles, AutobYears, AutobMeans, MaigrTitles, MaigrYears, MaigrMeans, RomanTitles, RomanYears, RomanMeans, GraphFile): 
    chart = pygal.XY(x_label_rotation=300,
                              stroke=False,
                              range = (8,24),
                              xrange=(1930, 1980),
                              title="Satzlängen (127 x Simenon)",
                              x_title="Entstehungsjahr",
                              y_title="Mittlere Satzlänge in Worten",
                             show_x_guides=True,
                              show_y_guides=True,
                              style=CleanStyle)                
    chart.add("autobio", [
    {"value" : (AutobYears[0], AutobMeans[0]), "label" : AutobTitles[0]},
    {"value" : (AutobYears[1], AutobMeans[1]), "label" : AutobTitles[1]},
    {"value" : (AutobYears[2], AutobMeans[2]), "label" : AutobTitles[2]},
    {"value" : (AutobYears[3], AutobMeans[3]), "label" : AutobTitles[3]},
    {"value" : (AutobYears[4], AutobMeans[4]), "label" : AutobTitles[4]},
    {"value" : (AutobYears[5], AutobMeans[5]), "label" : AutobTitles[5]},
    {"value" : (AutobYears[6], AutobMeans[6]), "label" : AutobTitles[6]},
    {"value" : (AutobYears[7], AutobMeans[7]), "label" : AutobTitles[7]},
    {"value" : (AutobYears[8], AutobMeans[8]), "label" : AutobTitles[8]},
    {"value" : (AutobYears[9], AutobMeans[9]), "label" : AutobTitles[9]},
    {"value" : (AutobYears[10], AutobMeans[10]), "label" : AutobTitles[10]},
    {"value" : (AutobYears[11], AutobMeans[11]), "label" : AutobTitles[11]},
    {"value" : (AutobYears[12], AutobMeans[12]), "label" : AutobTitles[12]},
    {"value" : (AutobYears[13], AutobMeans[13]), "label" : AutobTitles[13]},
    {"value" : (AutobYears[14], AutobMeans[14]), "label" : AutobTitles[14]},
    {"value" : (AutobYears[15], AutobMeans[15]), "label" : AutobTitles[15]},
    {"value" : (AutobYears[16], AutobMeans[16]), "label" : AutobTitles[16]},
    {"value" : (AutobYears[17], AutobMeans[17]), "label" : AutobTitles[17]},
    {"value" : (AutobYears[18], AutobMeans[18]), "label" : AutobTitles[18]},
    {"value" : (AutobYears[19], AutobMeans[19]), "label" : AutobTitles[19]},
    {"value" : (AutobYears[20], AutobMeans[20]), "label" : AutobTitles[20]},
    {"value" : (AutobYears[21], AutobMeans[21]), "label" : AutobTitles[21]},
    {"value" : (AutobYears[22], AutobMeans[22]), "label" : AutobTitles[22]},
    {"value" : (AutobYears[23], AutobMeans[23]), "label" : AutobTitles[23]},
    {"value" : (AutobYears[24], AutobMeans[24]), "label" : AutobTitles[24]},
    {"value" : (AutobYears[25], AutobMeans[25]), "label" : AutobTitles[25]},
    ], dots_size=7)
    chart.add("maigret", [
    {"value" : (MaigrYears[0], MaigrMeans[0]), "label" : MaigrTitles[0]},
    {"value" : (MaigrYears[1], MaigrMeans[1]), "label" : MaigrTitles[1]},
    {"value" : (MaigrYears[2], MaigrMeans[2]), "label" : MaigrTitles[2]},
    {"value" : (MaigrYears[3], MaigrMeans[3]), "label" : MaigrTitles[3]},
    {"value" : (MaigrYears[4], MaigrMeans[4]), "label" : MaigrTitles[4]},
    {"value" : (MaigrYears[5], MaigrMeans[5]), "label" : MaigrTitles[5]},
    {"value" : (MaigrYears[6], MaigrMeans[6]), "label" : MaigrTitles[6]},
    {"value" : (MaigrYears[7], MaigrMeans[7]), "label" : MaigrTitles[7]},
    {"value" : (MaigrYears[8], MaigrMeans[8]), "label" : MaigrTitles[8]},
    {"value" : (MaigrYears[9], MaigrMeans[9]), "label" : MaigrTitles[9]},
    {"value" : (MaigrYears[10], MaigrMeans[10]), "label" : MaigrTitles[10]},
    {"value" : (MaigrYears[11], MaigrMeans[11]), "label" : MaigrTitles[11]},
    {"value" : (MaigrYears[12], MaigrMeans[12]), "label" : MaigrTitles[12]},
    {"value" : (MaigrYears[13], MaigrMeans[13]), "label" : MaigrTitles[13]},
    {"value" : (MaigrYears[14], MaigrMeans[14]), "label" : MaigrTitles[14]},
    {"value" : (MaigrYears[15], MaigrMeans[15]), "label" : MaigrTitles[15]},
    {"value" : (MaigrYears[16], MaigrMeans[16]), "label" : MaigrTitles[16]},
    {"value" : (MaigrYears[17], MaigrMeans[17]), "label" : MaigrTitles[17]},
    {"value" : (MaigrYears[18], MaigrMeans[18]), "label" : MaigrTitles[18]},
    {"value" : (MaigrYears[19], MaigrMeans[19]), "label" : MaigrTitles[19]},
    {"value" : (MaigrYears[20], MaigrMeans[20]), "label" : MaigrTitles[20]},
    {"value" : (MaigrYears[21], MaigrMeans[21]), "label" : MaigrTitles[21]},
    {"value" : (MaigrYears[22], MaigrMeans[22]), "label" : MaigrTitles[22]},
    {"value" : (MaigrYears[23], MaigrMeans[23]), "label" : MaigrTitles[23]},
    {"value" : (MaigrYears[24], MaigrMeans[24]), "label" : MaigrTitles[24]},
    {"value" : (MaigrYears[25], MaigrMeans[25]), "label" : MaigrTitles[25]},
    {"value" : (MaigrYears[26], MaigrMeans[26]), "label" : MaigrTitles[26]},
    {"value" : (MaigrYears[27], MaigrMeans[27]), "label" : MaigrTitles[27]},
    {"value" : (MaigrYears[28], MaigrMeans[28]), "label" : MaigrTitles[28]},
    {"value" : (MaigrYears[29], MaigrMeans[29]), "label" : MaigrTitles[29]},
    {"value" : (MaigrYears[30], MaigrMeans[30]), "label" : MaigrTitles[30]},
    {"value" : (MaigrYears[31], MaigrMeans[31]), "label" : MaigrTitles[31]},
    {"value" : (MaigrYears[32], MaigrMeans[32]), "label" : MaigrTitles[32]},
    {"value" : (MaigrYears[33], MaigrMeans[33]), "label" : MaigrTitles[33]},
    {"value" : (MaigrYears[34], MaigrMeans[34]), "label" : MaigrTitles[34]},
    {"value" : (MaigrYears[35], MaigrMeans[35]), "label" : MaigrTitles[35]},
    {"value" : (MaigrYears[36], MaigrMeans[36]), "label" : MaigrTitles[36]},
    {"value" : (MaigrYears[37], MaigrMeans[37]), "label" : MaigrTitles[37]},
    {"value" : (MaigrYears[38], MaigrMeans[38]), "label" : MaigrTitles[38]},
    {"value" : (MaigrYears[39], MaigrMeans[39]), "label" : MaigrTitles[39]},
    {"value" : (MaigrYears[40], MaigrMeans[30]), "label" : MaigrTitles[40]},
    {"value" : (MaigrYears[41], MaigrMeans[31]), "label" : MaigrTitles[41]},
    {"value" : (MaigrYears[42], MaigrMeans[32]), "label" : MaigrTitles[42]},
    {"value" : (MaigrYears[43], MaigrMeans[33]), "label" : MaigrTitles[43]},
    {"value" : (MaigrYears[44], MaigrMeans[34]), "label" : MaigrTitles[44]},
    {"value" : (MaigrYears[45], MaigrMeans[35]), "label" : MaigrTitles[45]},
    ], dots_size=7)
    chart.add("romans", [
    {"value" : (RomanYears[0], RomanMeans[0]), "label" : RomanTitles[0]},
    {"value" : (RomanYears[1], RomanMeans[1]), "label" : RomanTitles[1]},
    {"value" : (RomanYears[2], RomanMeans[2]), "label" : RomanTitles[2]},
    {"value" : (RomanYears[3], RomanMeans[3]), "label" : RomanTitles[3]},
    {"value" : (RomanYears[4], RomanMeans[4]), "label" : RomanTitles[4]},
    {"value" : (RomanYears[5], RomanMeans[5]), "label" : RomanTitles[5]},
    {"value" : (RomanYears[6], RomanMeans[6]), "label" : RomanTitles[6]},
    {"value" : (RomanYears[7], RomanMeans[7]), "label" : RomanTitles[7]},
    {"value" : (RomanYears[8], RomanMeans[8]), "label" : RomanTitles[8]},
    {"value" : (RomanYears[9], RomanMeans[9]), "label" : RomanTitles[9]},
    {"value" : (RomanYears[10], RomanMeans[10]), "label" : RomanTitles[10]},
    {"value" : (RomanYears[11], RomanMeans[11]), "label" : RomanTitles[11]},
    {"value" : (RomanYears[12], RomanMeans[12]), "label" : RomanTitles[12]},
    {"value" : (RomanYears[13], RomanMeans[13]), "label" : RomanTitles[13]},
    {"value" : (RomanYears[14], RomanMeans[14]), "label" : RomanTitles[14]},
    {"value" : (RomanYears[15], RomanMeans[15]), "label" : RomanTitles[15]},
    {"value" : (RomanYears[16], RomanMeans[16]), "label" : RomanTitles[16]},
    {"value" : (RomanYears[17], RomanMeans[17]), "label" : RomanTitles[17]},
    {"value" : (RomanYears[18], RomanMeans[18]), "label" : RomanTitles[18]},
    {"value" : (RomanYears[19], RomanMeans[19]), "label" : RomanTitles[19]},
    {"value" : (RomanYears[20], RomanMeans[20]), "label" : RomanTitles[20]},
    {"value" : (RomanYears[21], RomanMeans[21]), "label" : RomanTitles[21]},
    {"value" : (RomanYears[22], RomanMeans[22]), "label" : RomanTitles[22]},
    {"value" : (RomanYears[23], RomanMeans[23]), "label" : RomanTitles[23]},
    {"value" : (RomanYears[24], RomanMeans[24]), "label" : RomanTitles[24]},
    {"value" : (RomanYears[25], RomanMeans[25]), "label" : RomanTitles[25]},
    {"value" : (RomanYears[26], RomanMeans[26]), "label" : RomanTitles[26]},
    {"value" : (RomanYears[27], RomanMeans[27]), "label" : RomanTitles[27]},
    {"value" : (RomanYears[28], RomanMeans[28]), "label" : RomanTitles[28]},
    {"value" : (RomanYears[29], RomanMeans[29]), "label" : RomanTitles[29]},
    {"value" : (RomanYears[30], RomanMeans[30]), "label" : RomanTitles[30]},
    {"value" : (RomanYears[31], RomanMeans[31]), "label" : RomanTitles[31]},
    {"value" : (RomanYears[32], RomanMeans[32]), "label" : RomanTitles[32]},
    {"value" : (RomanYears[33], RomanMeans[33]), "label" : RomanTitles[33]},
    {"value" : (RomanYears[34], RomanMeans[34]), "label" : RomanTitles[34]},
    {"value" : (RomanYears[35], RomanMeans[35]), "label" : RomanTitles[35]},
    {"value" : (RomanYears[36], RomanMeans[36]), "label" : RomanTitles[36]},
    {"value" : (RomanYears[37], RomanMeans[37]), "label" : RomanTitles[37]},
    {"value" : (RomanYears[38], RomanMeans[38]), "label" : RomanTitles[38]},
    {"value" : (RomanYears[39], RomanMeans[39]), "label" : RomanTitles[39]},
    {"value" : (RomanYears[40], RomanMeans[40]), "label" : RomanTitles[40]},
    {"value" : (RomanYears[41], RomanMeans[41]), "label" : RomanTitles[41]},
    {"value" : (RomanYears[42], RomanMeans[42]), "label" : RomanTitles[42]},
    {"value" : (RomanYears[43], RomanMeans[43]), "label" : RomanTitles[43]},
    {"value" : (RomanYears[44], RomanMeans[44]), "label" : RomanTitles[44]},
    {"value" : (RomanYears[45], RomanMeans[45]), "label" : RomanTitles[45]},
    {"value" : (RomanYears[46], RomanMeans[46]), "label" : RomanTitles[46]},
    {"value" : (RomanYears[47], RomanMeans[47]), "label" : RomanTitles[47]},
    {"value" : (RomanYears[48], RomanMeans[48]), "label" : RomanTitles[48]},
    {"value" : (RomanYears[49], RomanMeans[49]), "label" : RomanTitles[49]},
    {"value" : (RomanYears[50], RomanMeans[50]), "label" : RomanTitles[50]},
    {"value" : (RomanYears[51], RomanMeans[51]), "label" : RomanTitles[51]},
    {"value" : (RomanYears[52], RomanMeans[52]), "label" : RomanTitles[52]},
    {"value" : (RomanYears[53], RomanMeans[53]), "label" : RomanTitles[53]},
    {"value" : (RomanYears[54], RomanMeans[54]), "label" : RomanTitles[54]},
    ], dots_size=7)
    chart.render_to_file(GraphFile)

# Coordination function
def scatter_time(DataFile, GraphFile):
    Data = read_data(DataFile)
    AutobTitles, AutobYears, AutobMeans, MaigrTitles, MaigrYears, MaigrMeans, RomanTitles, RomanYears, RomanMeans = make_datedata(Data)
    make_scatterplot(AutobTitles, AutobYears, AutobMeans, 
                     MaigrTitles, MaigrYears, MaigrMeans,
                     RomanTitles, RomanYears, RomanMeans,
                     GraphFile)
    
scatter_time(DataFile, GraphFile)






























