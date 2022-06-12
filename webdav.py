import os
import yaml
import time
import requests
from webdav4.client import Client

# Get Environment Variables
WEBDAVURL = os.getenv('WEBDAVURL')
WEBDAV_USER = os.getenv('WEBDAV_USER')
WEBDAV_ACCESS = os.getenv('WEBDAV_ACCESS')
CLASHURL = os.getenv('CLASHURL')
if WEBDAV_ACCESS == None:
    raise Exception('WEBDAV_ACCESS variable is None')
if WEBDAV_USER == None:
    raise Exception('WEBDAV_USER variable is None')
if WEBDAV_ACCESS == None:
    raise Exception('WEBDAV_ACCESS variable is None')
if CLASHURL == None:
    raise Exception('CLASHURL variable is None')

now_str_time = time.asctime( time.localtime(time.time()) )
new_proxy_group = {
    "name":"亚洲负载均衡",
    "type":"url-test",
    "interval":600,
    "url":"http://www.gstatic.com/generate_204",
    "proxies":["🇭🇰 香港","🇹🇼 台湾","🇸🇬 新加坡"]
}

ans = requests.get(CLASHURL)
with open("clash.yml",'w+') as f:
    f.write(ans.text)

client = Client(base_url=WEBDAVURL,
                auth=(WEBDAV_USER, WEBDAV_ACCESS))

with open("clash.yml",'r+') as f:
    yml_data = f.read()
    json_data = yaml.load(yml_data,Loader=yaml.FullLoader)
json_data['proxy-groups'][0]['proxies'].insert(0,new_proxy_group['name'])
json_data['proxy-groups'].insert(-1,new_proxy_group)
json_data['updateTime'] = now_str_time
with open('newclash.yml','w+') as f:
    yaml.safe_dump(json_data,f,default_flow_style=False)

client.upload_file(from_path='newclash.yml', to_path='/clashbuild/newclash.yaml', overwrite=True)