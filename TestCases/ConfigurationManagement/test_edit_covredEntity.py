from PageObjects.ConfigurationManagement import Configurationmanagement
from PageObjects.LoginPage import loginData
from TestData.CP_TestData import CE_dropdownvalues, Pharamcy_types, Wholesaler_types
from Utilities.readProperties import configRead


class Test_editCE:
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()

    def test_edit_pendingCe_details(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        confMgr = Configurationmanagement(self.driver)
        confMgr.edit_ceDetails(confMgr.random_number(), "huTRuAbo", CE_dropdownvalues.CE3,
                                 confMgr.random_letter(), confMgr.random_number_NPI(), confMgr.random_letter(),
                                 confMgr.random_number(), Pharamcy_types.PH2, confMgr.random_number_NPI(),
                                 confMgr.random_letters(), Wholesaler_types.WH2, confMgr.random_number_NPI(),"44699770229","88700441414")
        loginpage.logout_app()