#!/usr/bin/env python3
# Filename: sentencelength.py

"""
# Create scatterplot from vocabulary richness data.
"""


# Import statements

import pandas as pd
import pygal
from pygal.style import Style


# Parameter definitions

WorkDir = "/media/christof/data/Dropbox/0-Analysen/2016/martians/sentences/"
DataFile = WorkDir+"results_RandomWindow-1000.csv"
MetadataFile = WorkDir+"metadata.csv"
GraphFile = WorkDir+"SLxCH.svg"


# Functions

def read_data(File):
    with open(File,"r") as InFile:
        Data = pd.DataFrame.from_csv(InFile)
        #print(Data.head(6))
        return Data

def merge_data(Data, Metadata):
    AllData = pd.merge(Data, Metadata, on="idno")
    #print(AllData.head(3))
    return AllData 


def make_tout_xydata(AllData): 
    #print(list(AllData.columns.values))
    GroupedData = AllData.groupby("version")
    OneData = GroupedData.get_group("version1")
    TwoData = GroupedData.get_group("version2")
    OnePoints = []  
    for i in range(0,len(OneData)): 
        XY = (OneData.iloc[i,10], OneData.iloc[i,3])  
        Label = str(OneData.iloc[i,11])+", ch. "+str(OneData.iloc[i,10])
        OnePoint = {"value" : XY, "label" : Label}
        OnePoints.append(OnePoint)
    TwoPoints = []    
    for i in range(0,len(TwoData)): 
        XY = (TwoData.iloc[i,10], TwoData.iloc[i,3])
        Label = str(TwoData.iloc[i,11])+", ch. "+str(TwoData.iloc[i,10])
        TwoPoint = {"value" : XY, "label" : Label}
        TwoPoints.append(TwoPoint)
    return OnePoints, TwoPoints


my_style = Style(
  background='white',
  plot_background='white',
  foreground='#282828',
  foreground_strong='#000000',
  foreground_subtle='#282828',
  opacity='.6',
  opacity_hover='.9',
  transition='100ms ease-in',
  font_family = "FreeSans",
  title_font_size = 20,
  legend_font_size = 16,
  label_font_size = 12,
  #colors=('#000000', '#707070', '#E0E0E0') # bw
  colors=('#003399', '#006600', '#004de6', '#009900') # blue-green
  )


def make_tout_xyplot(OnePoints, TwoPoints, GraphFile): 
    chart = pygal.XY(x_label_rotation=300,
                     stroke=False,
                     #range = (0.36, 0.56),
                     #xrange=(1900, 2000),
                     title="The Martian",
                     x_title="Chapter",
                     y_title="Mean sentence length",
                     show_x_guides=True,
                     show_y_guides=True,
                     legend_at_bottom=True,
                     pretty_print=True,
                     style=my_style)                
    chart.add("Martian1", OnePoints, dots_size=8)
    chart.add("Martian2", TwoPoints, dots_size=8)
    chart.add("Martian1 (mean)", [
    {"value": (1,10.2) , "label": "mean"}, 
    {"value": (26,10.2) , "label": "mean"}
    ], stroke=True, stroke_style={'width': 3}, dots_size=1)
    chart.add("Martian2 (mean)", [
    {"value": (1,10.4) , "label": "mean"}, 
    {"value": (26,10.4) , "label": "mean"}
    ], stroke=True, stroke_style={'width': 3}, dots_size=1)
    chart.render_to_file(GraphFile)


# Coordination function
def scatter_time(DataFile, MetadataFile, GraphFile):
    print("Launched")
    File = MetadataFile
    Data = read_data(File)
    Metadata = Data 
    File = DataFile
    Data = read_data(File)
    AllData = merge_data(Data, Metadata)
    OnePoints, TwoPoints = make_tout_xydata(AllData)
    make_tout_xyplot(OnePoints, TwoPoints, GraphFile)
    print("Done.")
    
scatter_time(DataFile, MetadataFile, GraphFile)






























