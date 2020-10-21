import json 
import re
import urllib.request
from pytube import YouTube

api_key = "AIzaSyCoZlLHcolOq_Opi2_BGI0gekU27mEfzZk"

url = "https://www.youtube.com/watch?v=ZkYOvViSx3E&list=PL5tcWHG-UPH1fnJw-BvBiiiPUPm1LUKsm&index=22"
json_url = urllib.request.urlopen(url)
data = json.loads(json_url.read())
print(data)