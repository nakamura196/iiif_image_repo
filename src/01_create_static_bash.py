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

config_path = "/Users/nakamura/git/min_a/lda/src/data/config.yml"
f = open(config_path, "r+")
config = yaml.load(f)

doc_dir = config["doc_dir"]
src_dir = config["src_dir"]

prefix = config["prefix"]


f = open(src_dir+'/tmp/convert.sh', 'w')
writer = csv.writer(f, lineterminator='\n')


files = glob.glob(
    doc_dir+'/data/image/original/**/*.jpg', recursive=True)
for file in files:

    base_dir_pair = os.path.split(file)
    odir = base_dir_pair[0].replace("/original/", "/tile/")

    line = "python "+src_dir+"/iiif_static/iiif_static.py  -d "+odir+" -t 200  -p "+odir.replace(doc_dir, prefix)+" "+file

    
    writer.writerow([line])

f.close()
