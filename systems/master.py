from tools import Config, ModuleLoader
import time


class Master:
    config = None

    def __init__(self):
        pass

    def initialize(self):
        print("Initialize master:")
        self.config = Config.Config("Config/pymosy.conf")
        self.load_modules()

    def load_modules(self):
        loader = ModuleLoader.ModuleLoader()
        loader.load(self.config.get_parameter('Main', 'ModulesDirectory'))

    def run(self):
        self.initialize()
        try:
            while 1:
                print ("master run")
                time.sleep(1)
        except:
            print("Application error")