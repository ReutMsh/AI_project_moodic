class OpenCameraException(Exception):
    pass

    def __init__(self, message="Your camera cannot be accessed.\n"
                               "It might be currently occupied.\n"
                               "Please close any application or program that is currently using your camera"):
        self.message = message
        super().__init__(self.message)

class noAvailableDevice(Exception):
    pass

    def __init__(self, message="None of your devices are currently connected to Spotify.\n"
                               "Please connect one of your devices to Spotify."):
        self.message = message
        super().__init__(self.message)

class noSpotifyPremium(Exception):
    pass

    def __init__(self, message="Your account has not been upgraded to Spotify Premium.\n"
                               "In order to enjoy moodic you must set it as premium first."):
        self.message = message
        super().__init__(self.message)

class noActiveDevice(Exception):
    pass

    def __init__(self, message="all device are not currently active\n"
                               "Please play and pause a song on any device and try again.\n"):
        self.message = message
        super().__init__(self.message)