class OpenCameraException(Exception):
    pass

    def __init__(self, message="Your camera cannot be accessed.\n"
                               "It might be currently occupied.\n"
                               "Please close any application or program that is currently using your camera"):
        self.message = message
        super().__init__(self.message)
