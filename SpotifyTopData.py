from collections import Counter
import spotipy
import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read user-read-private user-read-playback-state user-modify-playback-state'

# Erase the cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

if token:

    # Create the spotifyObject
    sp = spotipy.Spotify(auth=token)

    sp.trace = False

    # Set list for checked time ranges
    ranges = ['short_term', 'medium_term', 'long_term']

    #  Now we define a dictionary pairing the ranges to more concrete time intervals.
    timeInterval = {'short_term':'this month ','medium_term':'this year ','long_term':'all time '}

    for range in ranges:

        # Initialize an empty list for the genres.
        genres = []

        print("range:", timeInterval[range])

        # Get the top 10 artists listened to during this time range.
        artistsResults = sp.current_user_top_artists(time_range=range, limit = 25)

        # Get the top 10 tracks listened to during this time range.
        trackResults = sp.current_user_top_tracks(time_range=range, limit = 25)


        print('Artists')
        for i, item in enumerate(artistsResults['items']):
            # Add in all the different genres covered by these artists
            genres += item['genres']
            print(str(i + 1)+":",item['name'])

        print()

        print('Tracks')
        for i, item in enumerate(trackResults['items']):
            print(str(i + 1)+":", item['artists'][0]['name']+" - "+item['name'])

        print()
        print("Your most listented to genre of "+timeInterval[range] +"is "+ Counter(genres).most_common(1)[0][0] + "!")
        print()
else:
    print("Can't get token for", username)
