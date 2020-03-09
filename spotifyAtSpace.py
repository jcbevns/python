from __future__ import print_function    # (at top of module)
import spotipy
import os
import json
import sys
import spotipy.util as util
import time 
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

username = '1230966705'
client_id = '0d632b21e74c4f86b991255a4623d528'
client_secret = '64ec1b6290e74a88a3c9895bd1851166'
redirect_uri = 'http://example.com/callback/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

pi3targetID = "3624ae2848450d67a127389db8bec8ec4a6892ee"

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    command = sp.start_playback(device_id=pi3targetID)
    pi3MaxVolume = sp.volume(volume_percent, device_id=pi3targetID)
    print("pi3")
else:
    print ("Can't get token for", username)



sp = spotipy.Spotify()

# not sure if this is gonna work

def pi3Start():
	sp.start_playback(device_id=pi3targetID)

pi3MaxVolume = sp.volume(volume_percent, device_id=pi3targetID)

pi3start()
pi3MaxVolume()

