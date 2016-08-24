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


# Parameter definitions

InPath = "./txt/*.txt"
ResultFile = "AllResults.csv"

# Functions

def read_file(File):
    with open(File,"r") as InFile:
        Text = InFile.read()
        TextName, Ext = os.path.splitext(os.path.basename(File))
        print("Now:", TextName)
        return Text, TextName

def get_lengths(Text):
    Paras = re.split("\n", Text)
    LengthsWords = []
    for Para in Paras:
        #print(Para,"\n")
        if len(Para) > 2: 
            Sents = re.split("[\.?!]", Para)
            for Sent in Sents:
                if len(Sent) > 2:
                    Sent = re.sub("[\.,!?:;«»]"," ", Sent)
                    Sent = re.sub("[-]{2,4}"," ", Sent)
                    Sent = re.sub("[ ]{2,4}"," ", Sent)
                    Sent = re.sub("\t"," ", Sent)
                    Sent = Sent.strip()
                    #print(Sent)
                    Words = re.split("[\W'-]", Sent)
                    #print(Words)
                    LengthWords = len(Words)
                    LengthsWords.append(LengthWords)
    #print(LengthsWords)
    return LengthsWords
    
def get_stats(LengthsWords, TextName): 
    Words = sum(LengthsWords)
    Sents = len(LengthsWords)
    Mean = np.mean(LengthsWords)
    Median = np.median(LengthsWords)
    Stdev = np.std(LengthsWords)
    Stats = [Words, Sents, Mean, Median, Stdev]
    Stats = pd.Series(Stats, name=TextName)
    return Stats

def save_results(AllStats, ResultFile): 
    with open(ResultFile, "w") as OutFile: 
        AllStats.to_csv(OutFile)

# Coordination function

def sentencelength(InPath):
    AllStats = pd.DataFrame() # columns=["idno", "words", "sents", "mean", "median", "stdev"]
    for File in glob.glob(InPath):
        Text, TextName = read_file(File)
        LengthsWords = get_lengths(Text)
        Stats = get_stats(LengthsWords, TextName)
        AllStats = AllStats.append(Stats)
    save_results(AllStats, ResultFile)

sentencelength(InPath)
