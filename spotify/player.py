def get_first_available_device(spotify):
    available_devices = spotify.playback_devices()

    # If we have no available devices, exit the program
    if len(available_devices) == 0:
        print('No devices are available for this user.\nExiting...')
        exit()

    if available_devices[0].is_active:
        return available_devices[0]
    else:
        print(
            f'{available_devices[0].name} ({available_devices[0].type}) is not currently active.\nPlease play and pause a song on it and try again.\nExiting...')
        exit()