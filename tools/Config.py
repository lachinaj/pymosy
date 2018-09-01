import ConfigParser
import os
import sys


class Config(object):
    filename = ""

    def __init__(self, filename="Config/pymosy.conf"):
        self.filename = filename
        self.config = ConfigParser.ConfigParser()

        # Default value
        self.config.add_section('Main')
        self.config.set('Main', 'ModuleDirectory', './Modules')

        self.config.read(filename)

    def get_parameter(self, section, name):
        return self.config.get(section, name)

    def set_parameter(self, section, name, value):
        self.config.set(section, name, value)
        self.save()

    def save(self):
        with open(self.filename, 'wb') as configfile:
            self.config.write(configfile)
