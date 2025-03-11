import os
from pathlib import Path
from typing import Optional

from secomlint.utils import read_config


class Config:
    def __init__(self, path: Optional[str] = None, openai_key: Optional[str] = None) -> None:

        # Build paths in a cross-platform manner
        base_dir = Path(__file__).resolve().parent / "config"
        self.rules_config_path = base_dir / "rules.yml"
        #self.openai_key_config_path = base_dir / "openai-key"

        # Read the default rules if the file exists; fallback to empty dict
        self.default_rules = read_config(str(self.rules_config_path)) or {}

        # Merge new rules if a path is provided
        if path is not None:
            new_rules = read_config(path) or {}
            self._merge_rules(new_rules)

        # Optionally set or load an existing OpenAI key
        # if openai_key is not None:
        #     self.openai_key = openai_key
        # else:
        #     # If the key file exists, read it; otherwise set to None
        #     if self.openai_key_config_path.is_file():
        #         self.read_key()
        #     else:
        #         self.openai_key = None

        # if path:
        #     self.default_rules = read_config(self.rules_config_path)
        #     self.new_rules = read_config(path)
        #     if self.new_rules:
        #         for rule in self.new_rules:
        #             for element in self.new_rules[rule]:
        #                 self.default_rules[rule][element] = self.new_rules[rule][element]
        # if openai_key:
        #     self.openai_key = openai_key

    def _merge_rules(self, new_rules: dict) -> None:
        """
        Recursively merges new_rules into default_rules.
        """
        for rule, new_value in new_rules.items():
            if rule not in self.default_rules:
                self.default_rules[rule] = new_value
            else:
                old_value = self.default_rules[rule]
                if isinstance(old_value, dict) and isinstance(new_value, dict):
                    self._merge_rules_into(old_value, new_value)
                else:
                    self.default_rules[rule] = new_value

    def _merge_rules_into(self, base_dict: dict, new_dict: dict) -> None:
        """
        Helper function to recursively merge new_dict into base_dict.
        """
        for key, value in new_dict.items():
            if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
                self._merge_rules_into(base_dict[key], value)
            else:
                base_dict[key] = value

    def save_key(self) -> None:
        """
        Saves the current openai_key to the 'openai-key' file.
        Expects `self.openai_key` to hold the key string.
        """
        if not self.openai_key:
            raise ValueError("No OpenAI key to save.")
        with open(self.openai_key_config_path, 'w') as f:
            f.write(f"OPENAI_KEY={self.openai_key}")

    def read_key(self) -> None:
        """
        Reads the OpenAI key from the 'openai-key' file and sets self.openai_key.
        Expects the first line to be in the format: OPENAI_KEY=<value>
        """
        with open(self.openai_key_config_path, 'r') as f:
            line = f.readline().strip()
            if not line.startswith("OPENAI_KEY="):
                raise ValueError("Invalid OpenAI key format in file.")
            self.openai_key = line.split("=", 1)[1]
