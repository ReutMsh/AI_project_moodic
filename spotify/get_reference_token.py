import tekore as tk

CONFIG_FILE = 'credentials_Tamar.config'
client_id, client_secret, redirect_uri = tk.config_from_file(CONFIG_FILE)
conf = (client_id, client_secret, redirect_uri)

token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
tk.config_to_file(CONFIG_FILE, conf + (token.refresh_token,))