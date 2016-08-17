#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: make_json.py
# Author: #cf, 2016.

import re

WorkDir = "/media/christof/data/Dropbox/0-Analysen/2016/martians/collatex/chapters/"

def read_file(File):
    with open(File, "r") as InFile: 
        Text = InFile.read()
        Text = re.sub("\n","<n/> ", Text)
        Text = re.sub("\"","<=/>", Text)
        Text = re.sub("\'","<-/>", Text)
        return Text

def merge_to_json(Text1, Text2):
    Json = "{   \"witnesses\" : [     {       \"id\" : \"M1\",       \"content\" : \"" + Text1 + "\"     }, {       \"id\" : \"M2\",       \"content\" : \"" + Text2 + "\"      }    ] }" 
    return Json

def save_json(Json, JsonFile):
    with open(JsonFile, "w") as OutFile: 
        OutFile.write(Json)   

def make_json(WorkDir):
    for i in range(1,26):
        ChID = '{:02d}'.format(i)
        print("Working on chapter", ChID)
        File = WorkDir+"martian1/martian1-ch"+ChID+".txt"
        Text = read_file(File)
        Text1 = Text
        File = WorkDir+"martian2/martian2-ch"+ChID+".txt"
        Text = read_file(File)
        Text2 = Text
        Json = merge_to_json(Text1, Text2)
        JsonFile = "./json/Martians-ch"+ChID+".json"
        save_json(Json, JsonFile)
    print("Done.")

make_json(WorkDir)