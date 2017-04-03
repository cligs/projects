#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: topicpca.py
# Author: #cf


"""
Set of functions to perform clustering on data. 
Built for topic probabilities or word frequencies as input. 
Performs Principal Component Analysis or distance-based clustering.
"""

import os, glob, re
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import pygal
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering as AC
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from sklearn import metrics
from scipy.cluster.hierarchy import fcluster
from scipy import stats


# =================================
# Shared functions
# =================================

def get_mastermatrix(mastermatrix_file):
    with open(mastermatrix_file, "r") as infile:
        mastermatrix = pd.read_csv(infile)
        # print(mastermatrix.head())
        return mastermatrix


def get_topicdata(mastermatrix): 
    grouped = mastermatrix.groupby(by=["idno"])
    topicdata = grouped.agg(np.mean)
    topicdata = topicdata.iloc[:,5:-1]
    identifiers = topicdata.index.values
    # print(topicdata)
    # print(identifiers)
    return topicdata, identifiers


def get_metadata(metadata_file):
    with open(metadata_file, "r") as infile:
        metadata = pd.read_csv(infile, sep=";")
        # print(metadata.head())
        return metadata


def get_wordfreqs(WordfreqsFile):
    with open(WordfreqsFile, "r") as InFile:
        Wordfreqs = pd.read_csv(InFile, sep=";")
        #print(Wordfreqs.head())
        return Wordfreqs


def get_freqdata(Wordfreqs, MFW): 
    FreqData = Wordfreqs.iloc[0:MFW,1:]
    FreqDataMean = np.mean(FreqData, axis=1)
    FreqDataStd = np.std(FreqData, axis=1)
    FreqData = FreqData.subtract(FreqDataMean, axis=0)
    FreqData = FreqData.divide(FreqDataStd, axis=0)
    FreqData = FreqData.T
    #print(FreqData.head())
    Identifiers = list(FreqData.index.values)
    #print(Identifiers)
    return FreqData, Identifiers



##################################
# Cluster Analysis with topics
##################################

tc_style = pygal.style.Style(
    background='white',
    plot_background='white',
    font_family = "FreeSans",
    title_font_size = 20,
    legend_font_size = 16,
    label_font_size = 12,
    colors=["#1d91c0","#225ea8","#253494","#081d58", "#071746"])


def get_labels_tc(Identifiers, MetadataFile): 
    with open(MetadataFile, "r") as InFile: 
        Metadata = pd.read_csv(InFile, sep=";")
        Metadata.set_index("idno", inplace=True)
        #print(Metadata.head())
        #print(Identifiers)
        Labels = []
        Colors = []
        GroundTruth = []
        for Item in Identifiers:
            if Metadata.loc[Item,"tc_subgenre"] == "Comédie": 
                Labels.append(Item+"-CO")
                Colors.append("darkred")
                GroundTruth.append(0)
            if Metadata.loc[Item,"tc_subgenre"] == "Tragi-comédie":
                Labels.append(Item+"-TC")
                Colors.append("darkgreen")
                GroundTruth.append(1)
            elif Metadata.loc[Item,"tc_subgenre"] == "Tragédie": 
                Labels.append(Item+"-TR")
                Colors.append("darkblue")
                GroundTruth.append(2)
        #print(Labels)
        return Labels, Colors, GroundTruth


def clusteranalysis(TopicData, Method, Metric):
    """
    docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
    """
    # perform the cluster analysis
    LinkageMatrix = linkage(TopicData, method=Method, metric=Metric)
    #print(LinkageMatrix[0:10])
    return LinkageMatrix

    
def make_dendrogram(LinkageMatrix, GraphFolder, 
                    Method, Metric, CorrCoeff, Labels, Colors,
                    DisplayLevels):
    import matplotlib
    if not os.path.exists(GraphFolder):
        os.makedirs(GraphFolder)
    plt.figure(figsize=(12,24))
    plt.title("Plays clustered by topic probabilities", fontsize=14)
    #plt.ylabel("Parameters: "+Method+" method, "+Metric+" metric. CorrCoeff: "+str(CorrCoeff)+".")
    plt.xlabel("Distance\n(Parameters: "+Method+" / "+Metric+")", fontsize=12)
    matplotlib.rcParams['lines.linewidth'] = 1.2
    dendrogram(
        LinkageMatrix,
        p = DisplayLevels,
        truncate_mode="level",
        color_threshold = 1.3,
        show_leaf_counts = True,
        no_labels = False,
        orientation="left",
        labels = Labels, 
        leaf_rotation = 0,  # rotates the x axis labels
        leaf_font_size = 4,  # font size for the x axis labels
        )
    #plt.show()
    plt.savefig(GraphFolder+"dendrogram_"+Method+"-"+Metric+"-"+str(DisplayLevels)+".png", dpi=300, figsize=(12,18), bbox_inches="tight")
    plt.close()


def evaluate_cluster(TopicData, LinkageMatrix, GroundTruth): 
    # check the correlation coefficient
    CorrCoeff, coph_dists = cophenet(LinkageMatrix, pdist(TopicData))
    ## check several cluster evaluation metrics
    Threshold = 2
    FlatClusterNumbers = fcluster(LinkageMatrix, Threshold)
    #print(GroundTruth)
    #print(FlatClusterNumbers)
    ARI = metrics.adjusted_rand_score(GroundTruth, FlatClusterNumbers)
    Homog = metrics.homogeneity_score(GroundTruth, FlatClusterNumbers)
    Compl = metrics.completeness_score(GroundTruth, FlatClusterNumbers) 
    VMeasure = metrics.v_measure_score(GroundTruth, FlatClusterNumbers) 
    print("Evaluation metrics with threshold "+str(Threshold))
    print("CorrCoeff:", CorrCoeff)
    print("adjustedRI:", ARI)
    print("Homogeneity:", Homog)
    print("Completeness:", Compl)
    print("V-Measure:", VMeasure)
    return CorrCoeff, ARI, Homog, Compl, VMeasure


def topiccluster(MastermatrixFile,
                 MetadataFile, 
                 Method,
                 Metric,
                 GraphFolder,
                 DisplayLevels):
    print("Launched topiccluster.")
    Mastermatrix =  get_mastermatrix(MastermatrixFile)
    TopicData, Identifiers = get_topicdata(Mastermatrix)
    Labels, Colors, GroundTruth = get_labels_tc(Identifiers, MetadataFile)
    LinkageMatrix = clusteranalysis(TopicData, Method, Metric)
    CorrCoeff, ARI, Homog, Compl, VMeasure = evaluate_cluster(TopicData, 
                                                              LinkageMatrix, 
                                                              GroundTruth)
    make_dendrogram(LinkageMatrix, GraphFolder, 
                    Method, Metric, 
                    CorrCoeff, Labels, Colors, 
                    DisplayLevels)
    
    print("Done.")











##################################
# Cluster Analysis with words
##################################

tc_style = pygal.style.Style(
    background='white',
    plot_background='white',
    font_family = "FreeSans",
    title_font_size = 20,
    legend_font_size = 16,
    label_font_size = 12,
    colors=["#1d91c0","#225ea8","#253494","#081d58", "#071746"])


def get_labels_wc(Identifiers, MetadataFile): 
    with open(MetadataFile, "r") as InFile: 
        Metadata = pd.read_csv(InFile, sep=";")
        Metadata.set_index("idno", inplace=True)
        #print(Metadata.head())
        #print(Identifiers)
        Labels = []
        Colors = []
        GroundTruth = []
        for Item in Identifiers:
            if Metadata.loc[Item,"tc_subgenre"] == "Comédie": 
                Labels.append(Item+"-CO")
                Colors.append("darkred")
                GroundTruth.append(0)
            if Metadata.loc[Item,"tc_subgenre"] == "Tragi-comédie":
                Labels.append(Item+"-TC")
                Colors.append("darkgreen")
                GroundTruth.append(1)
            elif Metadata.loc[Item,"tc_subgenre"] == "Tragédie": 
                Labels.append(Item+"-TR")
                Colors.append("darkblue")
                GroundTruth.append(2)
        #print(Labels)
        return Labels, Colors, GroundTruth


def clusteranalysis_w(TopicData, Method, Metric):
    """
    docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
    """
    # perform the cluster analysis
    LinkageMatrix = linkage(TopicData, method=Method, metric=Metric)
    #print(LinkageMatrix[0:10])
    return LinkageMatrix

    
def make_dendrogram_w(LinkageMatrix, GraphFolder, 
                    Method, Metric, CorrCoeff, Labels, Colors,
                    DisplayLevels):
    import matplotlib
    if not os.path.exists(GraphFolder):
        os.makedirs(GraphFolder)
    plt.figure(figsize=(12,24))
    plt.title("Plays clustered by topic probabilities", fontsize=14)
    #plt.ylabel("Parameters: "+Method+" method, "+Metric+" metric. CorrCoeff: "+str(CorrCoeff)+".")
    plt.xlabel("Distance\n(Parameters: "+Method+" / "+Metric+")", fontsize=12)
    matplotlib.rcParams['lines.linewidth'] = 1.2
    dendrogram(
        LinkageMatrix,
        p = DisplayLevels,
        truncate_mode="level",
        color_threshold = 30,
        show_leaf_counts = True,
        no_labels = False,
        orientation="left",
        labels = Labels, 
        leaf_rotation = 0,  # rotates the x axis labels
        leaf_font_size = 4,  # font size for the x axis labels
        )
    #plt.show()
    plt.savefig(GraphFolder+"dendrogram_"+Method+"-"+Metric+"-"+str(DisplayLevels)+".png", dpi=300, figsize=(12,18), bbox_inches="tight")
    plt.close()


def evaluate_cluster_w(TopicData, LinkageMatrix, GroundTruth): 
    # check the correlation coefficient
    CorrCoeff, coph_dists = cophenet(LinkageMatrix, pdist(TopicData))
    ## check several cluster evaluation metrics
    Threshold = 2
    FlatClusterNumbers = fcluster(LinkageMatrix, Threshold)
    #print(GroundTruth)
    #print(FlatClusterNumbers)
    ARI = metrics.adjusted_rand_score(GroundTruth, FlatClusterNumbers)
    Homog = metrics.homogeneity_score(GroundTruth, FlatClusterNumbers)
    Compl = metrics.completeness_score(GroundTruth, FlatClusterNumbers) 
    VMeasure = metrics.v_measure_score(GroundTruth, FlatClusterNumbers) 
    print("Evaluation metrics with threshold "+str(Threshold))
    print("CorrCoeff:", CorrCoeff)
    print("adjustedRI:", ARI)
    print("Homogeneity:", Homog)
    print("Completeness:", Compl)
    print("V-Measure:", VMeasure)
    return CorrCoeff, ARI, Homog, Compl, VMeasure


def wordcluster(WordfreqsFile,
                AllMFW,
                MetadataFile, 
                Method,
                Metric,
                GraphFolder,
                DisplayLevels):
    print("Launched wordcluster.")
    Wordfreqs =  get_wordfreqs(WordfreqsFile)
    for MFW in AllMFW: 
        FreqData, Identifiers = get_freqdata(Wordfreqs, MFW)
        Labels, Colors, GroundTruth = get_labels_tc(Identifiers, MetadataFile)
        LinkageMatrix = clusteranalysis(FreqData, Method, Metric)
        CorrCoeff, ARI, Homog, Compl, VMeasure = evaluate_cluster(FreqData, 
                                                                  LinkageMatrix, 
                                                                  GroundTruth)
        make_dendrogram_w(LinkageMatrix, GraphFolder, 
                        Method, Metric, 
                        CorrCoeff, Labels, Colors, 
                        DisplayLevels)
    
    print("Done.")










# =================================
# PCA with topics scores per text
# =================================

tp_style = pygal.style.Style(
    background='white',
    plot_background='white',
    font_family = "FreeSans",
    title_font_size = 16,
    legend_font_size = 16,
    label_font_size = 12,
    value_font_size = 8,
    # colors=["#1d91c0","#225ea8","#253494","#081d58", "#071746"],
    colors=["darkred", "darkgreen", "navy", "#333333"]
    )


def get_labels(textids, metadata, category):
        categorylabels = list(metadata.loc[:,category])
        setlabels = sorted(list(set(categorylabels)))
        # print(setlabels)
        categorycolors = ["darkred" if x==setlabels[0] else x for x in categorylabels]
        categorycolors = ["green" if x==setlabels[1] else x for x in categorycolors]
        categorycolors = ["navy" if x==setlabels[2] else x for x in categorycolors]
        # for i in range(0,10):
            # print(categorylabels[i], categorycolors[i])
        authornames = list(metadata.loc[:,"tc_author-short"])
        authornames = [name.title() for name in authornames]
        shorttitles = list(metadata.loc[:,"tc_title-short"])
        shorttitles = [title.title() for title in shorttitles]
        referenceyears = list(metadata.loc[:,"year_reference"])
        #for i in range(0,10):
        #    print(textids[i], authornames[i], shorttitles[i])
        return categorylabels, categorycolors, authornames, shorttitles, referenceyears


def get_topicwords(topicwords_file):
    with open(topicwords_file, "r") as infile:
        topicwords = pd.read_csv(infile, sep="\t", header=None)
        # print(topicwords.head())
        topicwords = list(topicwords.iloc[:,2])
        topicwords = [words.split(" ") for words in topicwords] 
        topicwords = [words[0]+"-"+words[1]+"-"+words[2]+"-"+words[3] for words in topicwords]
        # for i in range(0,5): 
        #     print(topicwords[i])
        return topicwords
    

def apply_pca_t(topicdata): 
    print("--apply_pca_t")
    # z-score transformation
    means = np.mean(topicdata, axis=0)
    stds = np.std(topicdata, axis=0)
    topicdata = (topicdata - means) / stds
    # print(topicdata)
    # PCA itself
    pca = PCA(n_components=60)
    pca.fit(topicdata)
    variance = pca.explained_variance_ratio_
    transformed = pca.transform(topicdata)
    allpcloadings = pca.components_
    # Get cumulated variance for the PCs.
    cumulated_variance = 0
    dimensions_count = 0
    for item in variance: 
        cumulated_variance = item+cumulated_variance
        dimensions_count +=1
        print("{:02d}".format(dimensions_count), "{:3f}".format(cumulated_variance))
    print("variance explained per PC", variance)
    return transformed, variance, allpcloadings


def make_loadingsdata(allpcloadings, topicwords):
    print("topics", len(topicwords))
    print("pcs", len(allpcloadings))
    pc1_loadings = allpcloadings[0]
    pc2_loadings = allpcloadings[1]
    loadingsdata = []
    for i in range(0, len(topicwords)):
        topicloadings = [i, topicwords[i], pc1_loadings[i], pc2_loadings[i]]
        # print(topicloadings)
        loadingsdata.append(topicloadings)
    return loadingsdata
    
   
def make_2dscatterplot_t(transformed, variance, categorylabels,
                         categorycolors, textids, authornames,
                         shorttitles, referenceyears, loadingsdata, graph_folder):
    print("--make_2dscatterplot")
    xtitle = "PC1 (" + '{:01.0f}'.format(variance[0]*100) + "%)"
    ytitle = "PC2 (" + '{:01.0f}'.format(variance[1]*100) + "%)"
    if not os.path.exists(graph_folder):
        os.makedirs(graph_folder)
    plot = pygal.XY(style=tp_style,
                    stroke=False,
                    legend_at_bottom=True,
                    legend_at_bottom_columns = 4,
                    x_title = xtitle,
                    y_title = ytitle,
                    )
    setlabels = sorted(list(set(categorylabels)))
    comedydata = []
    tragedydata = []
    tracomdata = []
    for i in range(0,len(categorylabels)):
        if categorylabels[i] == setlabels[0]:
            textpoint = {"value" : (transformed[i][0], transformed[i][1]),
                         "color" : categorycolors[i],
                         "label" : textids[i]+": "+authornames[i]+", "+shorttitles[i]+" ("+str(referenceyears[i])+")"
                         }
            comedydata.append(textpoint)
        if categorylabels[i] == setlabels[1]:
            textpoint = {"value" : (transformed[i][0], transformed[i][1]),
                         "color" : categorycolors[i],
                         "label" : textids[i]+": "+authornames[i]+", "+shorttitles[i]+" ("+str(referenceyears[i])+")"
                         }
            tracomdata.append(textpoint)
        if categorylabels[i] == setlabels[2]:
            textpoint = {"value" : (transformed[i][0], transformed[i][1]),
                         "color" : categorycolors[i],
                         "label" : textids[i]+": "+authornames[i]+", "+shorttitles[i]+" ("+str(referenceyears[i])+")"
                         }
            tragedydata.append(textpoint)
    plot.add("comedies", comedydata, dots_size=4)
    plot.add("tragicomedies", tracomdata, dots_size=4)
    plot.add("tragedies", tragedydata, dots_size=4)
    # Add loadingsdata
    topicloadings = []
    for i in range(0, len(loadingsdata)):
        topicpoint = {"value" : (loadingsdata[i][2]*1, loadingsdata[i][3]*1),
                      "color" : "#333333",
                      "label" : "topic " + str(loadingsdata[i][0]) + " (" + str(loadingsdata[i][1]) +")",
                      }
        if abs(loadingsdata[i][2]) > 0.2 or abs(loadingsdata[i][3]) > 0.2:
            topicloadings.append(topicpoint)
    plot.add("Loadings", topicloadings, dots_size=2)
    plot.render_to_file(graph_folder+"2d-scatterplot-topicpca_2017-04-03_EN.svg")





def make_loadingsplot(transformed, variance, categorylabels,
                         categorycolors, textids, authornames,
                         shorttitles, referenceyears, loadingsdata, graph_folder):
    print("--make_loadingsplot")
    xtitle = "PC1 (" + '{:01.0f}'.format(variance[0]*100) + "%)"
    ytitle = "PC2 (" + '{:01.0f}'.format(variance[1]*100) + "%)"
    if not os.path.exists(graph_folder):
        os.makedirs(graph_folder)
    plot = pygal.XY(style=tp_style,
                    stroke=False,
                    legend_at_bottom=True,
                    legend_at_bottom_columns = 3,
                    x_title = xtitle,
                    y_title = ytitle,
                    )
    topicloadings = []
    for i in range(0, len(loadingsdata)):
        topicpoint = {"value" : (loadingsdata[i][2], loadingsdata[i][3]),
                      "color" : "grey",
                      "label" : "topic " + str(loadingsdata[i][0]) + " (" + str(loadingsdata[i][1]) +")"
                      }
        topicloadings.append(topicpoint)
    print(topicloadings[0])
    plot.add("Loadings", topicloadings)
    plot.render_to_file(graph_folder+"2d-scatterplot-topicloadings.svg")









def make_boxplot(Transformed, Variance, Colors, pc, GraphFolder):
    print("--make_boxplot")
    if not os.path.exists(GraphFolder):
        os.makedirs(GraphFolder)
    plot = pygal.Box(style=tp_style,
                    legend_at_bottom=True,
                    legend_at_bottom_columns = 3,
                    title = "Verteilungen in PC " + str(pc+1),
                    y_title = "PC" + str(pc+1) + " (" + '{:01.0f}'.format(Variance[pc]*100) + "%)"
                    )
    comedydata = []
    tracomdata = []
    tragedydata = []
    for i in range(0,391):
        if Colors[i] == "darkred":
            Point = {"value" : Transformed[i][pc], "color" : Colors[i]}
            comedydata.append(Point)
        if Colors[i] == "darkgreen":
            Point = {"value" : Transformed[i][pc], "color" : Colors[i]}
            tracomdata.append(Point)
        if Colors[i] == "navy":
            Point = {"value" : Transformed[i][pc], "color" : Colors[i]}
            tragedydata.append(Point)
    plot.add("Comédies", comedydata)
    plot.add("Tragi-comédies", tracomdata)
    plot.add("Tragédies", tragedydata)
    plot.render_to_file(GraphFolder+"boxplot-PC" + str(pc+1) + ".svg")
    



def group_data(Transformed, Colors, pc):
    comedydata = []
    tracomdata = []
    tragedydata = []
    for i in range(0,391):
        if Colors[i] == "darkred":
            Point = Transformed[i][pc]
            comedydata.append(Point)
        if Colors[i] == "darkgreen":
            Point = Transformed[i][pc]
            tracomdata.append(Point)
        if Colors[i] == "navy":
            Point = Transformed[i][pc]
            tragedydata.append(Point)
    #print(comedydata)
    return comedydata, tracomdata, tragedydata



def ranksumtest(comedydata, tracomdata, tragedydata):
    alldata = [comedydata, tracomdata, tragedydata]
    labels = ["comedy", "tragicomedy", "tragedy"]
    combinations = [[0,2], [1,0], [1,2]]
    for combination in combinations:
        mannwhitney =  stats.mannwhitneyu(alldata[combination[0]],
                                          alldata[combination[1]],
                                          alternative="two-sided")
        statistics = [labels[combination[0]],
                      labels[combination[1]],
                      mannwhitney[0],
                      mannwhitney[1]]
        print(statistics)
    

def make_3dscatterplot_t(Transformed, Variance, Colors, GraphFolder):
    if not os.path.exists(GraphFolder):
        os.makedirs(GraphFolder)
    print("--make_3dscatterplot")
    azims = range(120,140,1)
    elevs = range(221,222,1)
    for azim in azims: 
        for elev in elevs:
            print(".")
               
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            allx = []
            ally = []
            allz = []
            for i in range(0,391): 
                # print(i)
                # print(Transformed[i])
                allx.append(Transformed[i][0])
                ally.append(Transformed[i][1])
                allz.append(Transformed[i][2])
            ax.scatter(allx, ally, allz, c=Colors, marker="o", s=10, linewidth=0.3)
            plt.setp(ax.get_xticklabels(), fontsize=5)
            plt.setp(ax.get_yticklabels(), fontsize=5)
            plt.setp(ax.get_zticklabels(), fontsize=5)
            ax.set_xlabel("PC1 "+"{:03.2f}".format(Variance[0]), fontsize=8)
            ax.set_ylabel("PC2 "+"{:03.2f}".format(Variance[1]), fontsize=8)
            ax.set_zlabel("PC3 "+"{:03.2f}".format(Variance[2]), fontsize=8)
        
            ax.azim = azim
            ax.elev = elev
            
            #plt.show()
            fig.savefig(GraphFolder+"forgif-3dscatter_"+"{:03d}".format(azim)+"-"+"{:03d}".format(elev)+".png", dpi=600, figsize=(3,3), bbox_inches="tight", facecolor="white", transparent=True)
            plt.close()
    

### Main function ###
def topicpca(
    mastermatrix_file,
    topicwords_file,
    metadata_file,
    graph_folder): 
    """
    Coordinating function for topicpca.
    Creates a PCA plot based on topic scores per text.
    """
    print("Launched topicpca.")
    mastermatrix = get_mastermatrix(mastermatrix_file)
    topicdata, textids = get_topicdata(mastermatrix)
    metadata = get_metadata(metadata_file)
    categorylabels, categorycolors, authornames, shorttitles, referenceyears = get_labels(textids, metadata, category="tc_subgenre")
    topicwords = get_topicwords(topicwords_file)
    transformed, variance, allpcloadings = apply_pca_t(topicdata)
    loadingsdata = make_loadingsdata(allpcloadings, topicwords)   
    make_2dscatterplot_t(transformed, variance, categorylabels,
                         categorycolors, textids, authornames, shorttitles,
                         referenceyears, loadingsdata, graph_folder)
    #make_loadingsplot(transformed, variance, categorylabels,
    #                     categorycolors, textids, authornames, shorttitles,
    #                     referenceyears, loadingsdata, graph_folder)
    # make_3dscatterplot_t(Transformed, Variance, Colors, GraphFolder)
    #for pc in [0, 1]:
    #    print("now dealing with pc " + str(pc+1))
    #    make_boxplot(Transformed, Variance, Colors, pc, GraphFolder)
    #    comedydata, tracomdata, tragedydata = group_data(Transformed, Colors, pc)
    #    ranksumtest(comedydata, tracomdata, tragedydata)
    print("Done.")
    
    
 
 
 
 
 
 
 
 
 
 
################################
# PCA with word frequencies
################################

wd_style = pygal.style.Style(
    background='white',
    plot_background='white',
    font_family = "FreeSans",
    title_font_size = 20,
    legend_font_size = 16,
    label_font_size = 12,
    colors=["#1d91c0","#225ea8","#253494","#081d58", "#071746"])




def get_colors_w(Identifiers, MetadataFile): 
    with open(MetadataFile, "r") as InFile: 
        Metadata = pd.read_csv(InFile, sep=";")
        Metadata.set_index("idno", inplace=True)
        #print(Metadata.head())
        Colors = []
        for Item in Identifiers:
            Label = Metadata.loc[Item,"tc_subgenre"]
            #print(Item, Label)
            if Label == "Comédie": 
                Colors.append("darkred")
            if Label == "Tragi-comédie":
                Colors.append("darkgreen")
            elif Label == "Tragédie": 
                Colors.append("navy")
        #print(Colors)
        return Colors
   
   

def apply_pca_w(FreqData): 
    pca = PCA(n_components=3)
    pca.fit(FreqData)
    Variance = pca.explained_variance_ratio_
    Transformed = pca.transform(FreqData)
    #print(Transformed)
    #print(Variance)
    return Transformed, Variance
   
   
   
def make_2dscatterplot_w(Transformed, GraphFolder): 
    if not os.path.exists(GraphFolder):
        os.makedirs(GraphFolder)
    plot = pygal.XY(style=wd_style,
                    stroke=False)
    Data = []
    for i in range(0,391): 
        Point = (Transformed[i][0], Transformed[i][1])
        Data.append(Point)
    plot.add("test", Data)
    plot.render_to_file(GraphFolder+"2dscatter.svg")



def make_3dscatterplot_w(Transformed, Variance, Colors, GraphFolder, MFW):
    if not os.path.exists(GraphFolder):
        os.makedirs(GraphFolder)
    azims = range(0,350,10)
    elevs = range(180,350,10)
    for azim in azims: 
        for elev in elevs: 
               
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            allx = []
            ally = []
            allz = []
            for i in range(0,391): 
                allx.append(Transformed[i][0])
                ally.append(Transformed[i][1])
                allz.append(Transformed[i][2])
            ax.scatter(allx, ally, allz, c=Colors, marker="o", s=6, linewidth=0.3)
            plt.setp(ax.get_xticklabels(), fontsize=3)
            plt.setp(ax.get_yticklabels(), fontsize=3)
            plt.setp(ax.get_zticklabels(), fontsize=3)
            ax.set_xlabel("PC1 "+"{:03.2f}".format(Variance[0]), fontsize=4)
            ax.set_ylabel("PC2 "+"{:03.2f}".format(Variance[1]), fontsize=4)
            ax.set_zlabel("PC3 "+"{:03.2f}".format(Variance[2]), fontsize=4)
        
            ax.azim = azim
            ax.elev = elev
            
            #plt.show()
            fig.savefig(GraphFolder+"3dscatter_"+"{:04d}".format(MFW)+"mfw-"+"{:03d}".format(azim)+"-"+"{:03d}".format(elev)+".png", dpi=600, figsize=(3,3), bbox_inches="tight")
            plt.close()
    


### Main function ###

def wordpca(WordfreqsFile,
            MetadataFile,
            GraphFolder,
            AllMFW): 
    """
    Coordinating function.
    """
    print("Launched wordpca.")
    WordFreqs = get_wordfreqs(WordfreqsFile)
    for MFW in AllMFW: 
        FreqData, Identifiers = get_freqdata(WordFreqs, MFW)
        Colors = get_colors_w(Identifiers, MetadataFile)
        Transformed, Variance = apply_pca_w(FreqData)
        #make_2dscatterplot_w(Transformed, GraphFolder)
        make_3dscatterplot_w(Transformed, Variance, Colors, GraphFolder, MFW)
    print("Done.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
