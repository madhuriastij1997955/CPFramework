import allure
import pytest

from PageObjects.LoginPage import loginData
from PageObjects.UserManagement import UserManagement_data
from Utilities.BaseClass import BaseClass
from Utilities.readProperties import configRead


class Test_view_user(BaseClass):
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()

    @pytest.mark.smoke
    @pytest.mark.order(6)
    @allure.severity(allure.severity_level.NORMAL)
    def test_view_user(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        usermgt=UserManagement_data(self.driver)
        usermgt.view_user_details("wkdm1@mailinator.com")
        loginpage.logout_app()