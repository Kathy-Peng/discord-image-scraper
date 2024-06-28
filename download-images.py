import urllib.request 
from PIL import Image 
import os
import json
from tqdm import tqdm
from io import BytesIO
from urllib.request import Request, urlopen
import requests
import os


outdir = './downloaded-images'
os.makedirs(outdir, exist_ok=True)

idx = 0
with open('sd3.jsonl', 'r') as linkfile:
    for link in linkfile:
        image_urls = link.split('"')
        for image_url in image_urls:
            if image_url == '' or image_url =='\n':
                continue
            print(image_url)
            response = requests.get(image_url)
            header = response.headers.get("Content-Type", "")
            if header != 'image/jpeg': 
                continue
            # change the jpg extension to mp4 to download videos
            with open(os.path.join(outdir, f'{idx}.jpg'), "wb") as file:
                file.write(response.content)
            idx += 1 
        
