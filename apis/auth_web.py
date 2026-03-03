from utils.config_reader import ConfigReader
import re
import requests

class AuthWeb:
    # Orange HRM is web session authentication, not API authentication
    # 1st Login to get CSRF token
    # 2nd Validate CSRF token & username/ password
    @staticmethod
    def get_cookies():
        session = requests.Session()
        response = session.get(f'{ConfigReader.get_base_url()}/web/index.php/auth/login', timeout=10)
        token = re.search(r':token="&quot;(.*?)&quot;"', response.text).group(1)
        session.post(f'{ConfigReader.get_base_url()}/web/index.php/auth/validate',
                                 {"_token": f'{token}', "username": f'{ConfigReader.get_username()}', "password": f'{ConfigReader.get_password()}'}, timeout=10)
        return session.cookies


