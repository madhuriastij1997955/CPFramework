import allure
import pytest

from PageObjects.LoginPage import loginData
from PageObjects.UserManagement import UserManagement_data
from PageObjects.User_Registration_Link import User_Registration
from TestData.CP_TestData import Security_QAs
from Utilities.BaseClass import BaseClass
from Utilities.readProperties import configRead


# @pytest.mark.usefixtures("setUp")
class Test_Edit_user(BaseClass):
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.order(5)
    def test_edit_users(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        txt = User_Registration(self.driver).random_email()
        usermgmt = UserManagement_data(self.driver)
        usermgmt.edit_user("3xh8a@mailinator.com", "3xh8a@mailinator.com	", "FName" + txt, "LName" + txt,"Pharmacy User")

        loginpage.logout_app()
