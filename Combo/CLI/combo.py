import click
import os
from Combo.Core.PluginManager import PluginManager
from Combo.Core.Configurations import Configuration


@click.group(help='Combo! Make work easy!')
def combo():
    pass


pm = PluginManager(combo)
cfg = Configuration()
cfg.username()

pm.add_plugin_path('.')
for p in cfg.plugin_path():
    pm.add_plugin_path(os.path.expanduser(p))

plugins = cfg.plugins()
for plg in plugins:
    pm.load(plg)

