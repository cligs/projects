#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Annotation Workflow

- converts TEI master files to annotated TEI files
- annotation with heideltime

The final results are stored in a folder "teia".
Run this file directly.


@author: Ulrike Henny
@filename: workflow_teihdt.py 

"""

############ Options ##############

# where the TEI master files are
infolder = "/home/ulrike/Dokumente/Konferenzen/DH/2017/corpora/special"

# where the annotation working files and results should go
outfolder = "/home/ulrike/Dokumente/Konferenzen/DH/2017/corpora/hdt"

# language of the texts (tested for: FRENCH, SPANISH, ITALIAN, PORTUGUESE)
lang = "ITALIAN"

# path to heideltime installation
heideltimePath = "/home/ulrike/Programme/heideltime-standalone-2.1"


import sys
import os

# use the following to add the toolbox to syspath (if needed):
sys.path.append(os.path.abspath("/home/ulrike/Git/"))

from toolbox.annotate import prepare_tei
from toolbox.annotate import use_heideltime


# by default, it should be enough to change the options above and leave this as is

#prepare_tei.prepare("split", infolder, outfolder)
#use_heideltime.apply_ht(heideltimePath, os.path.join(outfolder, "txt"), os.path.join(outfolder, "hdt"), lang)
#use_heideltime.wrap_body("/home/ulrike/Dokumente/Konferenzen/DH/2017/corpora/hdt/hdt", "/home/ulrike/Dokumente/Konferenzen/DH/2017/corpora/hdt/anno")
#prepare_tei.prepare("merge-hdt", outfolder, os.path.join(outfolder, "teia"))
