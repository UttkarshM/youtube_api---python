import os
import re
from googleapiclient.discovery import build
import pandas as pd
api_key = os.environ.get('pyt_accesskey')


youtube = build('youtube','v3',developerKey=api_key)

# request = youtube.channels().list(
#     part='contentDetails, statistics',
#     forUsername='schafer5'
# )
# response = list(request.execute())
# new = pd.DataFrame.from_dict(response)
# print(response)
# print(new.index)

#for finding the playlists in his channel

# request_playlist = youtube.playlists().list(
#     part='contentDetails,snippet',
#     channelId="UCCezIgC97PvUuR4_gbFUs5g"# you get that by the above program
# )
# play_lists= request_playlist.execute()

# for item in play_lists['items']:
#     print(item['id'])
#     print()
#     print()

#     print(item)
#     print()

playlist = youtube.playlistItems().list(
    part='contentDetails',
    playlistId='PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'
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
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')# to catch digits bfr a capital M
seconds_pattern = re.compile(r'(\d+)S') 

sum_m=0
sum_h=0
sum_s=0
for item in vstats['items']:
    durat=item['contentDetails']['duration']
    hours = hours_pattern.search(durat)
    minutes = minutes_pattern.search(durat)
    seconds = seconds_pattern.search(durat)

    #can use ternary conditional but can also use if statements
    #we would get an error if there were was no return value
    hours=int(hours.group(1)) if hours else 0
    sum_h +=hours
    minutes = int(minutes.group(1)) if minutes else 0
    sum_m +=minutes
    seconds=int(seconds.group(1)) if seconds else 0
    sum_s +=seconds

sentence = f'the total videotime the entire playlist is {sum_h} hours, {sum_m} minutes ,and {sum_s} seconds'
print(sentence)

    #some notes lmaoo
    #we will get only integer if we use group(1)
    
    #Duration.append(item['contentDetails']['duration'])

        #i=i+1
# times=(',').join(Duration)
# print(times)
# time=times.split(',')
# print(time) 
