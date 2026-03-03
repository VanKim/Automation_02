from apis.user_account_apis import UserAccountApis
import pytest
import pytest_check as check
from utils.data_reader import DataReader
from jsonschema import validate

@pytest.mark.api_testing
class TestUserAccountListSearchingApi:

    def test_search_on_user_account_list_schema_validation(self):
        search_parameter= {
            "limit": 50,
            "offset": 0,
            "username": "Admin",
            "userRoleId": 1,
            "status": 1,
            "sortField": "r.displayName",
            "sortOrder": "ASC"
        }
        schema = DataReader.read_data_from_json_file('./testdata/apis/user_account_list_search/response_schema.json')
        response = UserAccountApis.user_account_list_search(search_parameter)
        assert response.status_code == 200
        # Compare response.body (instance) with schema
        validate(instance=response.json(), schema=schema)


    test_data = DataReader.read_data_from_json_file('./testdata/apis/user_account_list_search/search_parameters.json')
    @pytest.mark.parametrize("search_parameters", test_data)
    def test_search_on_user_account_list_exist_resource(self, search_parameters):
        response = UserAccountApis.user_account_list_search(search_parameters)
        assert response.status_code == 200
        response = response.json()
        # Currently, Tester doesn't have DB information. So , I'll compare between response and some hard value
        # Sorting by search_parameters["sortField"]
        sorted_response = None
        if search_parameters["sortOrder"].lower() == "desc":
            sorted_response = sorted(response["data"], key=lambda item:item[search_parameters["sortField"].split(".")[1]].lower(), reverse=True)
        elif search_parameters["sortOrder"].lower() == "asc":
            sorted_response = sorted(response["data"], key= lambda item:item[search_parameters["sortField"].split(".")[1]].lower(), reverse=False)
        # Verify response
        # Compare response with sorted_response
        check.equal(response["data"], sorted_response)
        # Verify total -> I don't know verify response which value?? >> skip

    def test_search_on_user_account_list_zero_resource(self):
        search_parameter = {
            "limit": 50,
            "offset": 0,
            "username": "Adminfgfhfhgfh",
            "userRoleId": 1,
            "status": 1,
            "sortField": "r.displayName",
            "sortOrder": "ASC"
            }
        response = UserAccountApis.user_account_list_search(search_parameter)
        assert response.status_code == 200
        response = response.json()
        # Verify response
        check.equal(response["data"], [])
        check.equal(response["meta"]["total"], 0)
        check.equal(response["rels"], [])

    def test_search_on_user_account_list_invalid_data(self):
        search_parameter = {
            "limit": 50,
            "offset": 0,
            "username": "Admin",
            "userRoleId": 300,
            "status": 100,
            "sortField": "r.displayName",
            "sortOrder": "ASC"
            }
        response = UserAccountApis.user_account_list_search(search_parameter)
        assert response.status_code == 422
        response = response.json()
        # Verify response
        check.equal(response["error"]["status"],'422')
        check.equal(response["error"]["message"],'Invalid Parameter')
        check.equal(response["error"]["data"]["invalidParamKeys"][0], 'status')




