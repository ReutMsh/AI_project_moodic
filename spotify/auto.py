import tekore as tk


def get_user_token():
    CONFIG_FILE = 'credentials.config'
    conf = tk.config_from_file(CONFIG_FILE, return_refresh=True)
    token = tk.refresh_user_token(*conf[:2], conf[3])
    return token