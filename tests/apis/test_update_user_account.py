from apis.user_account_apis import UserAccountApis
import pytest
import pytest_check as check
from utils.data_reader import DataReader
from jsonschema import validate
import json

@pytest.mark.api_testing
class TestUpdateUserAccountApi:

    def test_update_user_account_schema_validation(self):
        request_schema = DataReader.read_data_from_json_file(
            './testdata/apis/update_user_account/request_schema.json')
        response_schema = DataReader.read_data_from_json_file(
            './testdata/apis/update_user_account/response_schema.json')
        user_id = 54
        payload = {
            "changePassword": False,
            "empNumber": 137,
            "password": "",
            "status": True,
            "userRoleId": 2,
            "username": "FMLName EDIT1"
        }
        response = UserAccountApis.update_user_account(payload, user_id)
        assert response.status_code == 200
        validate(instance=json.loads(response.request.body.decode('utf-8')), schema=request_schema)
        validate(instance=response.json(), schema=response_schema)

    def test_update_user_account_success(self):
        user_id = 54
        payload={
                "changePassword": False,
                "empNumber": 137,
                "password": "",
                "status": True,
                "userRoleId": 2,
                "username": "FMLName EDIT1"
        }
        response = UserAccountApis.update_user_account(payload, user_id)
        assert response.status_code == 200
        response = response.json()
        check.equal(response["data"]["changePassword"], False)
        # Verify comparing response with payload
        check.equal(response["data"]["id"], user_id)
        check.equal(response["data"]["userName"], payload["username"])
        check.equal(response["data"]["status"], payload["status"])
        check.equal(response["data"]["empNumber"], payload["empNumber"])
        check.equal(response["data"]["userRole"]["userRoleId"], payload["id"])

    def test_update_user_account_change_password_success(self):
        user_id = 54
        payload={
                "changePassword": True,
                "empNumber": 137,
                "password": "admin123",
                "status": True,
                "userRoleId": 2,
                "username": "FMLName EDIT1"
        }
        response = UserAccountApis.update_user_account(payload, user_id)
        assert response.status_code == 200
        response = response.json()
        print(response)
        # Verify comparing response with payload
        check.equal(response["data"]["id"], user_id)
        check.equal(response["data"]["userName"], payload["username"])
        check.equal(response["data"]["status"], payload["status"])
        check.equal(response["data"]["employee"]["empNumber"], payload["empNumber"])
        check.equal(response["data"]["userRole"]["userRoleId"], payload["id"])

    def test_update_user_account_invalid_format_data(self):
        user_id = 54
        payload = {
            "changePassword": "false",
            "empNumber": "abc",
            "password": "",
            "status": "True",
            "userRoleId": 2,
            "username": "FMLName EDIT1"
        }
        response = UserAccountApis.update_user_account(payload, user_id)
        assert response.status_code == 422
        response = response.json()
        # Verify response
        check.equal(response["error"]["status"], '422')
        check.equal(response["error"]["message"], 'Invalid Parameter')
        check.equal(response["error"]["data"]["invalidParamKeys"],['changePassword', 'empNumber', 'status'] )

