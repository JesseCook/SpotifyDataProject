# SpotifyDataProject
This repository is dedicated to working with the Spotify API to collect data, and then using that data to do things like viewing how my musical tastes have changed through the years. I plan to learn more about my overall habits when it comes to how I consume music-based media.

# Installation
In order to use this Python script you will want to first install the Spotipy Python library. You will find full Spotipy documentation here:

https://spotipy.readthedocs.io/en/latest/

Next, you will want to set up authentication for using Spotify's API by getting your Client ID, and Client Secret Code too. You may find both of these values here:

https://developer.spotify.com/dashboard/

Once you have logged in to the developer dashboard you can create a new app to host this code. Fill out the form for a new app with the default information, or as you please, except you must add the following link to your Redirect URIs:

http://google.com/

This will give you access to your Client ID, and Client Secret Code. After you have downloaded our script, open the terminal and move to the directory that you saved the script. After you are in this directory write the following code:
```
export SPOTIPY_CLIENT_ID='clientID'
export SPOTIPY_CLIENT_SECRET='client_secret'
export SPOTIPY_REDIRECT_URI='http://google.com/'
```
In the above code, replace clientID and client_secret with the values you find on the developer dashboard. Each will be a string of numbers and letters.

Lastly, run the program in the same terminal instance by writing the following code:
```
python3 SpotifyTopData.py username
```
Here, use your Spotify username in place of where username is used in the above code snippet. This will run the script and you will be redirected to give permission to access your account data. Once you accept you will be directed to Google, except it will have a much longer URL. Copy and paste the full URL back into the terminal and press enter. Next, your top artists and tracks will be shown. They will be broken up by month, year, and all time. Also, it will show your most listened to genre for each time range. 

Enjoy!
