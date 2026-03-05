from pages.admin_user_management.admin_user_management_page import AdminPage
import pytest
from time import sleep
import pytest_check as check

class TestAdminPage:

    def test_user_account_table(self, admin_page_driver):
        admin_page = AdminPage(admin_page_driver)
        admin_page.get_response_user_account_list()
        sleep(3)

    def aest_search_user_account(self, admin_page_driver):
        data = {
            "username": "Admin",
            "userRole": "Admin",
            "employeeName": "a",
            "status": "Enabled"
        }
        admin_page = AdminPage(admin_page_driver)
        admin_page.search_user_account(data["username"], data["userRole"], data["employeeName"], data["status"])
        sleep(3)


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
        admin_page.reset_search_form(data["username"], data["userRole"], data["employeeName"], data["status"])
        # Verify search form after pressing on reset button
        check.equal(admin_page.get_username(), "")
        check.equal(admin_page.get_user_role(), "-- Select --")
        check.equal(admin_page.get_employee_name(), "")
        check.equal(admin_page.get_status(), "-- Select --")



