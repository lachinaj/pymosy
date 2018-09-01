import time
from systems import module


class Module(module.Module):
    def __init__(self):
        module.Module.__init__(self)
        self.Name = "TestModule"
        self.Version = "1.0"
        self.Description = "Module for testing functionnalities"

        print ("Load module " + self.Name + " v" + self.Version)
        self.start()

    def run(self):
        while 1:
            print("Test module run")
            time.sleep(1)
