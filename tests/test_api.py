from utils.api_helper import ApiHelper
import pytest
import pytest_check as check

@pytest.mark.api
class TestApi:
    def test_get_info_user(self,path ='/users/', params={"id": "1"}):
        response = ApiHelper.get(self,path, params)
        #print(response.json(), response.headers, response.status_code)
        response_data = response.json()
        assert check.equal(response.status_code, 200)
        assert check.equal(response_data["id"], 1)
        assert check.equal(response_data["name"], "Leanne Graham")
        assert check.equal(response_data["email"], "Sincere@april.biz")

    def test_get_fetch_users(self, path='/users/'):
        response = ApiHelper.get(self, path)
        response_data = response.json()
        assert check.equal(response.status_code, 200)
        for user in response_data:
            if user["id"] == 2:
                assert check.equal(user["name"], "Ervin Howell")
                assert check.equal(user["email"], "Shanna@melissa.tv")
                break
    



