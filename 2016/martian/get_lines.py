#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: get_lines.py
# Authors: #cf
# 2016-05-21


import re
import os
import glob
import pandas as pd


WorkDir = "/media/christof/data/Dropbox/0-Analysen/2016/martians/diffs5/"
DiffTable = WorkDir+"DiffTable_2016-04-29.csv"
DiffedText = WorkDir+"martians_wdiffed-prep.txt"
Types = ["deletion-major", "deletion-minor", "expansion-major", "expansion-minor"]


def get_lines(DiffTable, DiffedText, Types): 
    """
    Collect line IDs with expansions / deletions, get lines from diffed text, write into separate file.
    Author: #cf.
    """
    print("get_lines...")
    
    # Open and read the DiffTable
    with open(DiffTable, "r") as InFile:
        Diffs = pd.DataFrame.from_csv(InFile, sep="\t")
    with open(DiffedText, "r") as InFile: 
        Text = InFile.read()
        Text = re.split("\n", Text)
        #print(Diffs.head())
        # For each type of edir, get the line-ids
        for Type in Types: 
            Items = Diffs.loc[Diffs['type'] == Type]
            #print(Type, len(Items))
            ItemIDs = Items.index.values
            #print(ItemIDs)
            LineIDs = []
            for ItemID in ItemIDs:
                LineID = int(ItemID[:-2])
                LineIDs.append(LineID)
            #print(len(LineIDs))
            #print(LineIDs)
            
            Lines = []
            for LineID in LineIDs:
                Line = "-- " + '{:05d}'.format(LineID-1) + ": " + Text[LineID-2]
                Lines.append(Line)
                Line = "=> " + '{:05d}'.format(LineID) + ": " + Text[LineID-1]
                Lines.append(Line)
                Line = "-- " + '{:05d}'.format(LineID+1) + ": " + Text[LineID-0] + "\n"
                Lines.append(Line)
            Lines = "\n".join(Lines)
            
            LinesFile = "./lines/lines_"+str(Type)+".txt"
            with open(LinesFile, "w") as OutFile: 
                OutFile.write(Lines)
            
        

        #with open(TXMFolder+Filename[:-7]+".xml", "w") as OutFile: 
        #     OutFile.write(NewNewText)
                
                
                

    print("Done.")
    

get_lines(DiffTable, DiffedText, Types)
    

