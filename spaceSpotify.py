from __future__ import print_function    # (at top of module)
import spotipy
import os
import json
import sys
import spotipy.util as util
import time 
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp.trace=False

username = '1230966705'
client_id = 'ad7816b31ce8423fbc05646f14bfce49'
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect_uri = 'http://example.com/callback/'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#spaceTargetID = "a9c10be65d783a01393445c2aba85a1782c11402"
spaceTargetID = "5a0e6f83bdf11ea662e3228c4417264cc137b768"

try: 
	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
	os.remove(f".cache-{username}")

#created spotipy opbject with permissions
#spotifyObject = spotipy.Spotify(auth=token)

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    spaceStart = sp.start_playback(device_id=spaceTargetID)
    spaceMaxVolume = sp.volume(volume_percent, device_id=spaceTargetID)
    print("space")
else:
    print ("Can't get token for", username)

#sp = spotipy.Spotify()

print(res)

# contained in "if" fn
#spaceStart = sp.start_playback(device_id=spaceTargetID)
#spaceMaxVolume = sp.volume(volume_percent, device_id=spaceTargetID)

#spacestart()
sp.Volume(100)

