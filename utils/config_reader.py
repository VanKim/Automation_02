import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        """Load configuration from testsetting.json if not already loaded"""
        if ConfigReader._config is None:
            #os.path.abspath(__file__): get path của the current working file
            #os.path.dirname: process get path of folder
            #os.path.join....: concat path folder of the current config_reader.py + testsetting.json
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testsetting.json')
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config

    @staticmethod
    def get_base_url():
        """Get the base URL from the configuration"""
        return ConfigReader.load_config()['base_url']

    @staticmethod
    def get_username():
        """Get the username from the configuration"""
        return ConfigReader.load_config()['credentials']['username']

    @staticmethod
    def get_password():
        """Get the password from the configuration"""
        return ConfigReader.load_config()['credentials']['password']

    @staticmethod
    def get_implicit():
        """Get the implicit from the configuration"""
        return ConfigReader.load_config()['timeouts']['implicit']
