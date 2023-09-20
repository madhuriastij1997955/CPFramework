import allure
import pytest
import softest

from PageObjects.LoginPage import loginData

from Utilities.BaseClass import BaseClass
from Utilities.readProperties import configRead


class Test_Login_page(BaseClass):
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()

    def test_logn_page_UI_details(self):
        loginpage = loginData(self.driver)
        loginpage.loginpage_UI_elements()

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.order(0)
    @pytest.mark.dependency()
    def test_login_to_app(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        loginpage.logout_app()

    def test_login_datadriven(self):
        loginpage = loginData(self.driver)
        loginpage.logindata_driven_XL("\\old data\\CP StarterKIT AutomationLatest\\TestData\LoginData.xlsx",
                                      "LoginData")
