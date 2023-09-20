from PageObjects.ConfigurationManagement import Configurationmanagement
from PageObjects.LoginPage import loginData

from TestData.CP_TestData import CE_dropdownvalues, Pharamcy_types, Wholesaler_types
from Utilities.readProperties import configRead


class Test_add_CE:
    uname = configRead.get_uname()
    pwd = configRead.get_pwd()

    def test_add_CovredEntity(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        confMgr = Configurationmanagement(self.driver)
        confMgr.add_covredEntity(confMgr.random_number(), confMgr.random_letters(), CE_dropdownvalues.CE1,
                                 confMgr.random_letter(), confMgr.random_number_NPI(), confMgr.random_letter(),
                                 confMgr.random_number(), Pharamcy_types.PH1, confMgr.random_number_NPI(),
                                 confMgr.random_letters(), Wholesaler_types.WH1, confMgr.random_number_NPI())
        loginpage.logout_app()

    def test_search_CE(self):
        loginpage = loginData(self.driver)
        loginpage.user_login(self.uname, self.pwd)
        confMgr = Configurationmanagement(self.driver)
        confMgr.search_ce("huTRuAbo","6874932","Federally Qualified Health Center (FQHC)")
        loginpage.logout_app()


