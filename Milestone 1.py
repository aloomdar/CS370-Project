import pytube.exceptions
from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
import os


link = "https://www.youtube.com/playlist?list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL"
playlist = Playlist(link)

maxVideos = 10
start = 0

for video in playlist.videos:
    start += 1
    if start <= maxVideos:
        try:
            print("Attempting to Download Video #", start)
            video.streams.get_highest_resolution().download(filename_prefix='Video ' + f'{start} ')
            print("Done Downloading.")

            print("Getting Closed Captions.")
            videoID = video.video_id
            captions = YouTubeTranscriptApi.get_transcript(videoID)

            with open('Video ' f'{start} ' f'{video.video_id}.txt', 'w') as file:
                for caption in captions:
                    file.write(caption['text'] + "\n")

            print("Done Getting Closed Captions.\n")
        except pytube.exceptions.AgeRestrictedError:
            print("Video age restricted.\nDownloading Next Video.")
            start -= 1
