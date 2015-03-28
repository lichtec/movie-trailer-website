#!/usr/bin/python
#Basically the search example from Google Developer portal with some modifications to limit the search and the results.

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyB79fUYvpg-y17g1rswOKmTloNKwwj8TJ0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  #print options
  search_response = youtube.search().list(
    q=options,
    part="id,snippet",
    maxResults=1,
	type="video"
  ).execute()

  videos = []
  #channels = []
  #playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
	#print search_result
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(str(search_result["id"]["videoId"]))

  return videos
  #print "Channels:\n", "\n".join(channels), "\n"
  #print "Playlists:\n", "\n".join(playlists), "\n"


def trailer(title):
  try:
    return youtube_search(title)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
