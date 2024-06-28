import urllib.request 
from PIL import Image 
import os
import json
from tqdm import tqdm
from io import BytesIO
from urllib.request import Request, urlopen
import requests
import os

# if you are downloading videos, comment out the first line of code and uncomment the second line
media_format = 'image/jpeg'
# media_format = 'video/mp4'

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
            if header != media_format: 
                continue
            # change the jpg extension to mp4 to download videos
            with open(os.path.join(outdir, f'{idx}.jpg'), "wb") as file:
                file.write(response.content)
            idx += 1 
        
