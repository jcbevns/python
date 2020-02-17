import spotipy
import os
import json
import sys
import spotipy.util as util
import webbrowser
import requests
from json.decoder import JSONDecodeError

username = '1230966705'
client_id = '0d632b21e74c4f86b991255a4623d528'
client_secret = os.environ["SPOTIFY_SECRET"]
redirect_uri = 'http://example.com/callback/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'


#https://open.spotify.com/user/1230966705?si=iKWQzMcuQW-_QJJIMbjsPQ

try: 
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
	os.remove(f".cache-{username}")

#created spotipy opbject with permissions
spotifyObject = spotipy.Spotify(auth=token)


#Get current device
devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

# Current track information
track = spotifyObject.current_user_playing_track()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist != "":
    print("Currently playing " + artist + " - " + track)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

#print(devices)
ids = []
for x in range(len(devices))	:
	for arrayNum in devices['devices']:
		print(arrayNum['id'],arrayNum['is_active'],arrayNum['volume_percent'],arrayNum['type'],arrayNum['name'])

		




