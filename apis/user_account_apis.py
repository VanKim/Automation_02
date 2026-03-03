from utils.api_helper import ApiHelper
from apis.auth_web import AuthWeb

class UserAccountApis:

    # Get an user account on OrangeHRM
    @staticmethod
    def get_user_account(user_id):
        return ApiHelper.get(f'admin/users/{user_id}', None, cookies=AuthWeb.get_cookies(), timeout=10)

    # Searching on users account list with search parameters
    @staticmethod
    def user_account_list_search(search_parameters):
        return ApiHelper.get(f'admin/users', params= search_parameters, cookies=AuthWeb.get_cookies(),timeout=10)

    # Registers an user account login on OrangeHRM
    @staticmethod
    def create_user_account(payload):
        return ApiHelper.post(f'admin/users/', payload, cookies=AuthWeb.get_cookies(),timeout=10)

    # Delete user account login on OrangeHRM
    @staticmethod
    def delete_user_account(user_id):
        return ApiHelper.delete(f'admin/users/', user_id, cookies=AuthWeb.get_cookies(),timeout=10)

    # Update the information of an user account login on OrangeHRM
    @staticmethod
    def update_user_account(payload, user_id):
        return ApiHelper.put(f'admin/users/{user_id}', payload, cookies=AuthWeb.get_cookies(),timeout=10)


