#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: martians.py
# Author: #cf, 2016.

#diff_file = "wdiff_test.txt"
diff_file = "wdiffed_nowraps.txt"
diff_table_file = "diff_table.csv"

import pandas as pd
import re
import Levenshtein as ld

def extract_diffs(diff_file, diff_table_file): 
    with open(diff_file, "r") as df: 
        diff_text = df.read()
        diff_text = re.split("\n", diff_text)
        line_number = 0
        all_diffs = []
        for line in diff_text:
            line_number +=1
            line = re.sub("]{", "] {", line)
            line = re.sub("(-\]) ([^{])", "\\1 {++} \\2", line)
            line = re.sub("(\w) ({)", "\\1 [--] \\2", line)
            pairs = re.findall("\[-.*?\-\] {\+.*?\+}", line, re.DOTALL)
            item_number = 0
            for item in pairs: 
                item_number += 1
                #print(item_number, item)
                item = re.split("\] {", item)
                item_id = str(line_number)+"-"+str(item_number)
                item1 = item[0][2:-1]
                item2 = item[1][1:-2]
                insertion = 0
                deletion = 0
                capitalization = 0
                whitespace = 0
                italics = 0
                punctuation = 0
                hyphenation = 0
                numbers = 0
                condensation = 0
                expansion = 0
                xxTBCxx = 0
                if len(item1) == 0:
                    type = "insertion"
                    insertion = 1
                elif len(item2) == 0:
                    type = "deletion"
                    deletion = 1
                elif item1.lower() == item2.lower(): 
                    type = "capitalization"
                    capitalization = 1
                elif re.sub(" ","",item1) == re.sub(" ","",item2): 
                    type = "whitespace"
                    whitespace = 1
                elif re.sub("\*","",item1) == re.sub("\*","",item2): 
                    type = "italics"
                    italics = 1
                elif re.sub("[\",';:!?\.\(\)]","",item1) == re.sub("[\",';:!?\.\(\)]","",item2): 
                    type = "punctuation"
                    punctuation = 1
                elif re.sub("\-","",item1) == re.sub(" ","",item2): 
                    type = "hyphenation"
                    hyphenation = 1
                elif re.sub(" ","",item1) == re.sub("\-","",item2): 
                    type = "hyphenation"
                    hyphenation = 1
                elif bool(re.search(r'\d', item1+item2)) == True:
                    type = "numbers"
                    numbers = 1
                elif len(item1) > len(item2)+3:
                    type = "condensation"
                    condensation = 1
                elif len(item2) > len(item1)+3:
                    type = "expansion"
                    expansion = 1
                else: 
                    type = "xxTBCxx"
                    xxTBCxx = 1
                levenshtein = ld.distance(item1, item2)
                complete_item = [item_id, item1, item2, levenshtein, type, insertion, deletion, capitalization, whitespace, italics, punctuation, hyphenation, numbers, condensation, expansion, xxTBCxx]
                all_diffs.append(complete_item)
    diff_df = pd.DataFrame(all_diffs, columns=["item-id","version1","version2", "levenshtein",  "type", "insertion", "deletion", "capitalization", "whitespace", "italics", "punctuation", "hyphenation", "numbers", "condensation", "expansion", "xxTBCxx"])
    print(diff_df)
    with open(diff_table_file, "w") as dt: 
        diff_df.to_csv(dt, index=False)
            
extract_diffs(diff_file, diff_table_file)