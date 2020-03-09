import spotipy
import os
import json
import sys
import spotipy.util as util
import webbrowser
import requests
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials

username = '1230966705'
client_id = 'ad7816b31ce8423fbc05646f14bfce49'
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#https://open.spotify.com/user/1230966705?si=iKWQzMcuQW-_QJJIMbjsPQ

try: 
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
	os.remove(f".cache-{username}")

#created spotipy opbject with permissions
sp = spotipy.Spotify(auth=token)


#Get current device
devices = sp.devices()
deviceID = devices['devices'][0]['id']


# Current track information
trackInfo = sp.current_user_playing_track()
track = sp.current_user_playing_track()
artist = track['item']['artists'][0]['name']
track = track['item']['name']
trackUri = trackInfo['context']['uri']
trackProgress = trackInfo['progress_ms']

print("URI = ", trackUri)
print("Progress_ms = ", trackProgress)

if artist != "":
    print("Currently playing = " + artist + " - " + track)

# User information
#user = sp.current_user()
#displayName = user['display_name']
#followers = user['followers']['total']

print("Device ID                             - Active? -Vol -Type - Name")
ids = []
for x in range(len(devices))	:
	for arrayNum in devices['devices']:
		print(arrayNum['id'],arrayNum['is_active'],arrayNum['volume_percent'],arrayNum['type'],arrayNum['name'])

		
#sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth,scope=scope)
sp.volume(100)
print("Volume @ 100%")



