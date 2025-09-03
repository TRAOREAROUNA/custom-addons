import json
import random
import urllib.request
from os.path import commonpath

url = 'http://localhost:8069'
username ='admin'
password ='odoo'
db = 'ero'

def json_rpc(url,method,params):
    data = {
        "jsonrpc":"2.0",
        "method":method,
        "params":params,
        "id":random.randint(0,1000000000),

    }

    headers = {
        "content-type": "application/json",
    }

    req = urllib.request.Request(url=url,data=json.dumps(data).encode(), headers=headers)
    response = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if response.get('error'):
        raise Exception(response['error'])
    return response["result"]

def call(url,service,method,*args):
    return json_rpc(f"{url}/jsonrpc","call",{"service":service,"method":method,"args":args})
user_id= call(url,"common","login",db,username,password)

print(user_id)

vals = {
    "name": "property from JSON",
    "sales_id": 2
}
#
# create_property = call(url,"object","execute",db,user_id,password,'estate.property','create',vals)
# print(create_property)

read_property = call(url,"object","execute",db,user_id,password,'estate.property','read',[9])
print(read_property)