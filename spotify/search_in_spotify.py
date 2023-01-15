import tekore as tk
from spotify.auto import get_user_token
from spotify.player import get_first_available_device

NUM_ITEMS = 1


def emotion_to_playlist(emotion):
    """
    Converts an emotion to a matching playlist ID.

    return ID string of a playlist on spotify"""
    match emotion:
        case 'angry':
            return "37i9dQZF1EIg1pTZ3BUIEF"
        case 'fear':
            return "37i9dQZF1DXbmiyBesoBFy"
        case 'happy':
            return "37i9dQZF1DWYbUY40ZDAwb"
        case 'sad':
            return "37i9dQZF1DWUC4OPrlkH0Z"
        case 'surprise':
            return "37i9dQZF1DXdPec7aLTmlC"


def search_in_spotify(emotion):
    # Get the user's token to be able to make requests on their account
    token = get_user_token()
    spotify = tk.Spotify(token)

    #  Find the first available device
    available_device = get_first_available_device(spotify)

    # get the search-string from emotion_to_song function
    if emotion == "neutral":
        favorite = spotify.current_user_top_tracks()
        spotify.playback_start_tracks(
            [t.id for t in favorite.items], device_id=available_device.id)

    else:
        playlist_id = emotion_to_playlist(emotion)
        playlist_tracks = spotify.playlist(playlist_id, as_tracks=True)
        spotify.playback_start_context(playlist_tracks['uri'], device_id=available_device.id)
