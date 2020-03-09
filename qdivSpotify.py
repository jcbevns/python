from __future__ import print_function    # (at top of module)
import spotipy
import os
import json
import sys
import spotipy.util as util
import time 
from spotipy.oauth2 import SpotifyClientCredentials

username = '1230966705'
client_id = 'ad7816b31ce8423fbc05646f14bfce49'
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect_uri = 'http://example.com/callback/'
spaceTargetID = "5a0e6f83bdf11ea662e3228c4417264cc137b768"

#created spotipy opbject with permissions
#spotifyObject = spotipy.Spotify(auth=token)
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    spaceStart = sp.start_playback(device_id=spaceTargetID)
    spaceMaxVolume = sp.volume(volume_percent, device_id=spaceTargetID)
    print("space")
else:
    print ("Can't get token for", username)

#spaceStart = sp.start_playback(device_id=spaceTargetID)
#spaceMaxVolume = sp.volume(volume_percent, device_id=spaceTargetID)

spacestart()
sleep(5)
spaceMaxVolume()
spacestart()


