class OpenCameraException(Exception):
    pass

    def __init__(self, message="Your camera cannot be accessed.\n"
                               "It might be currently occupied.\n\n"
                               "Please close any application or program that is currently using your camera"):
        self.message = message
        super().__init__(self.message)


class NoAvailableDevice(Exception):
    pass

    def __init__(self, message="None of your devices are currently connected to Spotify.\n\n"
                               "Please connect one of your devices to Spotify."):
        self.message = message
        super().__init__(self.message)


class NoSpotifyPremium(Exception):
    pass

    def __init__(self, message="Your account has not been upgraded to Spotify Premium.\n\n"
                               "In order to enjoy moodic please upgrade your Spotify account."):
        self.message = message
        super().__init__(self.message)


class NoActiveDevice(Exception):
    pass

    def __init__(self, message="There is not a single device with an active Spotify player.\n\n"
                               "Please play and pause a song on any device and try again.\n"):
        self.message = message
        super().__init__(self.message)
