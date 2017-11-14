#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import json

host = 'http://toutiao-ali.juheapi.com/toutiao/index'
url = host + '?' + 'type=top'
headers = {
    'Authorization' : 'APPCODE ' + '7cba67b47a074d7984f3fc89cec3ab2d'
}
req = request.Request(url=url, headers=headers, method='GET')
response = request.urlopen(req)
content = response.read().decode('utf-8')
json = json.loads(content)
print(json.keys)
cc = json['result']['data']
print(cc)
for result in cc:
    print(result)