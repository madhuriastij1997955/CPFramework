import random
import string
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import loginData

from Utilities.BaseClass import BaseClass
from Utilities.readProperties import configRead


class User_Registration(BaseClass):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    usermanagemenr_module = (By.XPATH, "//li[@modulename='UserManagement']")
    add_user_main_btn = (By.XPATH, "//span[text()=' Add User']/parent::button")
    user_role_drpdwn = (By.XPATH, "//input[@id='addce_userRole']")
    super_admin = (By.XPATH, "//div[text()='Super Admin']")
    # standard_user = (By.XPATH, "//div[text()='Standard User']")
    first_name_txt = (By.ID, "addce_firstName")
    last_name_txt = (By.ID, "addce_lastName")
    email_txt = (By.ID, "addce_emailId")
    username_txt = (By.ID, "addce_userName")
    add_user_btn = (By.XPATH, "//span[text()='Add User']/parent::button")
    time.sleep(0.5)
    save_next_btn = (By.XPATH, "//span[text()='Save & Next']/parent::button")
    add_user_msg = (By.XPATH, "//span[text()='User added successfully!']")
    confirm_btn = (By.XPATH, "//span[text()='Confirm']/parent::button")
    new_user_added_msg = (By.XPATH, "//span[text()='New User is successfully added!']")
    mailnator_reglink_row = (By.XPATH, "//table[@class='table-striped jambo_table']/tbody/tr[1]/td[3 and contains(text("
                                       "),'Welcome to Contract Pharmacy Application – Please Log In')]")
    mailnator_reg_link = (By.XPATH, "//a[contains(text(),'https://cpframework-qa.excellarate.com/register?')]")

    # set password screen
    security_qa_title = (By.XPATH, "//strong[text()='Set the following Security Questions']")
    question1_dropdwn = (By.XPATH, "//input[@id='register_selectedsq1']")
    question2_dropdwn = (By.ID, "register_selectedsq2")
    qa_answer1_txt = (By.ID, "register_sq1")
    qa_answer2_txt = (By.ID, "register_sq2")
    pwd_txt1 = (By.ID, "register_pwd")
    confirm_pwd_txt2 = (By.ID, "register_cpwd")
    save_btn = (By.XPATH, "//span[text()='Save']")
    go_to_user_btn = (By.XPATH, "//span[contains(text(),'Go to User List')]")
    user_table_header_rows = (By.XPATH, "//thead/tr/th/descendant::span[1]")
    td_ele = (By.XPATH, "//tbody/tr/td")

    # web table
    get_rows = (By.XPATH, "//tbody//tr")
    cell_data = (By.XPATH, "//tbody/tr[not(position()=1)]/td")
    serch_box = (By.XPATH, "//input[@placeholder='Search here']")
    table_headers = (By.XPATH, "//thead/tr/th/descendant::span[@class='ant-table-column-title']")
    prev_page_btn = (By.XPATH, "//li[@title='Previous Page']")
    nxt_page_btn = (By.XPATH, "//li[@title='Next Page']")

    def add_user(self, FName, LName, userrolelocators, userrole):
        uname = configRead.get_uname()
        pwd1 = configRead.get_pwd()
        logger = self.log_gen()
        login = loginData(self.driver)
        login.user_login(uname, pwd1)
        P_wind = self.driver.current_window_handle
        self.click_element(self.usermanagemenr_module)
        self.click_element(self.add_user_main_btn)
        self.click_element(self.user_role_drpdwn)
        self.move_to_element(userrolelocators)
        # time.sleep(2.0)
        self.click_element(userrolelocators)
        time.sleep(0.25)
        self.send_keys(self.first_name_txt, FName)
        self.send_keys(self.last_name_txt, LName)
        mail = self.random_email() + "@mailinator.com"
        self.send_keys(self.email_txt, mail)
        logger.info("entered mail" + " " + mail)
        self.click_element(self.add_user_btn)
        # time.sleep(1.0)
        sucess_msg = self.return_text(self.add_user_msg)
        print(sucess_msg)
        assert sucess_msg == "User added successfully!"
        logger.info(mail + " " + " User added successfully!")
        if userrole == "CE User" or userrole == "Pharmacy User":
            print(userrole)
            self.click_element(self.save_next_btn)
            time.sleep(0.5)

        self.click_element(self.confirm_btn)
        nwe_user_added_text = self.return_text(self.new_user_added_msg)
        assert nwe_user_added_text == "New User is successfully added!"

        logger.info("New User is successfully added!")
        # user_mgt = UserManagement_data(self.driver)
        self.click_element(self.go_to_user_btn)
        time.sleep(1.0)
        self.search_detals(mail, mail, FName, LName, userrole)
        return mail

    def random_email(self):
        random_email = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(5))
        print(random_email)
        print(type(random_email))

        return random_email

    def set_password(self, QA1, QA2, Anw1, Anw2, pwd):
        logger = self.log_gen()
        self.click_element(self.question1_dropdwn)
        Question1 = str("//div[@class='rc-virtual-list-holder-inner']/child::div/div[contains(text(),'" + str(
            QA1) + "')]")
        select_security_qa1 = (By.XPATH, Question1)
        self.move_to_element(select_security_qa1)
        self.javascripit_click(select_security_qa1)
        self.send_keys(self.qa_answer1_txt, Anw1)
        self.click_element(self.question2_dropdwn)
        Question2 = str("(//div[@class='rc-virtual-list-holder-inner']/child::div/div[contains(text(),'" + str(
            QA2) + "')])[2]")
        select_security_qa2 = (By.XPATH, Question2)
        self.move_to_element(select_security_qa2)
        self.javascripit_click(select_security_qa2)
        self.send_keys(self.qa_answer2_txt, Anw2)
        self.send_keys(self.pwd_txt1, pwd)
        self.send_keys(self.confirm_pwd_txt2, pwd)
        logger.info("entered password")
        logger.info(pwd)
        self.click_element(self.save_btn)

    def search_detals(self, emial, username, FName, LName, userrole):
        dic = {}
        self.send_keys(self.serch_box, emial)
        row_count = self.get_webtable_rows(self.get_rows)
        cell_count = self.get_webtable_rows(self.cell_data)
        print(row_count, cell_count)
        for r in range(2, row_count + 1):
            d = self.get_webtable_rows(self.table_headers)
            for d in range(1, d+1):

                th_data = (
                    By.XPATH, "(//thead/tr/th/descendant::span[@class='ant-table-column-title'])[" + str(d) + "]")
                header = self.cell_data_txt(th_data)


                try:
                    try:
                        cell = "((//tbody/tr)[" + str(r) + "]/td)[" + str(d + 1) + "]/span"

                        locator = (By.XPATH, cell)
                        td_data = self.cell_data_txt(locator)
                        dic[header] = td_data
                    except:
                        cell = "(((//tbody/tr)[" + str(r) + "]/td)[" + str(d + 1) + "]/span)[2]"

                        locator = (By.XPATH, cell)
                        td_data = self.cell_data_txt(locator)
                        dic[header] = td_data

                except:
                    cell = "((//tbody/tr)[" + str(r) + "]/td)[" + str(d + 1) + "]"

                    locator = (By.XPATH, cell)
                    td_data = self.cell_data_txt(locator)
                    dic[header] = td_data
            break
        print(dic)
        assert dic['User Name'] == username
        assert dic['First Name'] == FName
        assert dic['Last Name'] == LName
        assert dic['Email ID'] == emial
        assert dic['User Role'] == userrole
        assert dic["Status"]=="Active"
        return dic

    def registration_link(self, QA1, QA2, Anw1, Anw2, pwd, mail):
        login = loginData(self.driver)
        logger = self.log_gen()
        # mail = self.add_user(FName, LName, userrolelocators, userrole)
        login.logout_app()
        self.driver.switch_to.new_window(Keys.CONTROL + 't')
        wind_handles_mail = self.driver.window_handles
        self.driver.switch_to.window(wind_handles_mail[1])
        self.driver.close()
        self.driver.switch_to.window(wind_handles_mail[0])
        self.driver.get(login.mailnator_url)
        self.send_keys(login.mailnator_search, mail)
        self.click_element(login.mailnator_go_btn)
        self.click_element(self.mailnator_reglink_row)
        self.driver.switch_to.frame("html_msg_body")
        time.sleep(0.5)
        reg_link = self.return_text(self.mailnator_reg_link)
        self.driver.switch_to.new_window(Keys.CONTROL + 't')
        time.sleep(0.5)
        wind_handles_mail = self.driver.window_handles
        self.driver.switch_to.window(wind_handles_mail[1])
        self.driver.close()
        self.driver.switch_to.window(wind_handles_mail[0])
        self.driver.get(reg_link)
        logger.info(reg_link)
        time.sleep(2.0)
        Security_title = self.return_text(self.security_qa_title)
        assert Security_title == "Set the following Security Questions"
        logger.info("Set the following Security Questions")
        time.sleep(1.0)
        self.set_password(QA1, QA2, Anw1, Anw2, pwd)
        time.sleep(1.0)
        logger.info("Registration Successfull!'")
        return mail
