import urllib.request
from PIL import Image
import os
import json
import csv
import time
import requests
from tqdm import tqdm
from io import BytesIO
from urllib.request import Request, urlopen

dirname = "download"
os.makedirs(dirname, exist_ok=True)

idx = 0
with open("links.jsonl", "r") as file:
    for link in tqdm(file):
        link = link.strip('"')
        try:
            response = requests.get(link)
            header = response.headers.get("Content-Type", "")
            type = header.split("/")[0]
            extension = header.split("/")[1]
            if type != "image":
                continue
            with open(os.path.join(dirname, f"{idx}.{extension}"), "wb") as file:
                file.write(response.content)
        except:
            print('error with url request, skipping this!')
        idx += 1
