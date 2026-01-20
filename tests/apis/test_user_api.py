import pytest
import pytest_check as check
from apis.user_api import UserApi


class TestApi:

    @pytest.mark.component_User
    def test_get_info_user(self):
        user_id = 1
        expected_user = {
            "id": user_id,
            "email": "Sincere@april.biz",
            "name": "Leanne Graham",
        }
        response = UserApi.get_user(user_id)
        assert response.status_code == 200
        response_data = response.json()
        check.equal(response_data["id"], expected_user["id"])
        check.equal(response_data["name"], expected_user["name"])
        check.equal(response_data["email"], expected_user["email"])

    def test_get_fetch_users(self):
        response = UserApi.get_all_users()
        assert response.status_code == 200
        response_data = response.json()
        check.equal(len(response_data), 10)
        user = next(user for user in response_data if user["id"] == 2)
        check.equal(user["name"], "Ervin Howell")
        check.equal(user["email"], "Shanna@melissa.tv")

    def test_create_user(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        response = UserApi.create_user(payload)
        assert response.status_code == 201
        response_data = response.json()
        check.equal(response_data["userId"], payload["userId"])
        check.equal(response_data["title"], payload["title"])
        check.equal(response_data["body"], payload["body"])