from pages.admin_user_management.admin_user_management_page import AdminPage
import pytest
#from apis.hrm_user_api import HRMUserApi


class AdminPage:
    def test_select_custom_dropdown(self, admin_page_driver):
        admin_page = AdminPage(admin_page_driver)
        admin_page.select_user_role_dropdown("Admin")
        assert admin_page.get_user_role_item() == "Admin"
    
    def test_redirect_adding_form(self, admin_page_driver):
        admin_page = AdminPage(admin_page_driver)
        admin_page.click_on_add_button()
        assert admin_page_driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser'
    
    def test_searching_with_user_role(self, admin_page_driver):
        admin_page = AdminPage(admin_page_driver)
        admin_page.select_user_role_dropdown("Admin")
        admin_page.click_on_search_button()
        #response = HRMUserApi.get_all_users(admin_page_driver)
        #print(response.url, response.headers)
        #assert response.status_code == 200
        assert  admin_page.get_total_number_user() == 10

