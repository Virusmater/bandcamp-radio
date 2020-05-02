# bandcamp-radio
Make your own mix tape. I cannot stress it enough: Always support bands you like!
# usage
```bash
bandcamp-radio -h
usage: Make your own mix tape. Always support bands that you like! [-h] [-g [genre [sub_genre ...]]] [-s [SLICE [SLICE ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -g [genre [sub_genre ...]], --genre [genre [sub_genre ...]]
                        genre followed by space separated sub-genre(s). all if not supplied
  -s [SLICE [SLICE ...]], --slice [SLICE [SLICE ...]]
                        slice type separated by space. possible values are: new best rec. best if not supplied
```
# requirements
Tested only under GNU/Linux (Ubuntu 20.04) in my case
Python 3.8
VLC should be installed
# example
```bash
$: bandcamp-radio -g punk garage crust-punk trash -g metal black-metal -s new best
    ____________________________
  /|............................|
 | |:      Knife Massage       :|
 | |:     Words Are Knives     :|
 | |:     ,-.   _____   ,-.    :|
 | |:    ( `)) [_____] ( `))   :|
 |v|:     `-`   ' ' '   `-`    :|
 |||:     ,______________.     :|
 |||...../::::o::::::o::::\.....|
 |^|..../:::O::::::::::O:::\....|
 |/`---/--------------------`---|
 `.___/ /====/ /=//=/ /====/____/
      `--------------------'
Support Knife Massage on https://bellybuttonrecords.bandcamp.com
[p]ause, [n]ext and [s]top
