# Trending Youtube Videos

This script is part of my research project called "What Topics Drives Youtube MX?". You can check the whole project [**here**]("https://gmarr.com/").

The main purpose of this code is to get the most relevant information from all the videos that are appearing on the [**Trending**]("https://www.youtube.com/feed/trending") page of Youtube, on any particular region, and export the results to a CSV file.

Here's an example of the final result you can get after running the script:

| published_date | trending_date | channel_title | video_title | views | likes | dislikes | comments | description | channel_id | link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2020-10-23T21:30:14Z | 2020-10-24T21:00:00Z | ArianaGrandeVevo | Ariana Grande - positions (official video) | 28005774| 2575454 | 37165 | 202362 | Here goes a description | UC0VOyT2OCBKdQhF3BAbZ-1g | https://youtu.be/tcYodQoapMg |

<br>

## The File
---
The `get_video_list.py` file makes a call to the Youtube API, gets the information of the first 50 videos on the "Trending" page and export that information into a CSV file.

## Tutorial
---
### 1. General Concepts
To follow the code in this tutorial I would recommend to have some knowledge of the next concepts:
* Python
    * `for` loops
    * functions
    * pip. 
        * [Here]("https://realpython.com/what-is-pip/") you can find a really good article that expalins what is pip.
    * pandas. 
        * [This]("https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html") is a gentle introduction to the pandas library.
* JSON
    * The general structure of a JSON file
* API's
    * Specifically, the tutorial is going to make more sense if you know what is an API Key. To learn more about API's I recommend to watch this [video]("https://www.youtube.com/watch?v=GZvSYJDk-us&t=4641s"). The video shows the inner workings of the [Trello API]("https://developer.atlassian.com/cloud/trello/rest/") however, the concepts that are shown can be applied to any API. This is my "go-to" reference guide when I'm stucked.

If you do not know how any of this concepts work I added resources troughout the tutorial that can be revised

### 2. The Set Up
In addition to the concepts mentioned above, before you start the tutorial be sure to have:

* A Youtube API Key
    * In order to retrieve the data from Youtube we're going to use the [Youtube API]("https://developers.google.com/youtube/v3"). All the API's from Google properties require a Google Account and autorization credentials.
    * To learn how to setup a Google Account and get this credentials you can follow this [tutorial]("https://developers.google.com/youtube/registering_an_application").
    * Once you have your credentials, you need to request an API Key. You can follow [this instructions]("https://cloud.google.com/resource-manager/docs/creating-managing-projects?visit_id=637472330160631271-1024614839&rd=1") to get your API Key.
    * If you want additional information about the API setup, Youtube offers a nice introduction [here]("https://developers.google.com/youtube/v3/getting-started).
* A Code Editor
    * I use VS Code. You can download it [here]("https://code.visualstudio.com/").
* Python
    * If you use a Mac you already have Python installed. If you use a Windows PC or Linux, you can download Python [here]("").
    * The `pandas` library. You can download it from [here]("https://pandas.pydata.org/").

### 3. The Code

1. Download the [google python client]("https://github.com/googleapis/google-api-python-client") via pip. 

```python
pip install google-api-python-client
```
2. Import the “build” function from the Google Python Client. This function helps to abstract a lot of the code needed to use the Youtube API.

```python
from googleapiclient.discovery import build
```
3. Get your API Key from the [Google Developer Console]("https://console.developers.google.com/") and copy it. 
4. Create a variable called `api_key` and paste the API Key that you copied from the Google Developer Console. Then create a variable called `youtube` and assign it the `build()` function with the parameters
 `youtube`, `v3` and `developerKey = api_key`

```python
api_key= "<Paste your API KEY here>"

youtube = build("youtube","v3", developerKey=api_key)
```

* [Here]("https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build") you can learn all the arguments that can be used in the `build()` function.
* I would also recommend to check all the different methods that the youtube API can use. You can find them [here]("https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html").

5. We’re going to use the `videos()` method inside the `build()` function that we created. [Here]("https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.videos.html") you can find all the methods that can be used on `video()`. For this tutproal we’re going to use the `list()` method and [here]("https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.videos.html#list") are all the parameters that can be used inside `list()`.

6. Once the parameters are added into the “list()” method the final step is to add the “execute()” method so everything can be executed.

```python
chart_mx= youtube.videos().list(

    part=["id","snippet","statistics"],
    # Part is a required parameter to make this method work. 
    # Inside this parameter you can specify the resources you want the API to return. 
    # Fore more information check the documentation that I shared for the list() method.

    chart="mostPopular",
    # The chart parameter specifies the chart you want to get information from. 
    # In my case I choose the "mostPopular" chart. This is the "Trending" playlist.

    regionCode="MX",
    # The regionCode parameter specifies which country you want to get the information from. 
    # In my case I choose "MX" which represents "Mexico". 

    maxResults=50
    # The maxResults parameter specifies how many results you want to be      returned in the call. 
    # I choose 50 because that's the max number you can get per call. 

    ).execute()
```
7. The API call returns a JSON file. Here’s and example of a single JSON item from that call:

```js
{'kind': 'youtube#video',
   'etag': 'pLCG4kSHJ6otRo8C1QR1bA-k120',
   'id': 'LGkUW5cUPz8',
   'snippet': {'publishedAt': '2021-01-25T15:00:10Z',
    'channelId': 'UCOmHUn--16B90oW2L6FRR3A',
    'title': 'ROSÉ - COMING SOON TEASER',
    'description': 'Get a first preview of ROSÉ's solo project at 2021 BLACKPINK: THE SHOW! 🖤💖\n\nDon't forget to join membership and watch the livestream concert on JAN 31 SUN 2PM (KST), only on BLACKPINK YouTube channel!\n\nBuy Access @ https://yt.be/music/BLACKPINKTheShow\n\n#BLACKPINK #블랙핑크 #ROSÉ #로제 #COMINGSOON #TEASER #PALMSTAGE #THESHOW #LIVESTREAMCONCERT #YOUTUBEMUSIC #YOUTUBE #YG',
    'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/LGkUW5cUPz8/default.jpg',
      'width': 120,
      'height': 90},
     'medium': {'url': 'https://i.ytimg.com/vi/LGkUW5cUPz8/mqdefault.jpg',
      'width': 320,
      'height': 180},
     'high': {'url': 'https://i.ytimg.com/vi/LGkUW5cUPz8/hqdefault.jpg',
      'width': 480,
      'height': 360},
     'standard': {'url': 'https://i.ytimg.com/vi/LGkUW5cUPz8/sddefault.jpg',
      'width': 640,
      'height': 480},
     'maxres': {'url': 'https://i.ytimg.com/vi/LGkUW5cUPz8/maxresdefault.jpg',
      'width': 1280,
      'height': 720}},
    'channelTitle': 'BLACKPINK',
    'tags': ['YG Entertainment',
     'YG',
     '와이지',
     'K-pop',
     'BLACKPINK',
     '블랙핑크'],
    'categoryId': '10',
    'liveBroadcastContent': 'none',
    'localized': {'title': 'ROSÉ - COMING SOON TEASER',
     'description': 'Get a first preview of ROSÉ's solo project at 2021 BLACKPINK: THE SHOW! 🖤💖\n\nDon't forget to join membership and watch the livestream concert on JAN 31 SUN 2PM (KST), only on BLACKPINK YouTube channel!\n\nBuy Access @ https://yt.be/music/BLACKPINKTheShow\n\n#BLACKPINK #블랙핑크 #ROSÉ #로제 #COMINGSOON #TEASER #PALMSTAGE #THESHOW #LIVESTREAMCONCERT #YOUTUBEMUSIC #YOUTUBE #YG'},
    'defaultAudioLanguage': 'en'},
   'statistics': {'viewCount': '15400465',
    'likeCount': '2589784',
    'dislikeCount': '20372',
    'favoriteCount': '0',
    'commentCount': '439932'}}
```

8.  To organize this file into a dataframe first create an empty list and assigned it to a variable called `top_videos`. This variable is going to store the dataframe. Secondly, write a `for` loop to append all the JSON items that were stored in the `chart_mx` variable, into my empty list. 

9. For this example I picked 13 different variables from the videos. All the information from these variables comes from the API call, however I added additional information to some of the data points in order to make them more usable for my final goal. Specifically I created a variable called `trending_date` which records the time the video was at the “Trending” page and “link” which creates a direct link to the video. Think about the data you would like to retrieve and only add those parameters into the API call.

```python
from datetime import datetime,date

date_new= date(datetime.now().year,datetime.now().month,datetime.now().day).isoformat()

hour=datetime.now().hour

top_videos=[]

for i in chart_mx["items"]:
    vid_id=i["id"]
    ytb_link=f"https://youtu.be/{vid_id}"
    
    top_videos.append({
        "published_date":i["snippet"]["publishedAt"],
        "trending_date":f"{date_new}T{hour}:00:00Z",
        "category_id":i["snippet"]["categoryId"],
        "channel_title":i["snippet"]["channelTitle"],
        "video_title":i["snippet"]["title"],
        "views":i["statistics"]["viewCount"], 
        "likes":i["statistics"]["likeCount"],
        "dislikes":i["statistics"]["dislikeCount"],
        "comments":i["statistics"].get("commentCount"),
        "description":i["snippet"]["description"],
        "channel_id":i["snippet"]["channelId"],
        "link":ytb_link,
        "thumbnail":i["snippet"]["thumbnails"]["medium"]["url"]
    })
```
10. To build the `link` variable I joined the string `https://youtu.be/` with the id of the video. The id of the video comes through the API call. This code snippet is included in the `for` loop. Once the `for` loop finishes, the `top_videos` variable will have a list with all the data in the order that was requested. Here’s an example of the result:

```python
{'published_date': '2021-01-25T15:00:10Z',
  'trending_date': '2021-01-26T16:00:00Z',
  'category_id': '10',
  'channel_title': 'BLACKPINK',
  'video_title': 'ROSÉ - COMING SOON TEASER',
  'views': '15400465',
  'likes': '2589784',
  'dislikes': '20372',
  'comments': '439932',
  'description': 'Get a first preview of ROSÉ's solo project at 2021 BLACKPINK: THE SHOW! 🖤💖\n\nDon't forget to join membership and watch the livestream concert on JAN 31 SUN 2PM (KST), only on BLACKPINK YouTube channel!\n\nBuy Access @ https://yt.be/music/BLACKPINKTheShow\n\n#BLACKPINK #블랙핑크 #ROSÉ #로제 #COMINGSOON #TEASER #PALMSTAGE #THESHOW #LIVESTREAMCONCERT #YOUTUBEMUSIC #YOUTUBE #YG',
  'channel_id': 'UCOmHUn--16B90oW2L6FRR3A',
  'link': 'https://youtu.be/LGkUW5cUPz8',
  'thumbnail': 'https://i.ytimg.com/vi/LGkUW5cUPz8/mqdefault.jpg'}
```

11. The final step is creating a pandas dataframe using the data stored in the `top_videos` variable, and then exporting it to a CSV file.  Firstly, create a variable called `title`. This string is going to be used as a title for the exported CSV file. Secondly, import pandas and use the `from_dict` method to transform the `top_videos` variable into a dataframe. Lastly, using the `.to_csv` method export the dataframe into a CSV file.

```python
import pandas as pd

title=f"{date_new[0:4]}_{date_new[5:7]}_{date_new[8:10]}_{datetime.now().hour}"

pd.DataFrame.from_dict(top_videos).to_csv(f"{title}.csv")
```

### Complete Script
Here's an example of how everything looks like at the end:

```python
from googleapiclient.discovery import build
from datetime import datetime,date
import pandas as pd

date_new= date(datetime.now().year,datetime.now().month,datetime.now().day).isoformat()

hour=datetime.now().hour

api_key= "<Paste your API KEY here>"

youtube = build("youtube","v3", developerKey=api_key)

top_videos=[]

title=f"{date_new[0:4]}_{date_new[5:7]}_{date_new[8:10]}_{datetime.now().hour}"

chart_mx= youtube.videos().list(
    part=["id","snippet","statistics"],
    chart="mostPopular",
    regionCode="MX",
    maxResults=50).execute()

for i in chart_mx["items"]:
    vid_id=i["id"]
    ytb_link=f"https://youtu.be/{vid_id}"
    
    top_videos.append({
        "published_date":i["snippet"]["publishedAt"],
        "trending_date":f"{date_new}T{hour}:00:00Z",
        "category_id":i["snippet"]["categoryId"],
        "channel_title":i["snippet"]["channelTitle"],
        "video_title":i["snippet"]["title"],
        "views":i["statistics"]["viewCount"], 
        "likes":i["statistics"]["likeCount"],
        "dislikes":i["statistics"]["dislikeCount"],
        "comments":i["statistics"].get("commentCount"),
        "description":i["snippet"]["description"],
        "channel_id":i["snippet"]["channelId"],
        "link":ytb_link,
        "thumbnail":i["snippet"]["thumbnails"]["medium"]["url"]
    })

pd.DataFrame.from_dict(top_videos).to_csv(f"{title}.csv")

```

## Final Toughts
--- 
You can use this code as a starting point to get the information that is relevant to your particular needs. I recommend to check all the documentation of the Youtube API, this is the quickest way to learn about the data that can (and can`t) be requested.






