#!/usr/bin/env python3
# Filename: visualize_metadata.py
# Author: #cf, #uh

"""
# Visualize some corpus properties.
"""

import pandas as pd
import matplotlib.pyplot as plt
import pygal
import os

plot_colors = ["#3366CC","#DC3912","#FF9900","#109618","#990099","#3B3EAC","#0099C6","#DD4477","#66AA00","#B82E2E","#316395","#994499","#22AA99","#AAAA11","#6633CC","#E67300","#8B0707","#329262","#5574A6","#3B3EAC"]
        

def describe_corpus(wdir, metadatafile, category):
    """
    Plots corpus properties (default: bar chart, by decade).
    
    Author: cf, uh
    
    Arguments:
    
    wdir (string): current working directory
    metadatafile (string): filename of the metadata CSV file (in wdir)
    category (string): which metadata category to visualize
    
    Example of how to use this function:
        from extract import visualize_metadata        
        visualize_metadata.describe_corpus("/home/ulrike/novelas-hispam", "metadata.csv", "author-country")

    """
    with open(wdir+metadatafile, "r") as infile:
        metadata = pd.DataFrame.from_csv(infile, header=0)
        #print(metadata.head())
        
        ## Preparing data
        cat_xaxis = "decade"
        cat_bars = category 
        labels = sorted(set(metadata[cat_bars]))
        #print(labels)
        metadata = metadata[["idno",cat_xaxis,cat_bars]]
        grouped = metadata.groupby([cat_xaxis,cat_bars]).count()
        unstacked = grouped.unstack()
        unstacked.fillna("0", inplace=True)

        ## Plotting the data    
        """
        # matplotlib    
        myplot = grouped.unstack().plot(kind="bar", stacked=True, title="",figsize=(10, 8), color=plot_colors)
        myplot.set_title("Distribution of novels", fontsize=20)        
        myplot.set_xlabel("Decades", fontsize = 16)
        myplot.set_ylabel("Number",fontsize = 16)
        myplot.legend(labels) ## This is correct only by chance!! -- seems to be solved!
        plt.setp(plt.xticks()[1], rotation=40, fontsize = 14)   
        plt.tight_layout()
        figurename = "dist_by-"+category+".png"
        plt.savefig(wdir+figurename, dpi=300)
        plt.close()
        """
        
        # pygal
        my_style = pygal.style.Style(
		  background='white',
		  plot_background='white',
		  font_family = "FreeSans",
		  opacity = "1",
		  title_font_size = 20,
		  legend_font_size = 18,
		  label_font_size = 16,
		  colors=plot_colors)
          
        bar_chart = pygal.StackedBar(style=my_style, legend_at_bottom=True, print_values=False)
        bar_chart.title = 'Distribution of novels'
        bar_chart.x_title = "Decade"
        bar_chart.y_title = "Number of novels"
        
        md_unstacked = grouped.unstack()
        md_unstacked.fillna(0, inplace=True)
        
        bar_chart.x_labels = [str(i) for i in list(md_unstacked.index)]
        
        for label in labels:
            vals = md_unstacked["idno",label]
            bar_chart.add(label, vals.values)
        
        figurename = os.path.join(wdir, "dist_by-"+category+".svg")
        bar_chart.render_to_file(figurename)
        
        
        print("barchart " + category + " done")
        
        
        
        
def plot_pie(wdir, metadatafile, category):
    """
    Plots corpus properties (pie chart)
    
    Author: uh
    
    Arguments:
    
    wdir (string): current working directory
    metadatafile (string): filename of the metadata CSV file (in wdir)
    category (string): which metadata category to visualize
    
    Example of how to use this function:
        from extract import visualize_metadata        
        visualize_metadata.plot_pie("/home/ulrike/novelas-hispam", "metadata.csv", "subgenre_x")
    """
    with open(wdir+metadatafile, "r") as infile:
        metadata = pd.DataFrame.from_csv(infile, header=0)
                
        #plot_labels = sorted(set(metadata[category]))
        data_grouped = metadata.groupby([category]).count()
        data_unstacked = data_grouped.unstack()
        data_plot = data_unstacked.idno.sort_values()
        
        
        myplot = data_plot.plot(kind="pie", figsize=(7,7), colors=plot_colors, startangle=0, fontsize=9)
        # autopct='%1.f'
        myplot.set_title("Distribution of novels", fontsize=18, y=1.03)
        myplot.set_xlabel(" ",fontsize = 14, y=-1.06)
        myplot.set_ylabel(" ",fontsize = 14, x=-1.20)
        
        
        #myplot.legend(plot_labels)
        
        #plt.axis('equal')
        #plt.tight_layout()
        
        figurename = "piechart-"+category+".png"
        plt.savefig(wdir+figurename, dpi=300)
        plt.close()
        
    print("piechart done")

if __name__ == "__main__":
	describe_corpus(int(sys.argv[1]))
