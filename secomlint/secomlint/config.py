import os

from secomlint.utils import read_config


class Config:
    def __init__(self, path=None, openai_key=None) -> None:
        self.rules_config_path = f"{os.path.dirname(os.path.abspath(__file__))}/config/rules.yml"
        self.openai_key_config_path = f"{os.path.dirname(os.path.abspath(__file__))}/config/openai-key"
        if path:
            self.default_rules = read_config(self.rules_config_path)
            self.new_rules = read_config(path)
            if self.new_rules:
                for rule in self.new_rules:
                    for element in self.new_rules[rule]:
                        self.default_rules[rule][element] = self.new_rules[rule][element]
        if openai_key:
            self.openai_key = openai_key

    def save_key(self):
        with open(self.openai_key_config_path, 'w') as f:
            f.write(f"OPENAI_KEY={self.openai_key}")
            
    def read_key(self):
        with open(self.openai_key_config_path) as f:
            self.openai_key = f.readlines()[0].split('=')[1]
