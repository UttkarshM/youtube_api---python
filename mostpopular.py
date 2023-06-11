from googleapiclient.discovery import build
import os

api_key=os.environ.get('pyt_accesskey')
pl_id='PLMBYlcH3smRyLrmf5zve7E2hIvsYmUflc'
youtube = build('youtube','v3',developerKey=api_key)

playlist = youtube.playlistItems().list(
    part='snippet',
    playlistId=pl_id,
    maxResults=50
)
video_ids=[]
#while playlist is not None:
resp = playlist.execute()
for index in resp['items']:
    print(index['snippet']['resourceId']['videoId'])
    video_ids.append(index['snippet']['resourceId']['videoId'])
url_views=[]
for vids in video_ids:
    strr = f'https://youtube.com/watch?v={vids}' # or can just use https://youtu.be/{vids}
    video = youtube.videos().list(
        part='statistics,snippet',
        id=vids,
        maxResults=50
    )
    v_resp = video.execute()
    for indd in v_resp['items']:
        
        print(indd['statistics']['viewCount'])
        url_views.append(
            {
            'views':int(indd['statistics']['viewCount']),
            'url':strr
            }
        )
#https://www.w3schools.com/python/ref_list_sort.asp
url_views.sort(key=lambda vid:vid['views'],reverse=True)

for inde in url_views:
    print(inde)







