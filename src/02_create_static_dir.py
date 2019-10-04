import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import json
import urllib.request
import os
from PIL import Image
import glob

import yaml

files = glob.glob("data/input_tmp/sanjo/*.jpg")

f = open('bash_dir.sh', 'w')
writer = csv.writer(f, lineterminator='\n')

for input_file_path in files:

    filename = input_file_path.split("/")[-1]

    odir = input_file_path.replace("data/input_tmp", "").replace("/"+filename, "")

    line = "python iiif_static/iiif_static.py  -d ../docs"+odir+" -t 200  -p https://nakamura196.github.io/iiif_image_repo"+odir+" "+input_file_path


    writer.writerow([line])

f.close()
