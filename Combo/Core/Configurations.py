import os
import yaml


class Configuration:
    def __init__(self):
        self.config_path = os.path.expanduser('~')
        self.combo_dot_dir = os.path.join(self.config_path, '.combo')
        self.combo_cfg_path = os.path.join(self.combo_dot_dir, 'combo.yaml')
        self.setup_config()
        self.configs = {}

        self.setup_config()
        self.reload()

    def reload(self):
        with open(self.combo_cfg_path, 'r', encoding='utf-8') as f:
            self.configs = yaml.load(f, Loader=yaml.FullLoader)

    def objects(self):
        return self.configs

    def flush(self, obj=None):
        with open(self.combo_cfg_path, 'r', encoding='utf-8') as f:
            yaml.dump(obj if obj else self.configs,
                      open(os.path.join(self.combo_dot_dir, 'combo.yaml'), 'w', encoding='utf-8'))

    def setup_config(self):
        if not os.path.exists(self.combo_dot_dir):
            os.mkdir(self.combo_dot_dir)
            if not os.path.exists(self.combo_dot_dir):
                raise Exception('Failed to create .combo directory!')

        combo_plugin_dir = os.path.join(self.combo_dot_dir, 'plugins')
        if not os.path.exists(combo_plugin_dir):
            os.mkdir(combo_plugin_dir)
            if not os.path.exists(combo_plugin_dir):
                raise Exception('Failed to create combo plugin directory!')

        obj = {
            'combo_server': 'http://127.0.0.1:8888/combo_api/v1/',
            'plugin_path': [
                '~/.combo/plugins/',
            ],
            'plugins': [
                'Combo.Core.Plugins.DemoPlugin'
            ],
            'plugin_auto_update': True
        }
        if not os.path.exists(self.combo_cfg_path):
            with open(self.combo_cfg_path, 'w', encoding='utf-8') as f:
                yaml.dump(obj, f)

    def plugins(self):
        if 'plugins' not in self.configs:
            return []
        return self.configs['plugins']

    def add_plugin(self, name):
        if name not in self.configs['plugins']:
            self.configs['plugins'].append(name)
            self.flush()

    def remove_plugin(self, name):
        if name in self.configs['plugins']:
            self.configs['plugins'].remove(name)
            self.flush()

    def plugin_auto_update(self, on):
        self.configs['plugin_auto_update'] = on
        self.flush()

    def plugin_path(self):
        if 'plugin_path' not in self.configs:
            return []
        return self.configs['plugin_path']

    def username(self):
        if 'username' not in self.configs or not self.configs['username']:
            # need input username
            username = input('you have not configure your name, please input your name:')
            self.configs['username'] = username
            self.flush()
        return self.configs['username']


