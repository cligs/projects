DH 2017: project documentation "Genre on time"
==============================================

This is accompanying material for the proposal "Genre on time: determining time-based features for historical and non-historical 19th century Romance novels", authored by Ulrike Henny, José Calvo and Katrin Betz and submitted for the 2017 DH conference in Montreal.


## Python scripts:

### Links
The following python modules available in the CLiGS toolbox have been used for data description, annotation, analysis and visualization:

For data description:
* https://github.com/cligs/toolbox/blob/master/extract/get_metadata.py
* https://github.com/cligs/toolbox/blob/master/extract/visualize_metadata.py

For data annotation:
* https://github.com/cligs/toolbox/blob/master/annotate/workflow_teihdt.py
* https://github.com/cligs/toolbox/blob/master/annotate/prepare_tei.py
* https://github.com/cligs/toolbox/blob/master/annotate/use_heideltime.py

For data analysis and visualization:
* https://github.com/cligs/toolbox/blob/master/analyse/genre_on_time.py

Copies of these files are included here to reflect the state of the scripts at submission time.

### Files
* scripts/get_metadata.py
* scripts/visualize_metadata.py
* scripts/workflow_teihdt.py
* scripts/prepare_tei.py
* scripts/use_heideltime.py

## Research data results:
* data/corpus-description.csv
* data/corpus-metadata.csv
* data/tpx-feature-doc.csv: documentation of temporal expression features
* data/tpx-corpus-counts.csv: feature counts
* [data/tpx-test-statistics.csv](data/tpx-test-statistics.csv): feature evaluation

## Visualizations:
* visuals/corpus-description: contains charts for corpus summarization
* visuals/tpx: contains charts with temporal feature analysis results
