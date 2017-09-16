#!/usr/bin/env python3

from TwitterAPI import TwitterAPI
from datetime import date, timedelta
import json

f = open('data/authentication.json', 'r')
data = json.load(f)
consumer = data['consumer']
access_token = data['access_token']
f.close()

f = open('data/streets.json', 'r')
streets = json.load(f)
f.close()

api = TwitterAPI( consumer['key'],
                  consumer['secret'],
                  access_token['key'],
                  access_token['secret'])

today = date.today()
delta = timedelta(days=7)
weeks = 1
days = [today]
info = []

for i in range(weeks):
    days.append(days[-1] - delta)

for day in days:
    r = api.request('search/tweets', {
            'q': '"la cisterna" "sin luz"',
            'until': day})

    for item in r.get_iterator():
        street_list = []

        for street in streets:
            index = item['text'].upper().find(street)
            if index > -1:
                street_list.append(street)

        if len(street_list) > 0:
            info.append(dict(
                datetime = item['created_at'],
                streets  = street_list
            ))

        # print('->', item['user']['screen_name'], item['created_at'])
        # print('   "' + item['text'] + '"')

print(info)
