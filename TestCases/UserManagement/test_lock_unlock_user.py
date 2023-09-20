import pytest

from PageObjects.UserManagement import UserManagement_data
from PageObjects.User_Registration_Link import User_Registration
from TestData.CP_TestData import Security_QAs


class Test_lock_unlock():

    # @pytest.mark.smoke
    def test_lock_unclock_user_login(self):
        user_reg = User_Registration(self.driver)
        mail = user_reg.add_user(Security_QAs.FName, Security_QAs.LName, user_reg.super_admin, "Super Admin")
        user_reg.registration_link(Security_QAs.QA3, Security_QAs.QA5, Security_QAs.Ans1, Security_QAs.Ans2,
                                    Security_QAs.password, mail)
        user_mgmt=UserManagement_data(self.driver)
        user_mgmt.lock_user_login_UI(3,mail,"Super Admin")




    # def test_lock_security_QAs(self):
    #     pass