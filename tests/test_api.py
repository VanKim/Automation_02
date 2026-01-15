from utils.api_helper import ApiHelper
import pytest

@pytest.mark.api
class test_api:
    def test_get_fetch_users(path="/users/", params={"id": 1}):
        response = ApiHelper.get(path, params)
        print(f'{response}')
        #assert response["status_code"] == 200 
    
    



