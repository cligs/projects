#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: #cf
# Version: 0.1, 2016-06-13

"""
Script to make barcharts.
"""

InputData = "AllResults.csv"
GraphFileName = "comparison-statistics"

import pandas as pd
import pygal
from pygal.style import BlueStyle


def make_barchart(InputData,
                  GraphFileName):
        """
        This script expects a data table. 
        Items should be in the rows and columns should be various types of variables.
        """
        with open(InputData, "r") as infile: 
            DataTable = pd.DataFrame.from_csv(infile, sep=",", index_col=None)
            DataTable = DataTable.sort_values("MeanRatio12", ascending=False)
            #print(DataTable)
            
            Items = DataTable.loc[:,"Code"].values.tolist()
            Labels = DataTable.loc[:,"Labels"].values.tolist()
            Ratio12 = DataTable.iloc[:,4].values.tolist()
            Wilcoxon = DataTable.iloc[:,10].values.tolist()
            #print(Items)
            #print(Wilcoxon[0])
            
            #bar = pygal.Bar(show_legend=True, x_label_rotation=0)
            bar = pygal.Bar(show_legend=False, 
                            x_label_rotation=295,
                            show_labels=True,
                            style = BlueStyle)
            #bar.title = "Beispiele in Spitzers Sourdine-Artikel"
            bar.x_title = "Stilistische Phänomene"
            bar.y_title = "Verhältnis der Mittelwerte Racine/Proches"
            #bar.x_labels = Items
            #bar.add("Ratio", Ratio12, rounded_bars=2)
            for i in range(0,len(Items)-1):
                #print(Ratio12[i])
                #print(Labels[i])
                if Wilcoxon[i] < 0.05: 
                    color = "RoyalBlue"
                else:
                    color = "#7eaacd"
                bar.add(Items[i], [{"value" : Ratio12[i], "color" : color, "label" : Labels[i]}], rounded_bars=3)
            bar.render_to_file(GraphFileName+"_MeanRatio12.svg")


make_barchart(InputData,
                  GraphFileName)