import allure
import pytest

from PageObjects.LoginPage import loginData
from PageObjects.UserManagement import UserManagement_data
from Utilities.readProperties import configRead


class Test_pagination_table:
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.order(5)
    def test_verify_pagination_table(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        usermgmt = UserManagement_data(self.driver)
        usermgmt.pagination_table("39l7gyp3n3@mailinator.com")
        loginpage.logout_app()
