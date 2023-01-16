class OpenCameraException(Exception):
    pass

    def __init__(self, message="Your camera cannot be accessed.\n"
                               "It might be currently occupied.\n\n"
                               "Please close any application or program\n"
                               "that is currently using your camera"):
        self.message = message
        super().__init__(self.message)


class NoAvailableDevice(Exception):
    pass

    def __init__(self, message="None of your devices are currently\n"
                               "connected to Spotify.\n\n"
                               "Please connect one of your devices\n"
                               "and try again"):
        self.message = message
        super().__init__(self.message)


class NoSpotifyPremium(Exception):
    pass

    def __init__(self, message="Your account has not been\n"
                               "upgraded to Spotify Premium.\n\n"
                               "In order to enjoy moodic \n"
                               "please upgrade to Premium\n"
                               "and try again."):
        self.message = message
        super().__init__(self.message)


class NoActiveDevice(Exception):
    pass

    def __init__(self, message="The player is not playing..\n\n"
                               "Please play and pause a song\n"
                               "on any device and try again.\n"):
        self.message = message
        super().__init__(self.message)
