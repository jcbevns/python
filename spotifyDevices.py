import spotipy
import os
import json
import sys
import spotipy.util as util
import webbrowser
import requests
from json.decoder import JSONDecodeError

username = '1230966705'
client_id = 'ad7816b31ce8423fbc05646f14bfce49'
client_secret = '461d8ae9476f4947bbeb6063458173f6'
redirect_uri = 'http://example.com/callback/'
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
track = sp.current_user_playing_track()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist != "":
    print("Currently playing " + artist + " - " + track)

# User information
#user = sp.current_user()
#displayName = user['display_name']
#followers = user['followers']['total']

#print(devices)
ids = []
for x in range(len(devices))	:
	for arrayNum in devices['devices']:
		print(arrayNum['id'],arrayNum['is_active'],arrayNum['volume_percent'],arrayNum['type'],arrayNum['name'])

		





