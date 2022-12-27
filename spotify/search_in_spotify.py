import tekore as tk
from spotify.auto import get_user_token
from spotify.player import get_first_available_device

NUM_ITEMS = 11

# Get the user's token to be able to make requests on their account
token = get_user_token()
spotify = tk.Spotify(token)

#  Find the first available device
available_device = get_first_available_device(spotify)

'''if len(sys.argv) == 1:
    print(f'Usage: python {sys.argv[0]} <string_to_search>')
     exit()'''

# get the search string from the user
search_string = input("Enter something: ")

# get the tracks found from this search
tracks, = spotify.search(query=search_string, limit=NUM_ITEMS)

# play the songs!
print(f'About to play {len(tracks.items)} tracks for "{search_string}" on {available_device.name} ({available_device.type})')
for index, track in enumerate(tracks.items):
    print(index+1, track.name, 'by', track.artists[0].name)
spotify.playback_start_tracks(
    [t.id for t in tracks.items], device_id=available_device.id)
