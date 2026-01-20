from utils.config_reader import ConfigReader
from pages.admin_user_management.admin_user_management_searching_form import SearchingForm
from pages.admin_user_management.admin_user_management_user_table import UserTable
from apis.hrm_user_api import HRMUserApi

class TestAdminPage:
    '''def test_select_custom_dropdown(self, admin_page_driver):
        searching_form = SearchingForm(admin_page_driver)
        searching_form.select_user_role_dropdown("Admin")
        assert  searching_form.get_user_role_item() == "Admin"
    '''
    '''def test_redirect_adding_form(self, admin_page_driver):
        user_table = UserTable(admin_page_driver)
        user_table.click_on_add_button()
        assert admin_page_driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser'
    '''
    def test_searching_with_user_role(self, admin_page_driver):
        searching_form = SearchingForm(admin_page_driver)
        searching_form.select_user_role_dropdown("Admin")
        searching_form.click_on_search_button()
        user_table = UserTable(admin_page_driver)
        #response = HRMUserApi.get_all_users(admin_page_driver)
        #print(response.url, response.headers)
        #assert response.status_code == 200
        #assert  user_table.get_total_number_user() == 10

