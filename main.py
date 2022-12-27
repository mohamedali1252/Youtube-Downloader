from pytube import YouTube
# from pytube.cli import on_progress
from pytube import Playlist
import pathlib

file_size = 0


# from art import *
# tprint("developed by mohamed ali")

# link = "https://www.youtube.com/playlist?list=PL0nX4ZoMtjYEMS2ZQ3jlEzpKPiKPxB154"


def get_url_from_video(url):
    playlist_url = "https://www.youtube.com/playlist?list="
    url_before = url.split("&list=")
    playlist = url_before[1].split("&")
    url_after = playlist_url + playlist
    return url_after


def get_playlist_urls(playlist_url):
    urls = []
    playlist_urls = Playlist(playlist_url)
    for url in playlist_urls:
        urls.append(url)
    return urls


def getting_path():
    path = input("Enter the Full path to output video: ")
    if path is None:
        path = pathlib.Path(__file__).parent.resolve()
    return path


def get_resolution_for_video(link):
    yt = YouTube(link)
    resolutions = [int(i.split("p")[0]) for i in
                   (list(dict.fromkeys([i.resolution for i in yt.streams if i.resolution])))]
    resolutions.sort()
    print("available resolutions is: ", resolutions)

    resolution = input("Enter the resolution: ")
    print(resolution + "p")
    return resolution, resolutions


def download_video(link, resolution, resolutions, path):
    yt = YouTube(link)

    if int(resolution) in resolutions:
        video_res = resolution + "p"
        yd = yt.streams.filter(res=video_res).first()
        name = yt.title
        special_characters = ['@', '#', '$', '*', '&', '|', ' ', '?', '^']
        new_name = ""
        for i in name:
            if i not in special_characters:
                new_name = new_name + i
        new_name = new_name + ".mp4"
        print("Downloading " + name+" ..............")
        yd.download(path, new_name)
        print(name + "Downloaded Successfully")
    else:
        print("Unknown Resolution")


def download_playlist():
    # first step, check if the link is for the playlist url or video in the playlist
    link = input("Enter the link: ")
    if "playlist" not in link:  # it's a video of the playlist
        url = get_url_from_video
    else:
        url = link

    # second step, getting playlist urls
    urls = get_playlist_urls(url)

    # third step, getting the path to save the playlist
    path = getting_path()
    # fourth step, getting the resolution
    resolution, resolutions = get_resolution_for_video(urls[0])
    # sixth step, loop on the urls and download it
    for video_url in urls:
        download_video(video_url, resolution, resolutions, path)
    print("Playlist downloaded successfully")


def download_one_video():
    link = input("Enter the link: ")
    path = getting_path()
    resolution, resolutions = get_resolution_for_video(link)
    download_video(link, resolution, resolutions, path)


download_playlist()
