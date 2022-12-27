import tekore as tk
from spotify.auto import get_user_token

NUM_ITEMS = 11

# Initialise client with user's bearer token
token = get_user_token()
spotify = tk.Spotify(token)


def heading(str):
    print(f'\n{str}\n{"-" * len(str)}')


# Print the user's top artists
heading(f'Top {NUM_ITEMS} Artists')
for index, artist in enumerate(spotify.current_user_top_artists(limit=NUM_ITEMS).items):
    print(index+1, artist.name)

# Print the user's top tracks
heading(f'Top {NUM_ITEMS} Tracks')
for index, track in enumerate(spotify.current_user_top_tracks(limit=NUM_ITEMS).items):
    print(index+1, track.name, 'by', track.artists[0].name)