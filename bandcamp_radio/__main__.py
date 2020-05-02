import vlc
from vlc import State, Meta
import random
from bandcamp_radio import bandcamp
from bandcamp_radio.Getch import Getch
from os import system, name
import argparse

vlc_instance = vlc.Instance("-q")
player = vlc_instance.media_list_player_new()


def control(command):
    switcher = {
        "p": lambda: player.pause(),
        "n": lambda: player.next(),
        "s": lambda: player.stop()
    }
    if command in switcher:
        action = switcher.get(command)
        action()


def print_tape(artist, title, url):
    # hack with a backspace key from
    # https://stackoverflow.com/questions/50379652/python-getch-print-from-separate-thread
    # ascii tape is from https://asciiart.website/index.php?art=objects/audio%20equipment
    print("    ____________________________")
    print('\b'*100+ "  /|............................|")
    print('\b'*100+ " | |:" + '{: ^26}'.format(artist) + ":|")
    print('\b'*100+ " | |:" + '{: ^26}'.format(title) + ":|")
    print('\b'*100+ " | |:     ,-.   _____   ,-.    :|")
    print('\b'*100+ " | |:    ( `)) [_____] ( `))   :|")
    print('\b'*100+ " |v|:     `-`   ' ' '   `-`    :|")
    print('\b'*100+ " |||:     ,______________.     :|")
    print('\b'*100+ " |||...../::::o::::::o::::\.....|")
    print('\b'*100+ " |^|..../:::O::::::::::O:::\....|")
    print('\b'*100+ " |/`---/--------------------`---|")
    print('\b'*100+ " `.___/ /====/ /=//=/ /====/____/")
    print('\b'*100+ "      `--------------------'")
    print('\b'*100+ "Support", artist, "on", url)
    print('\b'*100+ "[p]ause, [n]ext and [s]top")


def MediaChanged(event):
    artist = player.get_media_player().get_media().get_meta(Meta.Artist)
    title = player.get_media_player().get_media().get_meta(Meta.Title)
    url = player.get_media_player().get_media().get_meta(Meta.URL)
    clear()
    print_tape(artist, title, url)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    parser = argparse.ArgumentParser("Make your own mix tape. Always support bands that you like!")
    parser.add_argument('-g', '--genre', action='append', nargs='*',
                        metavar=('genre', 'sub_genre'),
                        help='genre followed by space separated sub-genre(s). all if not supplied'
                        )
    parser.add_argument('-s', '--slice', nargs='*', dest='slice',
                        help='slice type separated by space. possible values are: new best rec. best if not supplied',
                        default=["best"])
    args = parser.parse_args()
    genres = args.genre
    if genres is None:
        genres = [["all"]]
    tracks = []
    for genre in genres:
        sub_genres = genre[1:]
        if not sub_genres:
            sub_genres.append("any")
        for sub_genre in sub_genres:
            for slice in args.slice:
                tracks = tracks + bandcamp.discover(genre[0], sub_genre, slice)
    playlist = vlc_instance.media_list_new()
    random.shuffle(tracks)
    for item in tracks:
        mp3 = item['featured_track']['file']['mp3-128']
        media = vlc_instance.media_new(mp3)
        url = "https://" + item['url_hints']["subdomain"] + ".bandcamp.com"
        media.set_meta(Meta.Artist, item["secondary_text"])
        media.set_meta(Meta.Title, item["featured_track"]["title"])
        media.set_meta(Meta.URL, url)
        playlist.add_media(media)

    events = player.get_media_player().event_manager()
    print(events.event_attach(vlc.EventType.MediaPlayerMediaChanged, MediaChanged))
    player.set_media_list(playlist)
    player.play()
    getch = Getch()
    while player.get_state().value != State.Stopped:
        command = getch.impl()
        control(command)


if __name__ == '__main__':
    main()
