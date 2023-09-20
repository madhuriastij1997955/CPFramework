import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import loginData
from PageObjects.User_Registration_Link import User_Registration
from TestData.CP_TestData import Security_QAs
from Utilities.BaseClass import BaseClass
from Utilities.readProperties import configRead


class UserManagement_data(BaseClass):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    usermanagemenr_module = (By.XPATH, "//li[@modulename='UserManagement']")
    serch_box = (By.XPATH, "//input[@placeholder='Search here']")
    # add user
    user_management_title = (By.XPATH, "//span[contains(text(),'Add User')]/parent::button/preceding-sibling::span")
    add_user_main_btn = (By.XPATH, "//span[contains(text(),'Add User')]")
    search_txt_box = (By.XPATH, "//input[@placeholder='Search here']")

    show_records_dropdwn = (By.XPATH, "//span[@class='ant-select-selection-search']/input")
    users_list = {"Super Admin": (By.XPATH, "//div[text()='Super Admin']"),
                  "CE User": (By.XPATH, "//div[text()='CE User']"),
                  "Pharmacy User": (By.XPATH, "//div[text()='Pharmacy User']"),
                  "Standard User": (By.XPATH, "//div[text()='Standard User']")
                  }

    # edit user
    edit_dot_btn = (By.XPATH, "//span[@class='anticon anticon-more']/parent::button")
    edit_btn = (By.XPATH, "//span[text()='Edit']")
    edit_title = (By.XPATH, "//span[text()='Edit Existing User']")
    user_name = (By.XPATH, "//span[text()='User Name']/parent::div/following-sibling::div/span")
    first_name = (By.XPATH, "//span[text()='First Name']/parent::div/following-sibling::div/span")
    last_name = (By.XPATH, "//span[text()='Last Name']/parent::div/following-sibling::div/span")
    email_id = (By.XPATH, "//span[text()='Email ID']/parent::div/following-sibling::div/span")
    user_role = (By.XPATH, "//span[text()='User Role']/parent::div/following-sibling::div/span/span")
    userrole_txt_box = (By.XPATH, "//input[@id='addce_roleId']")
    userrole_txt_box_value = (By.XPATH, "//span[@class='ant-select-selection-item']")
    email_txt_box = (By.XPATH, "//input[@id='addce_emailId']")
    username_txt_box = (By.XPATH, "//input[@id='addce_userName']")
    first_name_txt_box = (By.XPATH, "//input[@id='addce_firstName']")
    last_name_txt_box = (By.XPATH, "//input[@id='addce_lastName']")
    status_btn = (By.XPATH, "//div[@class='ant-switch-handle']/parent::button")
    resend_reg_link_chx_box = (By.XPATH, "//input[@name='request']")
    lock_act_chx_box = (By.XPATH, "//span[text()='Lock Account']/preceding-sibling::span/input")
    cancel_btn = (By.XPATH, "//span[text()='Cancel']/parent::button")
    save_cont_btn = (By.XPATH, "//span[contains(text(),'Save')]/parent::button")
    existing_user_settings = (By.XPATH, "//span[text()='Edit Existing User Settings']")
    details_updated_msg = (By.XPATH, "//span[text()='Details updated successfully!']")
    entity_acess_tab = (By.XPATH, "//div[text()='Entity Access']")
    roles_perm_tab = (By.XPATH, "//div[text()='Role Permission']")
    # bread-crumbs_status
    current_status = (By.XPATH, "//h7[text()='Completed']")
    # user_settings = (By.XPATH, "//div[contains(text(),'User Settings')]")
    edit_user_link = (By.XPATH, "//h7[text()='Edit User']")
    user_settings = (By.XPATH, "//h7[text()='User Settings']")
    edit_user_pencil_icon = (By.XPATH, "//span[text()='Edit Existing User  ']/span")
    edit_user_setting_pencil_icon = (By.XPATH, "//span[text()='Edit Existing User Settings  ']/span")
    # preview edited details

    pre_userrole = (By.XPATH, "(//div[text()='User Role']/following-sibling::div)[2]")
    pre_emailid = (By.XPATH, "(//div[text()='Email ID']/following-sibling::div)[2]")
    pre_username = (By.XPATH, "(//div[text()='User Name']/following-sibling::div)[2]")
    pre_firstname = (By.XPATH, "(//div[text()='First Name']/following-sibling::div)[2]")
    pre_lastname = (By.XPATH, "(//div[text()='Last Name']/following-sibling::div)[2]")
    pre_confirm_btn = (By.XPATH, "//span[contains(text(),'Confirm')]/parent::button")
    edited_suces_msg = (By.XPATH, "//span[contains(text(),' User edit  successfully done')]")

    # view user
    view_icon = (By.XPATH, "//tbody/tr[not(position()=1)]/td[1]/button")
    view_user_title = (By.XPATH, "//span[text()='User Details']")

    # forgot link
    ForGot_link = (By.XPATH, "//span[text()='Forgot Password?']/parent::button")
    forgot_link_title = (By.XPATH, "//strong[text()='Forgot Password?']")
    forgot_uname_txt_box = (By.XPATH, "//input[@id='normal_login_email']")
    forgot_submit_btn = (By.XPATH, "//span[text()='Submit']/parent::button")
    Forgot_updated_msg = (By.XPATH, "//span[contains(text(),'Password reset link sent to your registered Email ID.')]")
    mailnator_forgot_link_row = (
        By.XPATH, "//table[@class='table-striped jambo_table']/tbody/tr[1]/td[3 and contains(text("
                  "),'Application - Forgot Password')]")
    mailnator_forgot_link = (By.XPATH, "(//a[@rel='nofollow'])[2]")
    create_new_pwd_title = (By.XPATH, "//strong[text()='Create New Password']")
    QA1 = (By.XPATH, "//span[text()='Question 1']/parent::div/following-sibling::div/span")
    QA2 = (By.XPATH, "//span[text()='Question 2']/parent::div/following-sibling::div/span")
    QA1_Answ1 = (By.XPATH, "//input[@id='normal_login_answer1']")
    QA1_Answ2 = (By.XPATH, "//input[@id='normal_login_answer2']")
    validate_btn = (By.XPATH, "//span[text()='Validate Answers']/parent::button")
    chage_pwd_title = (By.XPATH, "//strong[text()='Change your Password']")
    pwd_txt_box = (By.XPATH, "//input[@id='normal_login_password']")
    confirm_pwd_txt_box = (By.XPATH, "//input[@id='normal_login_confirmpassword']")
    save_btn = (By.XPATH, "//span[text()='Save']/parent::button")
    pwd_reset_updated_msg = (By.XPATH, "//span[text()='Password reset successfully!']")

    # lock_unlock

    invalid_pwd_txt = (By.XPATH, "//b[@class='cpf-alert-bold']")
    No_of_attempts = (By.XPATH, "//div[@class='ant-alert-description']/b")
    account_locked_txt = (By.XPATH, "//b[@class='cpf-alert-bold']")
    locked_msg = (By.XPATH, "//div[@class='ant-alert-description']")
    account_locked_status = (By.XPATH, "//span[text()='Account']/parent::div/following-sibling::div/span")
    lock_check_box = (By.XPATH, "//span[text()='Lock Account']/preceding-sibling::span/input")

    # export button
    export_btn = (By.XPATH, "//span[contains(text(),' Export')]/parent::button")
    configuration_module = (By.XPATH, "//span[text()='ConfigurationManagement']")

    # pagination table
    pagination_left_arrow = (By.XPATH, "//span[@aria-label='left']/parent::button")
    pagination_right_arrow = (By.XPATH, "//span[@aria-label='right']/parent::button")
    total_records = (By.XPATH, "(//span[contains(text(),'Showing ')]/span)[2]")
    search_username = (By.XPATH, "//tbody/tr[not(position()=1)]/td[2]")
    right_arrow_disabled = (By.XPATH, "//span[@aria-label='right']/ancestor::li")

    def Usermanagement_UI_elements(self):
        self.verify_element_displayed(self.user_management_title)
        self.verify_element_displayed(self.add_user_main_btn)
        self.verify_element_displayed(self.search_txt_box)
        self.verify_element_displayed(self.export_btn)
        self.verify_element_displayed(self.show_records_dropdwn)

    def add_user(self, userslist):
        logger = self.log_gen()
        for userrole, locator in userslist.items():
            from PageObjects.User_Registration_Link import User_Registration
            add_users = User_Registration(self.driver)
            mail = add_users.add_user(Security_QAs.FName, Security_QAs.LName, locator, userrole)
            print(userrole + " is added ")
            logger.info(userrole + " is added")
            add_users.registration_link(Security_QAs.QA3, Security_QAs.QA5, Security_QAs.Ans1, Security_QAs.Ans2,
                                        Security_QAs.password, mail)


    def edit_user(self, username, email, firstname, lastname,userrole):
        user_reg = User_Registration(self.driver)
        logger = self.log_gen()
        self.click_element(self.usermanagemenr_module)
        self.send_keys(self.serch_box, username)
        serched_details = user_reg.get_search_detals()
        print(serched_details)
        self.click_element(self.edit_dot_btn)
        time.sleep(0.5)
        self.click_element(self.edit_btn)
        edit_title = self.return_text(self.edit_title)
        self.soft_assert(self.assertTrue, edit_title, "Edit Existing User")
        # assert edit_title == "Edit Existing User"
        logger.info(edit_title)
        # verifying fields are enabled or not
        assert False == self.is_enabled(self.userrole_txt_box)
        assert False == self.is_enabled(self.username_txt_box)
        assert False == self.is_enabled(self.email_txt_box)
        assert True == self.is_enabled(self.first_name_txt_box)
        assert True == self.is_enabled(self.last_name_txt_box)
        # verifying the searched data information in edit screen

        assert serched_details['User Role'] == self.return_text(self.userrole_txt_box_value)
        assert serched_details['User Name'] == self.get_txt_box_value(self.username_txt_box, "value")
        assert serched_details['First Name'] == self.get_txt_box_value(self.first_name_txt_box, "value")
        assert serched_details['Last Name'] == self.get_txt_box_value(self.last_name_txt_box, "value")
        assert serched_details['Email ID'] == self.get_txt_box_value(self.email_txt_box, "value")
        # verifying the searched data information in edit screen in bread crumb

        assert serched_details['User Name'] == self.return_text(self.user_name)
        assert serched_details['User Role'] == self.return_text(self.user_role)
        assert serched_details['First Name'] == self.return_text(self.first_name)
        assert serched_details['Last Name'] == self.return_text(self.last_name)
        assert serched_details['Email ID'] == self.return_text(self.email_id)

        # update firstname and last name
        self.send_keys(self.first_name_txt_box, firstname)
        logger.info(firstname + " first name is edited value")
        self.send_keys(self.last_name_txt_box, lastname)
        logger.info(lastname + " lastname is edited value")
        self.click_element(self.save_cont_btn)
        assert "Details updated successfully!" == self.return_text(self.details_updated_msg)
        logger.info("updated user details")
        if userrole == "CE User" or userrole == "Pharmacy User":
            assert "Edit Existing User Settings" == self.return_text(self.existing_user_settings)
            assert "Completed" == self.return_text(self.current_status)
            self.click_element(self.save_cont_btn)
        # verifying the preview elements
        time.sleep(2.0)
        preview_userrole = self.return_text(self.pre_userrole)
        assert serched_details['User Role'] == preview_userrole
        logger.info(preview_userrole)
        preview_emailid = self.return_text(self.pre_emailid)
        assert serched_details['Email ID'] == preview_emailid
        logger.info(preview_emailid)
        preview_username = self.return_text(self.pre_username)
        assert serched_details['User Name'] == preview_username
        logger.info(preview_username)
        preview_first_name = self.return_text(self.pre_firstname)
        assert firstname == preview_first_name
        logger.info(preview_first_name)
        preview_lastname = self.return_text(self.pre_lastname)
        assert lastname == preview_lastname
        logger.info(preview_lastname)
        self.click_element(self.pre_confirm_btn)
        logger.info("preview details are updated")
        assert "User edit successfully done" == self.return_text(self.edited_suces_msg)
        logger.info("User edit successfully done")
        self.assert_all()

    def view_user_details(self, username):
        user_reg = User_Registration(self.driver)
        logger = self.log_gen()
        self.click_element(self.usermanagemenr_module)
        self.send_keys(self.serch_box, username)
        serched_details = user_reg.get_search_detals()
        print(serched_details)
        self.click_element(self.view_icon)
        time.sleep(0.5)
        assert serched_details['User Name'] == self.return_text(self.user_name)
        assert serched_details['User Role'] == self.return_text(self.user_role)
        assert serched_details['First Name'] == self.return_text(self.first_name)
        assert serched_details['Last Name'] == self.return_text(self.last_name)
        assert serched_details['Email ID'] == self.return_text(self.email_id)
        assert serched_details['Status'] == "Active"
        self.click_element(self.edit_btn)

    def forgot_link(self, email, QA1, QA2, Ans1, Ans2, pwd):
        logger = self.log_gen()
        parent_id = self.driver.current_window_handle
        self.click_element(self.ForGot_link)
        forgot_title = self.return_text(self.forgot_link_title)
        assert forgot_title == "Forgot Password?"
        self.send_keys(self.forgot_uname_txt_box, email)
        self.click_element(self.forgot_submit_btn)
        updated_msg = self.return_text(self.Forgot_updated_msg)
        logger.info(updated_msg)
        assert updated_msg == "Password reset link sent to your registered Email ID."
        login = loginData(self.driver)

        self.driver.switch_to.new_window(Keys.CONTROL + 't')
        wind_handles_mail = self.driver.window_handles
        self.driver.switch_to.window(wind_handles_mail[1])
        self.driver.close()
        self.driver.switch_to.window(wind_handles_mail[0])
        self.driver.get(login.mailnator_url)
        self.send_keys(login.mailnator_search, email)
        self.click_element(login.mailnator_go_btn)
        self.click_element(self.mailnator_forgot_link_row)
        self.driver.switch_to.frame("html_msg_body")
        forgot_link = self.return_text(self.mailnator_forgot_link)
        self.driver.switch_to.new_window(Keys.CONTROL + 't')
        wind_handles_mail = self.driver.window_handles
        self.driver.switch_to.window(wind_handles_mail[1])
        self.driver.close()
        self.driver.switch_to.window(wind_handles_mail[0])
        self.driver.get(forgot_link)
        create_pwd_title = self.return_text(self.create_new_pwd_title)
        assert "Create New Password" == create_pwd_title
        time.sleep(1.0)
        QA1_txt = self.return_text(self.QA1)
        QA_1 = QA1_txt.split("*")
        print(QA_1[1])

        assert QA_1[1].strip() == QA1
        QA2_txt = self.return_text(self.QA2)
        QA_2 = QA2_txt.split("*")
        print(QA2_txt)
        assert QA_2[1].strip() == QA2
        self.send_keys(self.QA1_Answ1, Ans1)
        self.send_keys(self.QA1_Answ2, Ans2)
        self.click_element(self.validate_btn)
        change_pwd_title = self.return_text(self.chage_pwd_title)
        logger.info(change_pwd_title)
        assert change_pwd_title == "Change your Password"
        self.send_keys(self.pwd_txt_box, pwd)
        self.send_keys(self.confirm_pwd_txt_box, pwd)
        self.click_element(self.save_btn)
        pwd_reset_msg = self.return_text(self.pwd_reset_updated_msg)
        assert "Password reset successfully!" == pwd_reset_msg
        logger.info(pwd_reset_msg)

    def lock_user_login_UI(self, no_of_attempt, mail,userrole):
        uname = configRead.get_uname()
        pwd = configRead.get_pwd()

        loginpage = loginData(self.driver)
        logger = self.log_gen()
        logger.info(loginpage.cp_url)
        self.driver.get(loginpage.cp_url)
        window_handles = self.driver.current_window_handle
        self.send_keys(loginpage.uname_txtbox, mail)
        self.send_keys(loginpage.pwd_txtbox, "hfhuuy2248@")
        for i in range(1, no_of_attempt + 1):

            self.click_element(loginpage.login_btn)
            if i < 3:
                Inpwd_txt = self.return_text(self.invalid_pwd_txt)
                assert "Invalid Password. Please try again." == Inpwd_txt
                noOf_att = self.return_text(self.No_of_attempts)

                no_of_attempt_num = list(noOf_att)

                print("Remaining attempts:" + " " + str(no_of_attempt_num[-1]))
                logger.info("Remaining attempts:" + " " + str(no_of_attempt_num[-1]))
                try:
                    assert "Remaining attempts:" + " " + str(no_of_attempt_num[-1]) == noOf_att
                except:
                    assert "Remaining attempt:" + " " + str(no_of_attempt_num[-1]) == noOf_att

            if i == 3:
                account_locked_msg = self.return_text(self.account_locked_txt)
                print(account_locked_msg)
                assert account_locked_msg == "This user account is locked for security reasons."
                logger.info(account_locked_msg)
                assert self.return_text(
                    self.locked_msg) == "Please check your email for the notification, or contact the administrator."
                loginpage.user_login(uname, pwd)
                self.click_element(self.usermanagemenr_module)
                time.sleep(0.5)
                self.send_keys(self.search_txt_box, mail)
                self.click_element(self.edit_dot_btn)
                time.sleep(0.5)
                self.click_element(self.edit_btn)
                user_locked_status = self.return_text(self.account_locked_status)
                assert user_locked_status == "Locked"
                self.click_element(self.lock_check_box)
                user_unlocked_status = self.return_text(self.account_locked_status)
                assert user_unlocked_status == "Unlocked"
                self.click_element(self.save_cont_btn)
                assert "Details updated successfully!" == self.return_text(self.details_updated_msg)
                logger.info("updated user details")

                if userrole == "CE User" or userrole == "Pharmacy User":

                    assert "Edit Existing User Settings" == self.return_text(self.existing_user_settings)
                    assert "Completed" == self.return_text(self.current_status)
                    self.click_element(self.save_cont_btn)
                # verifying the preview elements
                time.sleep(1.0)
                self.click_element(self.pre_confirm_btn)
                logger.info("preview details are updated")
                assert "User edit successfully done" == self.return_text(self.edited_suces_msg)
                logger.info("User edit successfully done")

    def export_data(self):

        logger = self.log_gen()
        # self.click_element(self.usermanagemenr_module)
        time.sleep(0.5)
        # self.click_element(self.export_btn)
        self.javascripit_click(self.export_btn)
        time.sleep(0.5)

    def pagination_table(self, username):
        self.click_element(self.usermanagemenr_module)
        time.sleep(1.0)
        staus = False

        while self.get_tag_attribute(self.right_arrow_disabled, "aria-disabled") != "true":
            list_users = self.find_elements(self.search_username)
            for user in range(1, len(list_users)):
                get_user = (By.XPATH, "(//tbody/tr[not(position()=1)]/td[2])[" + str(user) + "]")
                if username == self.return_text(get_user):
                    self.send_keys(self.search_txt_box, self.return_text(get_user))
                    staus = True
                    break

            self.click_element(self.pagination_right_arrow)

        if staus == True:
            print("user is found")
        else:
            print("given user is not exsited in the system")
