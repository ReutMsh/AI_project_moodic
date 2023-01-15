import tekore as tk
from UserException import NoSpotifyPremium
from spotify.authorization import get_user_token
from spotify.active_player import get_first_available_device


# NUM_ITEMS = 1


# region convert_emotion_to_playlist_ID
def convert_emotion_to_playlist_ID(emotion):
    """
    Converts an emotion to a matching playlist ID.

    :param emotion: string that represents the emotion
    :return: ID string of a playlist on spotify
    """
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
# endregion


# region activate_emotion_based_playlist_in_spotify
def activate_emotion_based_playlist_in_spotify(emotion, user_name):
    """
    :param emotion: type of playlist to activate
    :param user_name: play on this user
    :return: None
    """
    # Get the user's token to be able to make requests on their account
    token = get_user_token(user_name)
    spotify = tk.Spotify(token)

    available_device = get_first_available_device(spotify)

    try:
        if emotion == "neutral":
            # activate songs from the 'liked songs' playlist
            favorite = spotify.current_user_top_tracks()
            spotify.playback_start_tracks([t.id for t in favorite.items], device_id=available_device.id)

        else:
            # activate emotion-based playlist
            playlist_id = convert_emotion_to_playlist_ID(emotion)
            playlist_tracks = spotify.playlist(playlist_id, as_tracks=True)
            spotify.playback_start_context(playlist_tracks['uri'], device_id=available_device.id)

    except:     # exception will accrue if  the user doesn't own a Premium account
        raise NoSpotifyPremium
# endregion
