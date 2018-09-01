from threading import Thread
import time


class Module(Thread):
    Name = "Undefined"
    Version = "Undefined"
    Description = "Undefined"

    def __init__(self):
        Thread.__init__(self)
        pass

    def run(self):
        # To be override
        pass
