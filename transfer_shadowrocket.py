import os
import yaml
import time
import requests
from webdav4.client import Client

# Get Environment Variables
WEBDAVURL = os.getenv('WEBDAVURL')
WEBDAV_USER = os.getenv('WEBDAV_USER')
WEBDAV_ACCESS = os.getenv('WEBDAV_ACCESS')
SHADOW_URL = os.getenv('SHADOW_URL')
if WEBDAV_ACCESS == None:
    raise Exception('WEBDAV_ACCESS variable is None')
if WEBDAV_USER == None:
    raise Exception('WEBDAV_USER variable is None')
if WEBDAV_ACCESS == None:
    raise Exception('WEBDAV_ACCESS variable is None')
if SHADOW_URL == None:
    raise Exception('SHADOW_URL variable is None')

ans = requests.get(SHADOW_URL)
with open("shadowrocket.txt",'w+') as f:
    f.write(ans.text)

client = Client(base_url=WEBDAVURL,
                auth=(WEBDAV_USER, WEBDAV_ACCESS))

client.upload_file(from_path='shadowrocket.txt', to_path='/clashbuild/shadowrocket.txt', overwrite=True)