#!/usr/bin/env python3

from TwitterAPI import TwitterAPI
from datetime import date, timedelta
import json

f = open('data/authentication.json', 'r')
data = json.load(f)
consumer = data['consumer']
access_token = data['access_token']
f.close()

api = TwitterAPI( consumer['key'],
                  consumer['secret'],
                  access_token['key'],
                  access_token['secret'])

today = date.today()
delta = timedelta(days=7)
weeks = 1
days = [today]

for i in range(weeks):
    days.append(days[-1] - delta)

for day in days:
    r = api.request('search/tweets', {
            'q': '"la cisterna" "sin luz"',
            'until': day})

    for item in r.get_iterator():
        print('->', item['user']['screen_name'], item['created_at'])
        print('   "' + item['text'] + '"')
