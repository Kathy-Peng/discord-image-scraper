from tqdm import tqdm
from io import BytesIO
from urllib.request import Request, urlopen
import jsonlines

new_data_dir = 'data_dir'
os.makedirs(new_data_dir, exist_ok=True)

with jsonlines.open('links.jsonl', 'r') as linkfile:
    idx = 0
    for link in tqdm(linkfile.iter()):
        try:
            req = Request(link, headers={'User-Agent': 'Mozilla/5.0'}) 
            image = urlopen(req).read()
            image = Image.open(BytesIO(image))
            image = image.resize((1024, 1024))
            image.save(os.path.join(new_data_dir, str(idx))+'.jpeg')
        except :
            print(f'error downloading image {idx}, skipping this one!!')
        idx += 1
            
