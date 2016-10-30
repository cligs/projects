#!/usr/bin/env python3
# Filename: sentencelength.py

"""
# The Wilcoxon signed-rank test tests the null hypothesis that two related paired samples come from the same distribution. 
# statistic : The sum of the ranks of the differences above or below zero, whichever is smaller.
# pvalue : The two-sided p-value for the test; how likely is it that this result has been obtained by chance?
# Details: http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html
"""


# Import statements

import pandas as pd
import scipy.stats as stats
import itertools as itt
import csv


# Parameter definitions

WorkDir = "/media/christof/data/Dropbox/0-Analysen/2016/martians/sentences/"
DataFile = WorkDir+"results_RandomWindow-1000.csv"
MetadataFile = WorkDir+"metadata.csv"
ResultFile = WorkDir+"significance_narration.csv"

# Functions

def read_data(File):
    with open(File,"r") as InFile:
        Data = pd.DataFrame.from_csv(InFile)
        return Data

def merge_data(Data, Metadata):
    AllData = pd.merge(Data, Metadata, on="idno")
    print(AllData.head())
    return AllData 

def check_significance(AllData):
    GroupedData = AllData.groupby("narrative")
    OneData = GroupedData.get_group("first")
    #print(len(OneData))
    TwoData = GroupedData.get_group("third")
    #print(len(TwoData))
    AllSigs = [["feature", "statistic", "p-value"]]
    AllHeads = ["NumWords", "NumSents", "SLMean", "SLMedian", "SLStdev", "TTR-mean", "TTR-stdev", "BVR-mean", "BVR-stdev"]
    print(OneData.iloc[0:23,3], TwoData.iloc[0:23,3])
    Significance =  stats.wilcoxon(OneData.iloc[0:20,3], TwoData.iloc[0:20,3])
    Result = ["SLMean", Significance[0], Significance[1]]
    #print(Result)
    AllSigs.append(Result)
    return AllSigs

    
def save_data(AllCorrs, ResultFile): 
    with open(ResultFile, "w") as OutFile:
        writer = csv.writer(OutFile)
        writer.writerows(AllCorrs)

# Coordination function
def test_significance(DataFile, MetadataFile, ResultFile):
    print("Launched...")
    File = MetadataFile
    Data = read_data(File)
    Metadata = Data 
    File = DataFile
    Data = read_data(File)
    AllData = merge_data(Data, Metadata)
    AllSigs = check_significance(AllData)
    save_data(AllSigs, ResultFile)
    print("Done.")
    
test_significance(DataFile, MetadataFile, ResultFile)






























