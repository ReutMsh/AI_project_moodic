from UserException import noAvailableDevice, noActiveDevice


def get_first_available_device(spotify):
    available_devices = spotify.playback_devices()

    # If we have no available devices, exit the program
    if len(available_devices) == 0:
        print('No devices are available for this user.\nExiting...')
        raise noAvailableDevice

    for device in available_devices:
        if device.is_active:
            return device

    print(
        f'all device are not currently active.\nPlease play and pause a song on any device and try again.\nExiting...')
    raise noActiveDevice
