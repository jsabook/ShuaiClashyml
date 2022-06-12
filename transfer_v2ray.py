import os
import yaml
import time
import requests
from webdav4.client import Client
# Get Environment Variables
WEBDAVURL = os.getenv('WEBDAVURL')
WEBDAV_USER = os.getenv('WEBDAV_USER')
WEBDAV_ACCESS = os.getenv('WEBDAV_ACCESS')
V2RAYURL = os.getenv('V2RAYURL')
if WEBDAV_ACCESS == None:
    raise Exception('WEBDAV_ACCESS variable is None')
if WEBDAV_USER == None:
    raise Exception('WEBDAV_USER variable is None')
if WEBDAV_ACCESS == None:
    raise Exception('WEBDAV_ACCESS variable is None')
if V2RAYURL == None:
    raise Exception('V2RAYURL variable is None')

ans = requests.get(V2RAYURL)
with open("v2ray.txt",'w+') as f:
    f.write(ans.text)

client = Client(base_url=WEBDAVURL,
                auth=(WEBDAV_USER, WEBDAV_ACCESS))


client.upload_file(from_path='v2ray.txt', to_path='/clashbuild/v2ray.txt', overwrite=True)