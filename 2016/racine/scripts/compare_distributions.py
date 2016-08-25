#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to compare the relative frequency distributions of one query result in two partitions.
"""

import os
import glob
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import pygal


# Output table from TXM for the results of a given query
#AbsFreqsFileList = ["A1.csv", "A2.csv", "A3.csv"] # use for a specific list
AbsFreqsFileList = glob.glob("input/*.csv") # use for all input files in a folder
# Token frequency counts for each title (text length)
TokenCountsFile = "idnos-tokens.csv"
# List of column headers (identifiers) for texts belonging to partition 1 (Racine)
Partition1 = ["tc0649", "tc0651", "tc0653", "tc0654", "tc0655", "tc0656", "tc0657", "tc0658", "tc0659", "tc0661", "tc0664"] 
# List of column headers (identifiers) for texts belonging to partition 2 (Proches)
Partition2 = ["tc0093", "tc0094", "tc0096", "tc0098", "tc0101", "tc0113", "tc0114", "tc0115", "tc0116", "tc0117", "tc0118", "tc0163", "tc0165", "tc0183", "tc0189", "tc0190", "tc0193", "tc0196", "tc0200", "tc0203", "tc0204", "tc0206", "tc0207", "tc0219", "tc0221", "tc0222", "tc0224", "tc0225", "tc0226", "tc0227", "tc0628", "tc0629", "tc0630", "tc0632", "tc0636", "tc0637", "tc0645", "tc0648"]  
# Output file: table of types x test results


def compare_dists_loop(AbsFreqsFileList,
                       TokenCountsFile,
                       Partition1,
                       Partition2):

    AllRelFreqs = pd.DataFrame()
    for AbsFreqsFile in AbsFreqsFileList:

        # PREPARE DATA        
        
        # Give this test an identifier based on the filename / code
        Code = os.path.basename(AbsFreqsFile)[:-4] 
        print("Now working on query", Code)
        ResultsFile = "results/"+str(os.path.basename(AbsFreqsFile)[:-4])+"-statistics.csv"

        # Load absolute frequencies and wordcounts; make relative frequencies
        AbsFreqs = pd.read_csv(AbsFreqsFile, sep=";")
        AbsFreqs = AbsFreqs.iloc[:,2:].sum(axis=0)
        #print(AbsFreqs)
        TokenCounts = pd.read_csv(TokenCountsFile, sep=",")
        TokenCounts = TokenCounts.iloc[:,1:]
        RelFreqs = AbsFreqs/TokenCounts*1000
        AllRelFreqs = AllRelFreqs.append(RelFreqs)
        #print(RelFreqs)
        
        # Split the relative frequencies into the two partitions
        RelFreqsP1 = RelFreqs[Partition1]
        RelFreqsP2 = RelFreqs[Partition2] 
        P1 = RelFreqsP1.iloc[0].values.tolist()
        P2 = RelFreqsP2.iloc[0].values.tolist()
 
 
        # CALCULATE BASIC STATISTICS 
 
        #MeanP1, MeanP2, MeanRatio12, MedianRatio12
        MeanP1 = np.mean(P1)
        MeanP2 = np.mean(P2)
        #print(MeanP1,MeanP2)
        MedianP1 = np.median(P1)
        MedianP2 = np.median(P2)
        #print(MedianP1, MedianP2)
        MeanRatio12 = (MeanP1+0.00000001)/(MeanP2+0.00000001)
        MedianRatio12 = (MedianP1+0.00000001)/(MedianP2+0.00000001)
        MeanRatioAbs = abs(MeanRatio12-1)
        #print(MeanRatio12, MedianRatio12, MeanRatioAbs)
        
        
        # VISUAL COMPARISON
        
        # Box plot
        box = pygal.Box(show_legend=False)
        box.title = "Häufigkeitsverteilung für: "+str(Code)
        box.x_title = "Partitionen"
        box.y_title = "Häufigkeit pro 1000 Tokens"
        box.x_labels = "Racine", "Proches"
        box.add("Racine", P1)
        box.add("Proches", P2)
        box.render_to_file("results/"+str(Code)+"-boxplot.svg")
        
        if Code == "G4": 
            sns.distplot(P2, rug=False, kde=False, bins=5)
            sns.distplot(P2, rug=False, kde=False, bins=6)
            #sns.kdeplot(P1)
            #sns.distplot(P2, rug=False, bins=5)
            plt.savefig("results/"+str(Code)+"-distplot.svg")
            plt.close()
        


        # TEST STATISTICS
        
        # Welchs
        # http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ttest_ind.html
        Welch = stats.ttest_ind(P1, P2, equal_var=False)
        WelchP = str(Welch[1])
        #print(Welch)

        # Wilcoxon's rank sum test
        # http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ranksums.html
        Wilcoxon = stats.ranksums(P1, P2)
        WilcoxonP = str(Wilcoxon[1])
        #print(Wilcoxon)
                    
        # Kolmogorov-Smirnov test
        # http://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.stats.ks_2samp.html
        Kolmogorov = stats.ks_2samp(P1, P2)
        KolmogorovP = str(Kolmogorov[1])
           
        
        # SAVE RESULTS
        
        # Put the results together in a list
        #Headers = ["Code", "MeanP1", "MeanP2", "Ratio12", "Welch", "Wilcoxon", "Kolmogorov"]
        Results = [Code, MeanP1, MeanP2, MeanRatio12, MeanRatioAbs, MedianP1, MedianP2, MedianRatio12, WelchP, WilcoxonP, KolmogorovP]
        with open(ResultsFile, "w") as outfile: 
            wr = csv.writer(outfile,delimiter=",")
            wr.writerow(Results)
        # Note: To merge all results later, do "cat *.csv > AllResults.csv" in Terminal
            
    #print(AllRelFreqs)
    with open("AllRelFreqs.csv", "w") as outfile: 
        AllRelFreqs.to_csv(outfile)

compare_dists_loop(AbsFreqsFileList,
                   TokenCountsFile,
                   Partition1,
                   Partition2)
