#!/usr/bin/env python3
# Filename: my_tmw.py
# Author: #cf
# Version 0.2.0 (2015-08-27)


import visualize

### Set the general working directory.
wdir = "/media/christof/data/Dropbox/0-Analysen/2016/gddh-dhq/tc391zz/" # end with slash.
number_of_topics = 60

### make_wordle_from_mallet
### Creates a wordle for each topic.
word_weights_file = wdir + "7_model/word-weights_060tp-6000it-0300in.csv"
topics = 60
words = 40
outfolder = wdir + "9_visuals/060tp-0300in/wordles/"
font_path = wdir + "extras/AlegreyaSans-Regular.otf"
dpi = 300
num_topics = number_of_topics
TopicRanksFile = wdir + "9_aggregates/060tp-0300in/topicRanks.csv"
#visualize.make_wordle_from_mallet(word_weights_file,
#                                  num_topics, 
#                                  words,
#                                  TopicRanksFile,                                  
#                                  outfolder,
#                                  font_path,
#                                  dpi)

### crop_images
### Crops the wordle image files, use if needed.
inpath = wdir + "9_visuals/060tp-0300in/wordles/*.png"
outfolder = wdir + "9_visuals/060tp-0300in/wordles/"
left = 500 # image start at the left
upper = 50 # image start at the top
right = 3400 # image end on the right
lower = 2350 # image end at the bottom
#visualize.crop_images(inpath, outfolder, left, upper, right, lower)

### plot_topTopics
### For each item from a category, creates a barchart of the top topics.
averageDatasets = wdir+"/7_aggregates/060tp-0300in/avg*.csv" 
firstWordsFile = wdir+"/7_aggregates/060tp-0300in/firstWords.csv"
numberOfTopics = 250 # must be actual number of topics modeled.
targetCategories = ["author-name", "author-gender", "decade", "subgenre", "title"] 
# one or several: "author-name", "author-gender", "decade", "subgenre", "title"
topTopicsShown = 30 
fontscale = 1.0
height = 0 # 0=automatic and variable
dpi = 300
outfolder = wdir+"/8_visuals/060tp-0300in/topTopics/"
#tmw.plot_topTopics(averageDatasets, firstWordsFile, numberOfTopics, targetCategories, topTopicsShown, fontscale, height, dpi, outfolder)

### plot_topItems
### For each topic, creates a barchart with top items from a category. 
averageDatasets = wdir+"/9_aggregates/060tp-0300in/avg*.csv" 
outfolder = wdir+"/9_visuals/060tp-0300in/topItems/"
firstWordsFile = wdir+"9_aggregates/060tp-0300in/firstWords.csv"
numberOfTopics = 60 # must be actual number of topics modeled. 
targetCategories = ["tc_author-short", "tc_subgenre", "idno",] 
# choose one or several from: author-name, decade, subgenre, gender, idno, title, segmentID
topItemsShown = 20 
fontscale = 0.8
height = 0 # 0=automatic and flexible
dpi = 300
visualize.plot_topItems(averageDatasets, outfolder, firstWordsFile, numberOfTopics, targetCategories, topItemsShown, fontscale, height, dpi)

### plot_distinctiveness_heatmap
### For each category, make a heatmap of most distinctive topics. 
averageDatasets = wdir+"9_aggregates/060tp-0300in/avg*.csv" 
firstWordsFile = wdir+"9_aggregates/060tp-0300in/firstWords.csv"
outfolder = wdir+"9_visuals/060tp-0300in/distinctiveness/"
targetCategories = ["tc_subgenre"] 
# one or several: "author-name", "decade", "subgenre", "gender", "idno", "title"
numberOfTopics = 60 # must be actual number of topics modeled.
topTopicsShown = 20 
mode = "meannorm" # meannorm|mediannorm|zscores|absolute
sorting = "std"
fontscale = 1.0
dpi = 300
#visualize.plot_distinctiveness_heatmap(averageDatasets, firstWordsFile, outfolder, targetCategories, numberOfTopics, topTopicsShown, mode, sorting, fontscale, dpi)

### plot_topicsOverTime
### Creates lineplots or areaplots for topic development over time.
#averageDatasets = wdir+"/7_aggregates/avgtopicscores_by-decade.csv" 
#firstWordsFile = wdir+"/7_aggregates/firstWords.csv"
#outfolder = wdir+"/8_visuals/overTime/"
#numberOfTopics = 250 # must be actual number of topics modeled.
#fontscale = 1.0
#dpi = 300
#height = 0 # for lineplot; 0=automatic
#mode = "line" # area|line for areaplot or lineplot
#topics = ["48","67","199"] # list of one or several topics
#tmw.plot_topicsOverTime(averageDatasets, firstWordsFile, outfolder, numberOfTopics, fontscale, dpi, height, mode, topics)
