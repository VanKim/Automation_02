from utils.api_helper import ApiHelper
class UserApi:
    @staticmethod
    def get_user(user_id):
        return ApiHelper.get(f'/users/{user_id}')

    @staticmethod
    def get_all_users():
        return ApiHelper.get('/users')

    @staticmethod
    def create_user(payload):
        return ApiHelper.post('/posts/', payload)


