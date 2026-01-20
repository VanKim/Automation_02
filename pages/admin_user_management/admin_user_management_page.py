from pages.admin_user_management.admin_user_management_searching_form import SearchingForm
from pages.admin_user_management.admin_user_management_user_table import UserTable


class AdminPage(SearchingForm, UserTable):

    def __init__(self, driver):
        super().__init__(driver)
        
