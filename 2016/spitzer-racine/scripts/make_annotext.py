#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to create annotation-based pseudo-text from Freeling XML output.
"""

import os
import glob
import re
#import numpy as np
#import pandas as pd


# Input path with Freeling XML files
XMLPath = "./texts/*.xml"
# Type of annotation to use: form|lemma|pos|tag|wnlex
Annotation = "wnlex"
# Ngram size to use: uni|bi|tri
Ngrams = "uni" 
# Output folder where the annotated files go
OutFolder = "./"+Annotation+"-"+Ngrams+"/"
if not os.path.exists(OutFolder):
    os.makedirs(OutFolder)


# Subfunctions
def read_xmlfile(File):
    with open(File, "r") as infile:
        XMLText = infile.read()
        return XMLText

def extract_annos(XMLText, Annotation, Ngrams):
    Query = Annotation+"=\".*?\""
    QueryList = re.findall(Query, XMLText)
    AnnoList = []
    for Anno in QueryList: 
        Anno = re.sub("\"", "", Anno)
        Anno = re.sub("tag=", "", Anno)
        if Annotation == "pos":
            Anno = re.sub("pos=", "", Anno)
        elif Annotation == "tag":
            Anno = Anno[0:2]
        elif Annotation == "form":
            Anno = re.sub("form=", "", Anno)
        elif Annotation == "lemma":
            Anno = re.sub("lemma=", "", Anno)
        elif Annotation == "wnlex":
            Anno = re.sub("wnlex=", "", Anno)
            Anno = re.sub("\.", "_", Anno)
        AnnoList.append(Anno)
    
    if Ngrams == "uni": 
        AnnoString = " ".join(AnnoList)
    if Ngrams == "bi": 
        AnnoString = ""
        for i in range(0, len(AnnoList)-2): 
            Anno1 = AnnoList[i]
            Anno2 = AnnoList[i+1]
            Anno = Anno1+"-"+Anno2
            AnnoString = AnnoString+Anno+" "

    if Ngrams == "tri": 
        AnnoString = ""
        for i in range(0, len(AnnoList)-3): 
            Anno1 = AnnoList[i]
            Anno2 = AnnoList[i+1]
            Anno3 = AnnoList[i+2]
            Anno = Anno1+"-"+Anno2+"-"+Anno3
            AnnoString = AnnoString+Anno+" "

    return AnnoString

def save_textfile(AnnoString, OutFolder, idno):
    OutFile = OutFolder+idno+".txt"
    with open(OutFile, "w") as outfile:
        outfile.write(AnnoString)


# Manager function
def make_postext(XMLPath,
                 Annotation,
                 Ngrams,
                 OutFolder):
    """
    Function to create annotation-based pseudo-text from Freeling XML output.
    Author: #cf.
    """
    for File in glob.glob(XMLPath): 
        idno,ext = os.path.basename(File).split(".")
        print("Working on:", idno)
        XMLText = read_xmlfile(File)
        AnnoString = extract_annos(XMLText, Annotation, Ngrams)
        save_textfile(AnnoString, OutFolder, idno)

# Function call
make_postext(XMLPath,
             Annotation,
             Ngrams,
             OutFolder)
                    

