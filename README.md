# discord-image-scraper
A javascript scraper that scraped images/videos from discord channels
you can control the number of messages to scrape and it is also streaming the scraping process so that you can a channel with a large number of links (larger than the buffer size of javascrpt lanauge)

# Scraping Images from Discord Channels

## step 1: Environment Setup
Make sure nodes and npm are installed! I recommend using nvm (node version manager) as we need a specific version of node. See nvm official post for install instructions.


After installing node (requires version 10+, I recommand 14) and npm, glone this repo to your local repo.

run ```npm install```, this will install all the packages inside package.json and create a node_modules folder.

## step 2: fill out settings.json
In settings.json, only fill out the first two entries 'token' and 'channel_id" and ignore the other two

To get your user token, follow these steps:
1. open up discord channel webpage
2. open web inspector (you need to enable developer mode if using safari)
3. go to network, sort by type and find the messages packet from the left column, click on headers and you should see 'Authorization' on the right within request body, copy that auth token

To get channel id, first enable developer mode in discord (only able to see channel id with developer mode on), paste it in setting.json

## step 3: Scrape the Channel!!
```
touch links.jsonl
sudo chmod o+r links.jsonl
node scrape.js
```
The urls links for images will be stored in links.jsonl as jsonlines (for more info about the format, visit (https://jsonlines.org)

## step 4: Converting url links to local images
NOTE: please inspect download-images.py and change the filepath where you want to store all the jpeg images locally
```
pip install pillow
pip install urllib3
python download-images.py 
```
