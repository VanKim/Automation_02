from pygments.lexers import data

from pages.admin_user_management.admin_user_management_page import AdminPage
import pytest
from time import sleep
import pytest_check as check
from utils.data_reader import DataReader
from pages.admin_user_management.add_user_account_form import AddingUserForm

@pytest.mark.functional
class TestAdminPage:
    @pytest.mark.parametrize("data", DataReader.read_data_from_json_file('./testdata/ui/admin_page/navigation.json'))
    # Test Header Navigation
    def test_a_navigation_tab(self, admin_page_driver, data):
        print(f'[DEBUG]ADMIN - CURRENT: {admin_page_driver.current_url}')
        print(f'[DEBUG] DRIVER: {admin_page_driver}\n')
        print(f'[DEBUG] Data: {data}\n')
        print(f'[DEBUG]PAGESOURCE: {admin_page_driver.page_source}\n\n')
        admin_page = AdminPage(admin_page_driver)
        key, value =  list(data["option"].items())[0]
        # Get nav_list
        nav_list = admin_page.get_navigation_list()
        print(f'[DEBUG]nav_list: {nav_list}')
        assert len(nav_list) != 0, "navigation list is empty"
        # Get nav_tab correspond with data["name"]
        nav_tab = admin_page.get_navigation_tab(nav_list, data["name"])
        print(f'[DEBUG]nav_tab: {nav_tab}')
        # Click nav_tab
        admin_page.open_option_list_nav_tab(nav_tab)
        # Get option list
        options = admin_page.get_option_list_of_nav_tab(nav_tab)
        if options:
            # Select option
            admin_page.select_option_of_a_navigation_tab(options, key)
        else:
            admin_page.click_on_navigation_tab(nav_tab)
        # Verify redirect to url correspond with the selected option
        admin_page.current_url(value)
        check.is_in(value, admin_page.get_current_url() )
        admin_page.back()
        admin_page.current_url('/admin/viewSystemUsers')
        check.is_in('/admin/viewSystemUsers',admin_page.get_current_url())

    def test_delete_user_account(self, admin_page_driver):
        admin_page = AdminPage(admin_page_driver)
        # Get user account list table before deleting user account
        before_result_table = admin_page.get_user_account_list_table()
        before_total_records = len(before_result_table)
        # Get total number records in total records label before deleting user account
        before_total_records_label = admin_page.get_total_records_label()
        if before_total_records > 0:
            delete_record= admin_page.get_data_for_a_user_account_record(before_result_table[before_total_records-1])
            # Press on delete action
            admin_page.delete_action(before_result_table[before_total_records-1])
            admin_page.confirm_delete_popup(True)

            # Get user account list table after deleted user account
            after_result_table = admin_page.get_user_account_list_table()
            after_total_records = len(after_result_table)
            # Get total number records in total records label after deleted user account
            after_total_records_label = admin_page.get_total_records_label()
            with check.check:
                assert after_total_records == after_total_records_label
                assert after_total_records == (before_total_records-1)
                assert after_total_records_label == (before_total_records_label - 1)
            # Verify deleted record
            for i in range(0, after_total_records):
                record = admin_page.get_data_for_a_user_account_record(after_result_table[i])
                if record == delete_record:
                    check.is_true(False, "deleted record still exists on result table ")
                    break
        else:
            assert before_total_records_label == 0

    def aest_add_user_account(self, admin_page_driver):
        data = {
            "infor": {
            "userName": "vvvwwq11",
            "userRole": "Admin",
            "employeeName": "van tht",
            "status": "Enabled"
            },
            "password": "admin123",
            "confirmPassword": "admin123"
        }
        admin_page = AdminPage(admin_page_driver)

        # Get user account list table before adding user account
        before_result_table = admin_page.get_user_account_list_table()
        before_total_records = len(before_result_table)
        # Get total number records in total_records_label before adding user account
        before_total_records_label = admin_page.get_total_records_label()
        # Press on Add button
        admin_page.add_button()
        # Redirect to the adding user account page
        assert 'admin/saveSystemUser' in admin_page_driver.current_url
        adding_user_form = AddingUserForm(admin_page_driver)
        adding_user_form.add_user(data)
        admin_page.current_url('/admin/viewSystemUsers')

        # Get user account list table after added user account
        after_result_table = admin_page.get_user_account_list_table()
        after_total_records = len(after_result_table)
        # Get total number records in total_records_label after added user account
        after_total_records_label = admin_page.get_total_records_label()

        # Compare past result with current result
        check.equal(after_total_records, after_total_records_label)
        check.equal(before_total_records, after_total_records-1)
        check.equal(before_total_records_label, after_total_records_label-1)
        # Verify added record
        result_flag = False
        for i in range(0, after_total_records):
            record = admin_page.get_data_for_a_user_account_record(after_result_table[i])
            if record == data["infor"]:
                result_flag = True
                break
        check.is_true(result_flag, "added record != expected record")

    @pytest.mark.parametrize("data", DataReader.read_data_from_json_file('./testdata/ui/admin_page/searching_form.json'))
    def test_search_user_account_table(self, admin_page_driver, data):
        admin_page = AdminPage(admin_page_driver)
        # Search user account list
        admin_page.search_user_account(data["username"], data["userRole"], data["employeeName"], data["status"])

        #### Before searching user account list
        # Get response body from logs of browser
        expected_user_list = admin_page.get_response_user_account_list(data["endpoint"])
        # Get user account list table
        result_table = admin_page.get_user_account_list_table()
        total_records = len(result_table)
        # Get total number records in total_records_label string
        total_records_label = admin_page.get_total_records_label()

        # Compare total records between UI and response
        assert total_records == total_records_label == expected_user_list["meta"]["total"]
        if total_records > 0:
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
            check.is_true(result_flag, "expected record != actual record")
        else:
            assert total_records_label == 0

    def test_search_form_reset_data(self, admin_page_driver):
        data = {
            "username": "Admin",
            "userRole": "Admin",
            "employeeName": "anhgkg",
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



