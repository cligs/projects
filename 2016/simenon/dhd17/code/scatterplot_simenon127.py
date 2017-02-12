#!/usr/bin/env python3
# Filename: sentencelength.py

"""
# Function to visualize sentence length statistics as a scatterplot.
"""

import re
import glob
import os
import pandas as pd
import numpy as np
import pygal
import scipy.stats as stats


mystyle = pygal.style.Style(
    # general
    background='white',
    plot_background='white',
    font_family="FreeSans",
    # title
    title_font_size=16,
    tooltip_font_size=12,
    opacity_hover=0.2,
    # labels
    print_labels = True,
    label_colors = "darkblue",
    label_font_size=14,
    major_label_font_size=14,
    # values
    print_values = True,
    dynamic_print_values=False,
    value_colors = "darkblue",
    value_font_size=14,
    major_value_font_size=14,
    colors=["navy", "green", "darkred"]*3,
    )


# ==============================
# Parameter definitions
# ==============================


alldata_file = "metadata+results.csv"
plot_file = "sentlen-simenon_127.svg"


# ==============================
# Functions
# ==============================


def read_data(alldata_file):
    with open(alldata_file,"r") as infile:
        alldata = pd.DataFrame.from_csv(infile)
        #print(alldata.head(6))
        return alldata

def make_datedata(alldata):
    #print(alldata)
    groupeddata = alldata.groupby("simenon3")
    #for name,group in groupeddata:
    #    print(name)
    maigret_data = groupeddata.get_group("maigr")
    romans_data = groupeddata.get_group("romans")
    autobio_data = groupeddata.get_group("autob")
    return maigret_data, romans_data, autobio_data
    

def create_scatterplot(maigret_data, romans_data, autobio_data, plot_file): 
    plot = pygal.XY(
        range = (8,24),
        xrange=(1930, 1981),
        title="Satzlängen (127 x Simenon)",
        x_title="Entstehungsjahr",
        y_title="Mittlere Satzlänge in Worten",
        x_label_rotation=300,
        show_x_guides=True,
        show_y_guides=True,
        stroke=False,   
        show_legend = True,
        legend_at_bottom=True,
        legend_at_bottom_columns=3,
        legend_font_size=12,
        style=mystyle)
    maigret_points = []
    romans_points = []
    autobio_points = []
    for i in range(0,len(maigret_data)):
        point = {"value" : (maigret_data["pub-year"][i], maigret_data["mean"][i]),
                  "label" : maigret_data["title"][i]}
        maigret_points.append(point)
    for i in range(0,len(romans_data)):
        point = {"value" : (romans_data["pub-year"][i], romans_data["mean"][i]),
                  "label" : romans_data["title"][i]}
        romans_points.append(point)
    for i in range(0,len(autobio_data)):
        point = {"value" : (autobio_data["pub-year"][i], autobio_data["mean"][i]),
                  "label" : autobio_data["title"][i]}
        autobio_points.append(point)
    plot.add("Maigret-Romane", maigret_points, dots_size=5)
    plot.add("Psychol. Romane", romans_points, dots_size=5)
    plot.add("Autobiographien", autobio_points, dots_size=5)
    mean_maigret = np.mean(maigret_data["mean"])
    mean_romans = np.mean(romans_data["mean"])
    mean_autobio = np.mean(autobio_data["mean"])
    median_maigret = np.median(maigret_data["mean"])
    median_romans = np.median(romans_data["mean"])
    median_autobio = np.median(autobio_data["mean"])
    plot.add("mean: " + '{:03.1f}'.format(mean_maigret), [{"value" : (1930, mean_maigret), "label" : "mean"},
                              {"value" : (1981, mean_maigret), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("mean: " + '{:03.1f}'.format(mean_romans), [{"value" : (1930, mean_romans), "label" : "mean"},
                              {"value" : (1981, mean_romans), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("mean: " + '{:03.1f}'.format(mean_autobio), [{"value" : (1930, mean_autobio), "label" : "mean"},
                             {"value" : (1981, mean_autobio), "label" : "mean"}],
                             stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("median: " + '{:03.1f}'.format(median_maigret), [{"value" : (1930, median_maigret), "label" : "median"},
                              {"value" : (1981, median_maigret), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("median: " + '{:03.1f}'.format(median_romans), [{"value" : (1930, median_romans), "label" : "median"},
                              {"value" : (1981, median_romans), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("median: " + '{:03.1f}'.format(median_autobio), [{"value" : (1930, median_autobio), "label" : "median"},
                             {"value" : (1981, median_autobio), "label" : "mean"}],
                             stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.render_to_file(plot_file)


def calculate_significance(maigret_data, romans_data, autobio_data):
    # Get the mean distributions for the three groups of data
    maigret_means = maigret_data["mean"]
    romans_means = romans_data["mean"]
    autobio_means = autobio_data["mean"]
    # Perform the Welch's t-test on the combinations
    welch = stats.ttest_ind(maigret_means, romans_means, axis=0, equal_var=False)
    print("welch (maigret vs. romans)", welch[0], welch[1])
    welch = stats.ttest_ind(maigret_means, autobio_means, axis=0, equal_var=False)
    print("welch (maigret vs. autobio)", welch[0], welch[1])
    welch = stats.ttest_ind(romans_means, autobio_means, axis=0, equal_var=False)
    print("welch (romans vs. autobio)", welch[0], welch[1])
    # Perform Mann-Whitney's U rank sum test on the data
    mannwhitney = stats.mannwhitneyu(maigret_means, romans_means, use_continuity=True, alternative="two-sided")
    print("mannwhitneyu (maigret vs. romans)", mannwhitney[0], mannwhitney[1])
    mannwhitney = stats.mannwhitneyu(maigret_means, autobio_means, use_continuity=True, alternative="two-sided")
    print("mannwhitneyu (maigret vs. autobio)", mannwhitney[0], mannwhitney[1])
    mannwhitney = stats.mannwhitneyu(romans_means, autobio_means, use_continuity=True, alternative="two-sided")
    print("mannwhitneyu (romans vs. autobio)", mannwhitney[0], mannwhitney[1])
    




# ==============================
# Coordination function
# ==============================


def make_scatterplot(alldata_file, plot_file):
    alldata = read_data(alldata_file)
    maigret_data, romans_data, autobio_data = make_datedata(alldata)
    create_scatterplot(maigret_data, romans_data, autobio_data, plot_file)
    significance = calculate_significance(maigret_data, romans_data, autobio_data)
    
make_scatterplot(alldata_file, plot_file)






























