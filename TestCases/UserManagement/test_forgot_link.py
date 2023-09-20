import allure
import pytest

from PageObjects.UserManagement import UserManagement_data
from PageObjects.User_Registration_Link import User_Registration
from TestData.CP_TestData import Security_QAs
from Utilities.BaseClass import BaseClass


class Test_Forgot_link(BaseClass):

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.order(4)
    def test_forgot_link(self):
        txt = User_Registration(self.driver).random_email()
        user_reg = User_Registration(self.driver)
        mail = user_reg.add_user(Security_QAs.FName, Security_QAs.LName, user_reg.super_admin, "Super Admin")
        user_reg.registration_link(Security_QAs.QA3, Security_QAs.QA5, Security_QAs.Ans1, Security_QAs.Ans2,
                                   Security_QAs.password, mail)
        usermgmt=UserManagement_data(self.driver)
        usermgmt.forgot_link(mail,Security_QAs.QA3, Security_QAs.QA5,Security_QAs.Ans1, Security_QAs.Ans2,Security_QAs.password+txt)


