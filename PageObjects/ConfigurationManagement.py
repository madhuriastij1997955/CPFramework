import string
import time
import random

from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class Configurationmanagement(BaseClass):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # Add CE Details
    configuration_module = (By.XPATH, "//span[text()='Configuration Management']")
    default_confi_drop_value = (By.XPATH, "//span[text()='Covered Entities']")
    configuration_title = (By.XPATH, "//span[text()='Configuration']")
    CE_title = (By.XPATH, "//span[text()='Covered Entity List']")
    Add_ce_button = (By.XPATH, "//span[text()=' Add Covered Entity']/parent::button")
    OPA_ID_txt_box = (By.ID, "addce_opaid")
    OPA_search_box = (By.XPATH, "//input[@name='opaidinput']/ancestor::div[contains(@class,"
                                "'ant-form-item-control-input')]/descendant::span/parent::button")
    OPA_found_msg = (By.XPATH, "//span[contains(text(),'OPA ID not found.')]")
    # OPA ID not found. Please complete the form to add.
    CE_txt_box = (By.XPATH, "//input[@name='cenameinput']")
    CE_search_box = (By.XPATH, "//input[@name='cenameinput']/ancestor::div[contains(@class,"
                               "'ant-form-item-control-input')]/descendant::span/parent::button")
    CE_found_msg = (By.XPATH, "//span[contains(text(),'Covered Entity not found.')]")
    # Covered Entity not found. Please complete the form to add.
    CE_dropdown = (By.XPATH, "//input[@id='addce_cetype']/parent::span/parent::div")
    CE_address = (By.NAME, "addressinput")
    CE_cancel_btn = (By.XPATH, "//span[text()='Cancel']/parent::button")
    CE_save_btn = (By.XPATH, "//span[text()='Save']/parent::button")
    CE_add_con_btn = (By.XPATH, "//span[text()='Add & Continue']/parent::button")

    # add pharmacy
    map_pharamcy_ce_title = (By.XPATH, "//span[text()='Map Pharmacy to Covered Entity']")
    add_pharmacy_title = (By.XPATH, "//span[text()='Add Pharmacy']")
    NPI_code_txt_box = (By.NAME, "npicodeinput")
    NPI_code_search_box = (By.XPATH, "//input[@name='npicodeinput']/ancestor::div[contains(@class,"
                                     "'ant-form-item-control-input')]/descendant::span/parent::button")
    NPI_serched_msg = (By.XPATH, "//span[contains(text(),'Pharmacy not found')]")
    Pharmacy_txt_box = (By.NAME, "pharmacynameinput")

    Pharmacy_search_box = (By.XPATH, "//input[@name='pharmacynameinput']/ancestor::div[contains(@class,"
                                     "'ant-form-item-control-input')]/descendant::span/parent::button")
    Pharmacy_search_title = (By.XPATH, "//span[contains(text(),'Pharmacy not found')]")
    NABP_code_txt_box = (By.ID, "addpharmacy_nabpcode")
    pharamcy_type_dropdown = (By.ID, "addpharmacy_pharmacytype")
    pharamcy_store_num = (By.NAME, "pharmacystorenumberinput")
    pharamcy_address = (By.NAME, "addressinput")
    wholesaler_drop_down = (By.ID, "addpharmacy_wholesaler")
    wholesaler_account_num = (By.ID, "addpharmacy_wholesaleraccountno")
    save_conf_btn = (By.XPATH, "//button[@name='addpharmacy']")
    # Covered Entity Details preview
    ce_title_preview = (By.XPATH, "//span[text()='Covered Entity Details']")
    # pharamcy preview title
    pharmacy_preview_title = (By.XPATH, "//span[text()='Pharmacy Details']")
    confirm_btn = (By.XPATH, "//span[text()='Confirm']/parent::button")
    ce_added_msg_title = (By.XPATH, "//span[contains(text(),'New Covered Entity is successfully added!')]")
    # search CE
    search_txt_box = (By.XPATH, "//input[@placeholder='Search here']")
    get_rows = (By.XPATH, "//tbody//tr")
    cell_data = (By.XPATH, "//tbody/tr[not(position()=1)]/td")
    table_headers = (By.XPATH, "//thead/tr/th/descendant::span[@class='ant-table-column-title']")

    # edit CE
    edit_icon = (By.XPATH, "//span[@class='anticon anticon-edit']/parent::button")
    ce_updated_sucess_msg = (
        By.XPATH, "//span[contains(text(),'The Covered Entity details has been successfully updated')]")
    CE_edit_con_btn = (By.XPATH, "//span[text()=' Continue']/parent::button")
    show_more_link = (By.XPATH, "//span[text()='Show more']")
    pharmacy_list_count = (By.XPATH, "//div[contains(@class,'ant-collapse ant-collapse-icon-position-end')]")
    save_continue_btn = (By.XPATH, "//span[contains(text(),'Save And Confirm')]")
    phar1_NPI1 = (By.XPATH, "(//span[text()='NPI Code : ']/parent::div/following-sibling::div/span)[1]")
    phar1_account_num = (By.XPATH, "//span[text()='Account Number : ']/parent::div")

    def add_covredEntity(self, OPAID, CE_name, ce_type, addres, NPI, pharamcy_name, NABP, pgaramcy_type,
                         pharamcystore_num, pharamcy_addres, wholesaler, account_num):
        self.click_element(self.configuration_module)
        self.soft_assert(self.assertEqual, self.return_text(self.configuration_title), "Configuration")
        self.soft_assert(self.assertEqual, self.return_text(self.default_confi_drop_value), "Covered Entities")
        assert self.return_text(self.CE_title) == "Covered Entity List"
        self.click_element(self.Add_ce_button)
        time.sleep(0.5)
        self.send_keys(self.OPA_ID_txt_box, OPAID)
        time.sleep(0.5)
        self.javascripit_click(self.OPA_search_box)
        assert self.return_text(self.OPA_found_msg) == "OPA ID not found. Please complete the form to add."
        self.send_keys(self.CE_txt_box, CE_name)
        # self.click_element(self.CE_search_box)
        # assert self.return_text(self.CE_found_msg) == "Covered Entity not found. Please complete the form to add."
        # time.sleep(0.5)
        # self.send_keys(self.CE_txt_box, CE_name)
        self.move_to_element(self.CE_dropdown)
        self.click_and_hold(self.CE_dropdown)
        ce_type_value = "//div[contains(text(),'" + str(ce_type) + "')]"
        ce_type_value_locator = (By.XPATH, ce_type_value)
        print(ce_type_value_locator)
        time.sleep(0.5)
        self.click_element(ce_type_value_locator)
        self.send_keys(self.CE_address, addres)
        self.click_element(self.CE_add_con_btn)
        time.sleep(0.5)
        self.add_pharmacy(NPI, pharamcy_name, NABP, pgaramcy_type, pharamcystore_num,
                          pharamcy_addres, wholesaler, account_num)

        #     preview CE Details
        OPA_id_xpath = (
            By.XPATH,
            "//span[text()='Covered Entity Details']/parent::div/descendant::div[text()='" + str(OPAID) + "']")
        assert self.return_text(OPA_id_xpath) == OPAID
        CE_type_xpath = (
            By.XPATH,
            "//span[text()='Covered Entity Details']/parent::div/descendant::div[text()='" + str(ce_type) + "']")
        assert self.return_text(CE_type_xpath) == ce_type
        ce_name_xpath = (
            By.XPATH,
            "//span[text()='Covered Entity Details']/parent::div/descendant::div[text()='" + str(CE_name) + "']")
        assert self.return_text(ce_name_xpath) == CE_name

        #     preview pharamcy details
        pharamcy_name_xpath = (
            By.XPATH, "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + pharamcy_name + "']")
        assert self.return_text(pharamcy_name_xpath) == pharamcy_name
        wholesaler_xpath = (
            By.XPATH, "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + wholesaler + "']")
        assert self.return_text(wholesaler_xpath) == wholesaler
        npicode_xpath = (
            By.XPATH, "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + NPI + "']")
        assert self.return_text(npicode_xpath) == NPI
        accountnum_xpah = (
            By.XPATH, "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + account_num + "']")
        assert self.return_text(accountnum_xpah) == account_num
        NABP_xpah = (
            By.XPATH, "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + NABP + "']")
        assert self.return_text(NABP_xpah) == NABP
        pharamcytyep_xpah = (
            By.XPATH, "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + pgaramcy_type + "']")
        assert self.return_text(pharamcytyep_xpah) == pgaramcy_type
        pharamcy_storeNum_xpah = (
            By.XPATH,
            "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + pharamcystore_num + "']")
        assert self.return_text(pharamcy_storeNum_xpah) == pharamcystore_num
        pharamcy_addres_xpah = (
            By.XPATH,
            "//span[text()='Pharmacy Details']/parent::div/descendant::div[text()='" + pharamcy_addres + "']")
        assert self.return_text(pharamcy_addres_xpah) == pharamcy_addres
        self.click_element(self.confirm_btn)
        assert self.return_text(self.ce_added_msg_title) == "New Covered Entity is successfully added!"

    def add_pharmacy(self, NPI, pharamcy_name, NABP, pgaramcy_type, pharamcystore_num,
                     pharamcy_addres, wholesaler, account_num):
        map_pha_title = self.return_text(self.map_pharamcy_ce_title)
        assert map_pha_title == "Map Pharmacy to Covered Entity"
        add_pha_title = self.return_text(self.add_pharmacy_title)
        assert add_pha_title == "Add Pharmacy"
        # if len(NPI)
        self.send_keys(self.NPI_code_txt_box, NPI)
        # time.sleep(0.5)
        # self.move_to_element(self.NPI_code_search_box)
        # time.sleep(0.5)
        # self.click_element(self.NPI_code_search_box)
        # time.sleep(0.5)
        # npi_serch_msg = self.return_text(self.NPI_serched_msg)
        # assert npi_serch_msg == "Pharmacy not found. Please complete the form to ad..."
        self.send_keys(self.Pharmacy_txt_box, pharamcy_name)
        # self.click_element(self.Pharmacy_search_box)
        # phar_msg_searched = self.return_text(self.Pharmacy_search_title)
        # assert phar_msg_searched == "Pharmacy not found. Please complete the form to add."
        self.send_keys(self.NABP_code_txt_box, NABP)
        self.click_element(self.pharamcy_type_dropdown)
        pharmacy_type_value = "//div[contains(text(),'" + str(pgaramcy_type) + "')]"
        pharmacy_type_value_locator = (By.XPATH, pharmacy_type_value)
        self.click_element(pharmacy_type_value_locator)
        self.send_keys(self.pharamcy_store_num, pharamcystore_num)
        self.send_keys(self.pharamcy_address, pharamcy_addres)
        self.click_element(self.wholesaler_drop_down)
        wholesaler_type_value = "//div[contains(text(),'" + str(wholesaler) + "')]"
        wholesaler_type_value_locator = (By.XPATH, wholesaler_type_value)
        self.click_element(wholesaler_type_value_locator)
        self.send_keys(self.wholesaler_account_num, account_num)
        time.sleep(1.5)
        self.click_element(self.save_conf_btn)
        time.sleep(1.5)

    def search_ce(self, CE_name, opaid, CE_Type):
        self.click_element(self.configuration_module)
        time.sleep(0.9)
        self.send_keys(self.search_txt_box, CE_name)
        dic = self.get_search_detals()
        assert dic['Covered Entity Name'] == CE_name
        assert dic['OPA ID'] == opaid
        assert dic['Covered Entity Type'] == CE_Type

    def edit_ceDetails(self, OPAID1, CE_name, ce_type, addres, NPI, pharamcy_name, NABP, pgaramcy_type,
                       pharamcystore_num, pharamcy_addres, wholesaler, account_num, pharmacy1_NPI, phar1_accountNum):
        self.click_element(self.configuration_module)
        print(OPAID1)
        self.send_keys(self.search_txt_box, CE_name)
        dic = self.get_search_detals()
        pharcmacy_count = dic['Pharmacies']
        time.sleep(0.5)
        self.click_element(self.edit_icon)
        self.send_keys(self.CE_txt_box, CE_name)
        self.move_to_element(self.CE_dropdown)
        self.click_and_hold(self.CE_dropdown)
        ce_type_value = "//div[contains(text(),'" + str(ce_type) + "')]"
        ce_type_value_locator = (By.XPATH, ce_type_value)
        print(ce_type_value_locator)
        time.sleep(0.5)
        self.click_element(ce_type_value_locator)
        self.send_keys(self.CE_address, addres)
        self.click_element(self.CE_edit_con_btn)
        assert self.return_text(self.phar1_NPI1) == pharmacy1_NPI
        self.click_element(self.phar1_NPI1)
        PH1_accountnum = self.return_text(self.phar1_account_num)
        ph1_acount_num = PH1_accountnum.split(":")
        assert ph1_acount_num[1].strip() == phar1_accountNum
        time.sleep(0.5)
        try:
            self.is_displayed(self.show_more_link)
            self.click_element(self.show_more_link)
        except:
            pass

        no_of_px = self.find_elements(self.pharmacy_list_count)
        assert int(pharcmacy_count) == len(no_of_px)

        time.sleep(1.0)

        self.scroll_to_ele(self.save_continue_btn)

        # self.add_pharmacy(NPI, pharamcy_name, NABP, pgaramcy_type, pharamcystore_num,
        #                   pharamcy_addres, wholesaler, account_num)
        self.click_element(self.save_continue_btn)
        self.click_element(self.confirm_btn)
        assert self.return_text(
            self.ce_updated_sucess_msg) == "The Covered Entity details has been successfully updated"
        time.sleep(0.5)
