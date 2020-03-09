from __future__ import print_function    # (at top of module)
import spotipy
import os
import json
import sys
import spotipy.util as util
import time 
from spotipy.oauth2 import SpotifyClientCredentials

#spaceTargetID = "a9c10be65d783a01393445c2aba85a1782c11402"
username = '1230966705'
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


