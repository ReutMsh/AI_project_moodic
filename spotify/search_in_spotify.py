import tekore as tk
from spotify.auto import get_user_token
from spotify.player import get_first_available_device
from connect_emotion_to_spotify import emotion_to_song



NUM_ITEMS = 1

# Get the user's token to be able to make requests on their account
token = get_user_token()
spotify = tk.Spotify(token)

#  Find the first available device
available_device = get_first_available_device(spotify)

# get the search string from the user
#search_string = input("Enter something: ")

# get the search string from connect_emotion_to_spotify file

search_string = emotion_to_song()
print(f"your search is {search_string}\n")

# get the tracks found from this search
tracks, = spotify.search(query=search_string, types=('playlist',), limit=NUM_ITEMS)

# play the songs!
print(f'About to play {len(tracks.items)} tracks for "{search_string}" on {available_device.name} ({available_device.type})')
for index, track in enumerate(tracks.items):
    print(index+1, track.name)

playlist_tracks = spotify.playlist(tracks.items[0].id, as_tracks=True)
spotify.playback_start_context(playlist_tracks['uri'], device_id=available_device.id)

'''spotify.playback_start_tracks(
    playlist_tracks.tracks.items, device_id=available_device.id)
'''