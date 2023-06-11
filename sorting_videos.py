import os
import re
from googleapiclient.discovery import build
import pandas as pd
api_key = os.environ.get('pyt_accesskey')


youtube = build('youtube','v3',developerKey=api_key)
playlistID = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
nextPageToken= None


playlist = youtube.playlistItems().list(
    part='contentDetails',
    playlistId=playlistID,
    maxResults=50,
    pageToken=nextPageToken # none gives us the first page of results
)
request =playlist.execute()
vid_ids=[]
for index in request['items']:
    #i=0
    vid_ids.append(index['contentDetails']['videoId'])
video = youtube.videos().list(
    part='contentDetails',
    id=vid_ids # can also use ','.join(vid_ids)
)
Duration=[]
vstats = video.execute()


sum_m=0
sum_h=0
sum_s=0
for item in vstats['items']:
    print(item)
    print('\n\n\n')
    durat=item['contentDetails']['duration']
    
    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')# to catch digits bfr a capital M
    seconds_pattern = re.compile(r'(\d+)S') 
    
    hours = hours_pattern.search(durat)
    minutes = minutes_pattern.search(durat)
    seconds = seconds_pattern.search(durat)

    hours  = int(hours.group(1)) if minutes else 0
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1)) if minutes else 0

    videoseconds = timedelta(hours=hours,minutes=minutes,seconds=seconds).total_seconds()

    print(video_seconds)

#checkin if anymore pages are left
