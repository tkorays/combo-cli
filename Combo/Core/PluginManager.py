import importlib
import sys
import os


class PluginManager:
    def __init__(self, root):
        self.root = root

    def add_plugin_path(self, p: str):
        if not os.path.exists(p):
            raise Exception('plugin path {} is not exist!'.format(p))
        if p not in sys.path:
            sys.path.append(p)

    def load(self, name: str):
        module = importlib.import_module(name)
        module = importlib.reload(module)
        # TODO: module has no plugin attribute?
        for n, f in module.plugin['functions'].items():
            self.root.add_command(f)

    def plugin_exist(self, name: str):
        return False
