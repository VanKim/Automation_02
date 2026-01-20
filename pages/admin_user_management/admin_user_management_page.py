from pages.admin_user_management.admin_user_management_searching_form import AdminSearchingForm
from pages.admin_user_management.admin_user_management_user_table import AdminUserTable


class AdminPage(AdminSearchingForm, AdminUserTable):

    def __init__(self, driver):
        super().__init__(driver)
