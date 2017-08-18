#!/usr/bin/env python3

from TwitterAPI import TwitterAPI
import json

f = open('data/authentication.json', 'r')
data = json.load(f)
consumer = data['consumer']
access_token = data['access_token']

api = TwitterAPI( consumer['key'],
                  consumer['secret'],
                  access_token['key'],
                  access_token['secret'])

r = api.request('search/tweets', {'q': 'cisterna iluminacion'})

for item in r.get_iterator():
    print('User:', item['user']['screen_name'])
    print(' ->', item['text'])
