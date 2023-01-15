import tekore as tk


def get_user_token():
    """
    Read the config file and returns the token for the spotify user.
    """
    CONFIG_FILE = '../credentials_Tamar.config'
    conf = tk.config_from_file(CONFIG_FILE, return_refresh=True)
    token = tk.refresh_user_token(*conf[:2], conf[3])
    return token