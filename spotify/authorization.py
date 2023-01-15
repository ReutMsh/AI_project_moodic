import tekore as tk


def get_user_token(user_name):
    """
    Read the config file according to the username specified and returns the token for the spotify user.
    """
    CONFIG_FILE = 'spotify\credentials_' + user_name + '.config'
    conf = tk.config_from_file(CONFIG_FILE, return_refresh=True)
    token = tk.refresh_user_token(*conf[:2], conf[3])
    return token