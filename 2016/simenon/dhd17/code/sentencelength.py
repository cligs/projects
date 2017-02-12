#!/usr/bin/env python3
# Filename: sentencelength.py
# Author: #cf
# New version: 2017-02-12


"""
Function to calculate sentence length statistics for a text collection.
"""


import re
import glob
import os
import pandas as pd
import numpy as np
import statistics as st
import nltk


# ==============================
# Parameter definitions
# ==============================

inpath = "./txt/*.txt"
results_file = "results.csv"


# ==============================
# Functions
# ==============================


def read_file(file):
    with open(file,"r") as infile:
        text = infile.read()
        textname, ext = os.path.splitext(os.path.basename(file))
        print("Now:", textname)
        return text, textname


def get_lengths(text):
    paras = re.split("\n", text)
    length_in_words_text = []
    for para in paras:
        #print(para,"\n")
        if len(para) > 2:
            #para = re.sub("\sM\.\s", " M ", para)
            #sents = re.split("[\.?!]", para)
            #sents = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", para)
            sents = nltk.sent_tokenize(para, language='french')
            for sent in sents:
                if len(sent) > 2:
                    sent = re.sub("[\.,!?:;«»]"," ", sent)
                    sent = re.sub("[-]{2,4}"," ", sent)
                    sent = re.sub("[ ]{2,4}"," ", sent)
                    sent = re.sub("peut-être","peut_être", sent)
                    sent = re.sub("soi-disant","soi_disant", sent)
                    sent = re.sub("aujourd'hui","aujourd_hui", sent)
                    sent = re.sub("-t-","-t_", sent)
                    sent = re.sub("\t"," ", sent)
                    sent = sent.strip()
                    #if "-" in sent or "_" in sent:
                    #    print(sent)
                    words = re.split("[\W]", sent)
                    #words = nltk.word_tokenize(sent)
                    #if "-" in words:
                    #    print(words)
                    # print(words)
                    length_in_words_sent = len(words)
                    length_in_words_text.append(length_in_words_sent)
    #print(len(length_in_words_text))
    return length_in_words_text

    
def get_stats(length_in_words_text, textname): 
    words = sum(length_in_words_text)
    sents = len(length_in_words_text)
    mean = np.mean(length_in_words_text)
    median = np.median(length_in_words_text)
    try:
        mode = st.mode(length_in_words_text)
    except:
        mode = "N/A"
    stdev = np.std(length_in_words_text)
    stats = [words, sents, mean, median, mode, stdev]
    stats = pd.Series(stats, name=textname)
    #print(stats)
    return stats


def save_results(allstats, results_file):
    allstats.columns = ["words", "sents", "mean", "median", "mode", "stdev"]
    print(allstats)
    with open(results_file, "w") as outfile: 
        allstats.to_csv(outfile)


# ==============================
# Coordination function
# ==============================


def sentencelength(inpath, results_file):
    allstats = pd.DataFrame()
    for file in glob.glob(inpath):
        text, textname = read_file(file)
        length_in_words_text = get_lengths(text)
        stats = get_stats(length_in_words_text, textname)
        allstats = allstats.append(stats)
    save_results(allstats, results_file)

sentencelength(inpath, results_file)
