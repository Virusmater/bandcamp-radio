import requests
import json
from html.parser import HTMLParser
import time


class _FanIdParser(HTMLParser):
    def error(self, message):
        pass

    fan_id = ""

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "data-blob":
                data_html = attr[1]
                data = json.loads(data_html)
                self.fan_id = data['fan_data']['fan_id']


def discover(genre="all", sub_genre="any", slice="best", page=0):
    url = F"https://bandcamp.com/api/discover/3/get_web?g={genre}&t={sub_genre}&s={slice}&p={page}&f=all"
    request = requests.get(url)
    json.loads(request.content)
    print("got", genre, sub_genre, slice)
    return json.loads(request.content)['items']


def get_fan_id(name):
    url = F"https://bandcamp.com/{name}"
    request = requests.get(url)
    parser = _FanIdParser()
    content = request.content
    parser.feed(content.decode('utf-8'))
    return parser.fan_id


def get_collection(fan_id, count=1000):
    url = "https://bandcamp.com/api/fancollection/1/collection_items"
    token = get_token()
    body = F'{{"fan_id": "{fan_id}", "older_than_token": "{token}", "count":"{count}"}}'
    x = requests.post(url, data=body)
    return json.loads(x.text)['items']


def get_token():
    return str(int(time.time())) + "::FOO::"