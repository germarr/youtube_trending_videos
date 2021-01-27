## Call the "build()" function from the Python-client
from googleapiclient.discovery import build

api_key= ""

youtube = build("youtube","v3", developerKey=api_key)

nextPageToken = None

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
    # In my case I choose "MX" which means "Mexico". 

    maxResults=50

    # The maxResults parameter specifies how many results you want to be returned in the call. 
    # I choose 50 because that's the max number you can get per call. 

    ).execute()