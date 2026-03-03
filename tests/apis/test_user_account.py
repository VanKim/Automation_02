from apis.user_account_apis import UserAccountApis
import pytest
import pytest_check as check
from utils.data_reader import DataReader
from jsonschema import validate

@pytest.mark.api_testing
class TestUserAccountApi:

    def test_get_user_account_response_schema_validation(self):
        # Tester is self-designing for the mock web by using AI. I don't have Response schema exactly.
        schema = DataReader.read_data_from_json_file('./testdata/apis/get_user_account/response_schema.csv')
        user_id = 1
        response = UserAccountApis.get_user_account(user_id)
        assert response.status_code == 200
        # Compare response.body (instance) with schema
        validate(instance=response.json(), schema=schema)

    def test_get_user_account_exist_resource(self):
        user_id = 1
        response = UserAccountApis.get_user_account(user_id)
        assert response.status_code == 200
        response = response.json()
        # Verify response with the information in DB
        # Currently, Tester doesn't have DB information => compare between response and hard value
        check.equal(response["data"]["id"],1 )
        check.equal(response["data"]["userName"], "Admin")
        check.equal(response["data"]["userRole"]["id"], 1)
        check.equal(response["data"]["employee"]["empNumber"],7)

    def test_get_user_account_not_found_resource(self):
        user_id = 1000
        response = UserAccountApis.get_user_account(user_id)
        assert response.status_code == 404
        response = response.json()
        # Verify response body
        check.equal(response["error"]["status"], "404")
        check.equal(response["error"]["message"], "Record Not Found")

    def test_get_user_account_missing_user_id_param(self):
        response = UserAccountApis.get_user_account(None)
        assert response.status_code == 422
        response = response.json()
        # Verify response body
        check.equal(response["error"]["status"], "422", msg="invalid status code")
        check.equal(response["error"]["message"], "Invalid Parameter", msg="invalid message")
        check.equal(response["error"]["data"]["invalidParamKeys"][0], "id", msg="invalid ParamKeys")
