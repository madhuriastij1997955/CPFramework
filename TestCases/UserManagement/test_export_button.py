from PageObjects.LoginPage import loginData
from PageObjects.UserManagement import UserManagement_data
from Utilities.readProperties import configRead


class Test_ExportData:
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()
    def test_export_user_data(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        userMgmt=UserManagement_data(self.driver)
        userMgmt.export_data()
        loginpage.logout_app()