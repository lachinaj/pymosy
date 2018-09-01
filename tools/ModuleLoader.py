from os.path import dirname, basename, isfile
import glob
import imp

class ModuleLoader:
    def __init__(self):
        pass

    def load(self, directory):
        dirmodules = glob.glob(directory+"/*")
        modules = [basename(f) for f in dirmodules if not isfile(f)]

        for name in modules:
            mod = __import__(directory+"."+name+"."+name, fromlist=["*"])
            module = mod.Module()
