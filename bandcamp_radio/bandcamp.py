import requests
import json


def discover(genre="all", sub_genre="any", slice="best", page=0):
    url = F"https://bandcamp.com/api/discover/3/get_web?g={genre}&t={sub_genre}&s={slice}&p={page}&f=all"
    request = requests.get(url)
    json.loads(request.content)
    print("got", genre, sub_genre, slice)
    return json.loads(request.content)['items']
