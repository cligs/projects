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
    colors=["navy", "green"]*3,
    )


# ==============================
# Parameter definitions
# ==============================


alldata_file = "metadata+results.csv"
plot_file = "sentlen-romans_101+252.svg"


# ==============================
# Functions
# ==============================


def read_data(alldata_file):
    with open(alldata_file,"r") as infile:
        alldata = pd.DataFrame.from_csv(infile)
        #print(alldata.head(5))
        return alldata

def make_datedata(alldata):
    groupeddata = alldata.groupby("romans-corpus")
    #for name,group in groupeddata:
    #    print(name)
    simenon_data = groupeddata.get_group("simenon")
    contemps_data = groupeddata.get_group("contemporains")
    contemps_data = contemps_data[(contemps_data["pub-year"] > 1919) & (contemps_data["pub-year"] < 1983)]
    print("number of contemps", len(contemps_data))
    print("number of Simenon", len(simenon_data))
    return simenon_data, contemps_data
    

def create_scatterplot(simenon_data, contemps_data, plot_file): 
    plot = pygal.XY(
        range = (5,105),
        xrange=(1919, 1984),
        title="Satzlängen (101 + 252 Romane)",
        x_title="Entstehungsjahr",
        y_title="Mittlere Satzlänge in Worten (log)",
        x_label_rotation=300,
        show_x_guides=True,
        show_y_guides=True,
        stroke=False,   
        show_legend = True,
        legend_at_bottom=True,
        legend_at_bottom_columns=2,
        legend_font_size=12,
        logarithmic=True,
        style=mystyle)
    simenon_points = []
    contemps_points = []
    for i in range(0,len(simenon_data)-1):
        point = {"value" : (simenon_data["pub-year"][i], simenon_data["mean"][i]),
                  "label" : simenon_data["author"][i] + ", " + simenon_data["title"][i]}
        simenon_points.append(point)
    for i in range(0,len(contemps_data)-1):
        point = {"value" : (contemps_data["pub-year"][i], contemps_data["mean"][i]),
                  "label" : contemps_data["author"][i] + ", " + contemps_data["title"][i]}
        contemps_points.append(point)
    plot.add("Zeitgen. (252)", contemps_points, dots_size=4)
    plot.add("Simenon (101)", simenon_points, dots_size=4)
    # Add averages for the two groups
    mean_contemps = np.mean(contemps_data["mean"])
    median_contemps = np.median(contemps_data["mean"])
    mean_simenon = np.mean(simenon_data["mean"])
    median_simenon = np.median(simenon_data["mean"])
    plot.add("median: " + '{:03.1f}'.format(median_contemps), [{"value" : (1921, median_contemps), "label" : "mean"},
                              {"value" : (1982, median_contemps), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("median: "+ '{:03.1f}'.format(median_simenon), [{"value" : (1931, median_simenon), "label" : "mean"},
                              {"value" : (1972, median_simenon), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("mean: " + '{:03.1f}'.format(mean_contemps), [{"value" : (1921, mean_contemps), "label" : "mean"},
                              {"value" : (1982, mean_contemps), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.add("mean: "+ '{:03.1f}'.format(mean_simenon), [{"value" : (1931, mean_simenon), "label" : "mean"},
                              {"value" : (1972, mean_simenon), "label" : "mean"}],
                              stroke=True, stroke_style={'width': 3, 'dasharray': '6, 4', 'linecap': 'round', 'linejoin': 'round'}, dots_size=2)
    plot.render_to_file(plot_file)


def calculate_significance(simenon_data, contemps_data):
    # Get the mean distributions for the three groups of data
    simenon_means = simenon_data["mean"]
    contemps_means = contemps_data["mean"]
    # Perform the Welch's t-test on the combinations
    welch = stats.ttest_ind(simenon_means, contemps_means, axis=0, equal_var=False)
    print("welch (maigret vs. romans)", welch[0], '{:03.6f}'.format(welch[1]))
    # Perform Mann-Whitney's U rank sum test on the data
    mannwhitney = stats.mannwhitneyu(simenon_means, contemps_means, use_continuity=True, alternative="two-sided")
    print("mannwhitneyu (maigret vs. romans)", mannwhitney[0], '{:03.6f}'.format(mannwhitney[1]))



# ==============================
# Coordination function
# ==============================


def make_scatterplot(alldata_file, plot_file):
    alldata = read_data(alldata_file)
    simenon_data, contemps_data = make_datedata(alldata)
    create_scatterplot(simenon_data, contemps_data, plot_file)
    significance = calculate_significance(simenon_data, contemps_data)
    
make_scatterplot(alldata_file, plot_file)






























