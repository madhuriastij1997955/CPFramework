import time

import softest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
from Utilities.readProperties import configRead

from Utilities.XLUtils import XL_operations


class loginData(BaseClass):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    cp_url = configRead.get_url()

    contract_pharmacy_title = (By.XPATH, "//strong[text()='Contract Pharmacy']")
    stater_kit_title = (By.XPATH, "//strong[text()='STARTER KIT']")
    cp_banner_image = (By.XPATH, "//img[@alt='cpbanner']")
    cp_welecome_title = (By.XPATH, "//strong[text()='Welcome!']")
    cp_signin_title = (By.XPATH, "//strong[text()='Sign in']")
    usname_label_txt = (By.XPATH, "//label[@title='Username/Email ID']")
    uname_txtbox = (By.XPATH, "//input[@id='normal_login_username']")
    uname_txtbox_icon = (By.XPATH, "//span[@aria-label='user']")
    pwd_label_txt = (By.XPATH, "//label[@title='Password']")
    pwd_txtbox = (By.XPATH, "//input[@id='normal_login_password']")
    remember_checkbox = (By.XPATH, "//input[@class='ant-checkbox-input']/parent::span")
    remember_label_txt = (By.XPATH, "//span[text()='Remember me']")
    forgot_pwd_link = (By.XPATH, "//span[text()='Forgot Password?']/parent::button")
    login_btn = (By.XPATH, "//span[text()='Login']/parent::button")
    # mailnator info
    mailnator_url = "https://www.mailinator.com/"
    mailnator_search = (By.ID, "search")
    mailnator_go_btn = (By.XPATH, "//button[text()='GO']")
    cp_otp_uname = (By.XPATH, '//strong[contains(text(),"Hi, ")]')
    mailnator_row_otp = (By.XPATH,
                         "//table[@class='table-striped jambo_table']/tbody/tr/td[3 and contains(text(),'Your login verification - One Time Password (OTP)')] ")
    # otp_frame = "//iframe[@id='html_msg_body']"
    otp_text = (By.XPATH, "//p[contains(text(),'To log into the application, please enter the One Time Password (OTP) "
                          "provided: OTP: ')]")
    otp_txt1 = (By.XPATH, "//input[@aria-label='Please enter OTP character 1']")
    otp_txt2 = (By.XPATH, "//input[@aria-label='Please enter OTP character 2']")
    otp_txt3 = (By.XPATH, "//input[@aria-label='Please enter OTP character 3']")
    otp_txt4 = (By.XPATH, "//input[@aria-label='Please enter OTP character 4']")
    otp_txt5 = (By.XPATH, "//input[@aria-label='Please enter OTP character 5']")
    otp_txt6 = (By.XPATH, "//input[@aria-label='Please enter OTP character 6']")
    verify_btn = (By.XPATH, "//span[text()='Verify']/parent::button")
    otp_success_text = (By.XPATH, "//span[text()='A One Time Password has been sent to your registered Email ID']")
    encora_logo = (By.XPATH, "//img[@class='app-logo']")
    invalid_username = (By.XPATH, "//b[contains(text(),'Invalid Username. Please try again.')]")
    logout_profile = (By.XPATH, "//span[@class='ant-avatar-string']/parent::span")
    logout_icon = (By.XPATH, "//span[contains(text(),'Logout')]")

    def loginpage_UI_elements(self):
        self.driver.get(self.cp_url)
        self.verify_element_displayed(self.contract_pharmacy_title)
        self.verify_element_displayed(self.stater_kit_title)
        self.verify_element_displayed(self.cp_banner_image)
        self.verify_element_displayed(self.cp_welecome_title)
        self.verify_element_displayed(self.cp_signin_title)
        self.verify_element_displayed(self.usname_label_txt)
        self.verify_element_displayed(self.uname_txtbox)
        self.verify_element_displayed(self.pwd_txtbox)
        self.verify_element_displayed(self.pwd_label_txt)
        self.verify_element_displayed(self.remember_checkbox)
        self.verify_element_displayed(self.remember_label_txt)
        self.verify_element_displayed(self.forgot_pwd_link)
        self.verify_element_displayed(self.login_btn)

    def user_login(self, uname, pwd):
        self.uname = uname
        print(self.cp_url)
        logger = self.log_gen()
        logger.info(self.cp_url)
        self.driver.get(self.cp_url)
        window_handles = self.driver.current_window_handle
        self.send_keys(self.uname_txtbox, uname)
        self.send_keys(self.pwd_txtbox, pwd)
        self.click_element(self.login_btn)
        time.sleep(1.0)
        otp_msg = self.return_text(self.otp_success_text)
        logger.info(otp_msg)
        print(type(otp_msg))
        self.soft_assert(self.assertEqual, otp_msg, "A One Time Password has been sent to your registered Email ID",
                         "otp txt is failed")
        # assert otp_msg == "A One Time Password has been sent to your registered Email ID"
        logger.info(otp_msg)
        logger.info("Otp is generated")
        time.sleep(2.0)
        self.driver.switch_to.new_window(Keys.CONTROL + 't')
        self.read_otp_mailnator(self.uname, window_handles)
        self.assert_all("asserations are failed")

    def read_otp_mailnator(self, username, parent_window):
        self.driver.get(self.mailnator_url)
        time.sleep(2.0)
        self.send_keys(self.mailnator_search, username)
        time.sleep(1.0)
        self.click_element(self.mailnator_go_btn)
        time.sleep(2.0)
        self.click_element(self.mailnator_row_otp)
        self.driver.switch_to.frame("html_msg_body")
        otp_txt = self.return_text(self.otp_text)
        self.driver.close()
        otp_list = otp_txt.split("OTP:")
        otp = otp_list[1]  # 456665
        otp_nums = list(otp)
        print(type(otp_list))
        print(otp_list)
        self.driver.switch_to.window(parent_window)
        time.sleep(1.0)
        # self.send_keys(self.otp_txt1, otp[1])
        # self.send_keys(self.otp_txt2, otp[2])
        # self.send_keys(self.otp_txt3, otp[3])
        # self.send_keys(self.otp_txt4, otp[4])
        # self.send_keys(self.otp_txt5, otp[5])
        # self.send_keys(self.otp_txt6, otp[6])
        for r in range(1, otp_nums.__len__()):
            Xpath_opt_txt_box = "//input[@aria-label='Please enter OTP character " + str(r) + "']"
            locator = (By.XPATH, Xpath_opt_txt_box)
            self.send_keys(locator, otp_nums[r])

        self.click_element(self.verify_btn)
        time.sleep(2.0)
        self.verify_element_displayed(self.encora_logo)
        self.log_gen().info("encora log")

    def logout_app(self):
        self.click_element(self.logout_profile)
        time.sleep(1.5)
        self.move_to_element(self.logout_icon)
        time.sleep(0.5)
        self.javascripit_click(self.logout_icon)

    def logindata_driven_XL(self, path, sheetname):
        xl_actions = XL_operations()
        rows_count = xl_actions.GetRows_count(path, sheetname)
        cols_count = xl_actions.GetColumns_count(path, sheetname)
        print(rows_count, cols_count)

        for r in range(2, rows_count + 1):
            username = xl_actions.ReadData_from_XL(path, sheetname, r, 1)
            password = xl_actions.ReadData_from_XL(path, sheetname, r, 2)
            try:
                self.user_login(username, password)
                self.logout_app()
                xl_actions.WriteData_from_XL(path, sheetname, r, 3, "Pass")
                xl_actions.Fill_greenencolor(path, sheetname, r, 3)

            except:
                xl_actions.WriteData_from_XL(path, sheetname, r, 3, "Fail")
                xl_actions.Fill_redencolor(path, sheetname, r, 3)
