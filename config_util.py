import json
import yaml
import os

class ConfigLoader:
    """
    A utility class for loading a configuration file and fetching keys from it.
    Supports JSON and YAML formats.
    """
    def __init__(self, config_path):
        """
        Initializes the ConfigLoader with a configuration file.

        :param config_path: Path to the configuration file (JSON or YAML).
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file format is unsupported.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"The configuration file {config_path} does not exist.")

        self.config_data = self._load_config(config_path)

    def _load_config(self, config_path):
        """
        Loads the configuration file based on its format.

        :param config_path: Path to the configuration file.
        :return: Parsed configuration data.
        :raises ValueError: If the file format is unsupported.
        """
        _, ext = os.path.splitext(config_path)
        ext = ext.lower()

        if ext == ".json":
            with open(config_path, "r", encoding="utf-8") as file:
                return json.load(file)
        elif ext in [".yaml", ".yml"]:
            with open(config_path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported configuration file format. Use JSON or YAML.")

    def get(self, key, default=None):
        """
        Fetches the value for a given key in the configuration file.

        :param key: The key to fetch from the configuration data.
        :param default: The default value to return if the key is not found.
        :return: The value associated with the key, or the default value.
        """
        return self.config_data.get(key, default)
