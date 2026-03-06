from pages.admin_user_management.admin_user_management_page import AdminPage
import pytest
from time import sleep
import pytest_check as check
from utils.data_reader import DataReader
from pages.admin_user_management.add_user_account_form import AddingUserForm

class TestAdminPage:



    def aest_add_user_account(self, admin_page_driver):
        data = {
            "infor": {
            "userName": "vfwwwq11",
            "userRole": "Admin",
            "employeeName": "van tht",
            "status": "Enabled"
            },
            "password": "admin123",
            "confirmPassword": "admin123"
        }
        admin_page = AdminPage(admin_page_driver)
        #### Before adding user
        # Get user account list table
        before_result_table = admin_page.get_user_account_list_table()
        before_total_records = len(before_result_table)
        # Get total number records in total_records_label string
        before_total_records_label = admin_page.get_total_records_label()
        admin_page.add_button()
        assert 'admin/saveSystemUser' in admin_page_driver.current_url
        adding_user_form = AddingUserForm(admin_page_driver)
        adding_user_form.add_user(data)
        admin_page.current_url('/admin/viewSystemUsers')

        ##### Aftering adding successfully
        # Get user account list table
        after_result_table = admin_page.get_user_account_list_table()
        after_total_records = len(after_result_table)
        # Get total number records in total_records_label string
        after_total_records_label = admin_page.get_total_records_label()
        # Compare past result with current result
        check.equal(after_total_records, after_total_records_label)
        check.equal(before_total_records, after_total_records -1)
        check.equal(before_total_records_label, after_total_records_label -1)
        result_flag = False
        for i in range(0, after_total_records):
            record = admin_page.get_data_for_a_user_account_record(after_result_table[i])
            if record == data["infor"]:
                result_flag = True
                break
        check.is_true(result_flag)

    @pytest.mark.parametrize("data", DataReader.read_data_from_json_file('./testdata/ui/admin_page/searching_form.json'))
    def aest_search_user_account_table(self, admin_page_driver, data):
        admin_page = AdminPage(admin_page_driver)
        # Search user account list
        admin_page.search_user_account(data["username"], data["userRole"], data["employeeName"], data["status"])
        # Get response body from logs of browser
        expected_user_list = admin_page.get_response_user_account_list(data["endpoint"])
        sleep(5)
        # Get user account list table
        result_table = admin_page.get_user_account_list_table()
        total_records = len(result_table)
        # Get total number records in total_records_label string
        total_records_label = admin_page.get_total_records_label()

        # Compare total records between UI and response
        assert total_records == total_records_label == expected_user_list["meta"]["total"]

        if total_records > 0:
            i = None
            # Get expected record from response to compare with data in result table UI
            expected_record = {
                "userName": expected_user_list["data"][total_records-1]["userName"],
                "userRole": expected_user_list["data"][total_records-1]["userRole"]["displayName"],
                "employeeName": expected_user_list["data"][total_records-1]["employee"]["firstName"] + " " + expected_user_list["data"][total_records-1]["employee"]["lastName"],
                "status": 'Enabled' if expected_user_list["data"][total_records-1]["status"] else 'Disabled'
            }
            result_flag = False
            for i in range(0, total_records):
                actual_record = admin_page.get_data_for_a_user_account_record(result_table[i])
                if expected_record == actual_record:
                    result_flag = True
                    break
            check.is_true(result_flag)
        else:
            assert total_records_label == 0



    def aest_search_form_reset_data(self, admin_page_driver):
        data = {
            "username": "Admin",
            "userRole": "Admin",
            "employeeName": "a",
            "status": "Enabled"
        }
        # Login OrangeHRM and then go to Admin page
        admin_page = AdminPage(admin_page_driver)
        # Input và Reset data on search from
        admin_page.reset_search_form( data["username"], data["userRole"], data["employeeName"], data["status"])
        # Verify search form after pressing on reset button
        check.equal(admin_page.get_username(), "")
        check.equal(admin_page.get_user_role(), "-- Select --")
        check.equal(admin_page.get_employee_name(), "")
        check.equal(admin_page.get_status(), "-- Select --")



