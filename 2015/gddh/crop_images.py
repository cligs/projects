#!/usr/bin/env python3
# Filename: crop_images.py

"""
# Function to crop images using Pillow.
"""

import glob
from PIL import Image

def crop_image(file): 
    myimage = Image.open(file)
    #myimage.show()
    print(myimage.size)
    box = (370,350,3570,2150) # sides: left,top,right,bottom
    cropped = myimage.crop(box)
    outfile = file[:-4] + "-c.jpg"
    cropped.save(outfile, "JPEG")


def main(inputpath):
    for file in glob.glob(inputpath):
        crop_image(file)

main("./8_visuals/wordlesXXX/*.jpg")

