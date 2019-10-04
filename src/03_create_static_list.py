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

import requests
import shutil

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

dir = "data/input_tmp/sanjo"

file = dir+"/list.csv"

f = open('bash_list.sh', 'w')
writer = csv.writer(f, lineterminator='\n')

with open(file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:
        url = row[0]
        filename = url.split("/")[-1]

        input_file_path = dir+"/"+filename

        download_img(url, input_file_path)

        odir = input_file_path.replace("data/input_tmp", "").replace("/"+filename, "")

        line = "python iiif_static/iiif_static.py  -d ../docs"+odir+" -t 200  -p https://nakamura196.github.io/iiif_image_repo"+odir+" "+input_file_path

        writer.writerow([line])

f.close()
