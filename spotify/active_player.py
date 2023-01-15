from UserException import NoAvailableDevice, NoActiveDevice


# region get_first_available_device
def get_first_available_device(spotify):
    """
    :param spotify: access to the spotify player.
    :return: the available device that is available and active.

    exceptions:
        * NoAvailableDevice: the spotify is not open on any device
        * NoActiveDevice: the spotify is not active on any device
    """
    available_devices = spotify.playback_devices()

    if len(available_devices) == 0:  # no available devices were found, exit the program
        raise NoAvailableDevice

    for device in available_devices:
        if device.is_active:  # found an active device
            return device

    raise NoActiveDevice
# endregion
