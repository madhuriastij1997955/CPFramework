import allure
import pytest

from PageObjects.LoginPage import loginData
from PageObjects.User_Registration_Link import User_Registration
from TestData.CP_TestData import Security_QAs
from Utilities.BaseClass import BaseClass
from Utilities.readProperties import configRead


class Test_registration_link(BaseClass):
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()
    super_admin=configRead.get_uname()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(1)
    # @pytest.mark.dependency(depends=["test_login_to_app"])
    def test_login_to_app(self):
        user_reg=User_Registration(self.driver)
        mail=user_reg.add_user(Security_QAs.FName,Security_QAs.LName,user_reg.super_admin,"Super Admin")
        user_reg.registration_link(Security_QAs.QA3,Security_QAs.QA5,Security_QAs.Ans1,Security_QAs.Ans2,Security_QAs.password,mail)


