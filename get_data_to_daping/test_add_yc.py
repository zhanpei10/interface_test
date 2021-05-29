import requests
import json

url = 'http://10.111.32.82:10620/gms/device-data/access'

data = {

}
print(json.loads(data))

for i in range(0, 3):
    res = requests.post(url=url, json=data)
    print(res.text)
