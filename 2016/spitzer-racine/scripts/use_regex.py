#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to apply regular expressions to collections of texts. 
"""

import re
import os
import glob
import pandas as pd


# Define RegEx Query here
#L1y# Query = ".* (\w{5,8}) .{0,80} \\1.*" # repetition inside a line.
Query = ".* (\w{5,8}) .{0,25} \\1.*" #L1

# Other parameters
TextPath = "txt/*.txt"
CountsTemplate = "template_counts.csv"
HitsFile = "results_hits.csv"
CountsFile = "results_counts.csv"


def use_regex(Query, 
              TextPath, 
              HitsFile,
              CountsTemplate,
              CountsFile):

    open(HitsFile, "w").close()
    HitCounter = 0
    with open(CountsTemplate, "r") as infile:
        Counts = pd.DataFrame.from_csv(infile, sep=",")
        print(Counts)
        
    with open(HitsFile, "a") as outfile: 
        for file in glob.glob(TextPath):
            idno = os.path.basename(file)[:-4]
            with open(file, "r") as infile:
                text = infile.read()
                text = re.split("\n", text) 
            
                for line in text: 
                    #print(line)
                    hit = re.search(Query, line)
                    if hit != None:
                        HitCounter +=1
                        #df.ix[0, 'COL_NAME'] = x
                        Counts.ix["counts",idno] +=1
                        Hit = idno + "\t" + line + "\n"
                        #print(Hit)
                        outfile.write(Hit)
        print(Counts)
        Counts.to_csv(CountsFile, sep=";")
                        
    print("Total hits:", HitCounter)
            


use_regex(Query,
          TextPath,
          HitsFile,
          CountsTemplate,
          CountsFile)    

