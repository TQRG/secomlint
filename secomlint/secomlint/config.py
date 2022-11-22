import os

from secomlint.utils import read_config


class Config:
    def __init__(self, path=None) -> None:
        self.config_path = f"{os.path.dirname(os.path.abspath(__file__))}/config/rules.yml"
        self.default_rules = read_config(self.config_path)
        if path:
            self.new_rules = read_config(path)
            if self.new_rules:
                for rule in self.new_rules:
                    for element in self.new_rules[rule]:
                        self.default_rules[rule][element] = self.new_rules[rule][element]
