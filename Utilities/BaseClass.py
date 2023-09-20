import logging
import random
import string
import time
from datetime import datetime
import pytest
import softest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @pytest.mark.usefixtures("setUp")
class BaseClass(softest.TestCase):

    def verify_element_displayed(self, locator):
        exp_wait = WebDriverWait(self.driver, 5, 1, Exception)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        status = web_ele.is_displayed()
        return status

    def send_keys(self, locator, text):
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        web_ele.clear()
        web_ele.send_keys(Keys.CONTROL + 'a')
        web_ele.send_keys(Keys.DELETE)
        self.driver.execute_script("arguments[0].value ='';", web_ele)
        web_ele.send_keys(text)

    def click_element(self, locator):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        web_ele.click()

    def return_text(self, locator):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.visibility_of_element_located(locator))
        return web_ele.text

    def get_txt_box_value(self, locator, attirubute):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        # exp_wait.until(EC.staleness_of(web_ele))
        return web_ele.get_attribute(attirubute)

    def cell_data_txt(self, loactor):
        return self.driver.find_element(loactor[0], loactor[1]).text

    def log_gen(self):
        logging.basicConfig(filename='\\CP StarterKIT Automation\\Logs\\logs.log',
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    def get_screenshot(self, path, name):
        self.driver.save_screenshot(path + name)

    def move_to_element(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.move_to_element(web_ele).perform()

    def right_click(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.context_click(web_ele).perform()

    def double_click(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.double_click(web_ele).perform()

    def click_and_hold(self, locator):
        mouse_act = ActionChains(self.driver)
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        mouse_act.click_and_hold(web_ele).perform()

    def javascripit_click(self, locator):
        exp_wait = WebDriverWait(self.driver, 5, 1)
        web_ele = exp_wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", web_ele)

    def get_webtable_rows(self, locator):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        list = web_ele.find_elements(locator[0], locator[1])
        return len(list)

    def get_webtable_headres(self, locator):
        exp_wait = WebDriverWait(self.driver, 25, 1)
        web_ele = exp_wait.until(EC.presence_of_element_located(locator))
        headres_list = {}
        for index, header_text in enumerate(web_ele):
            headres_list[index] = header_text

        return headres_list

    def is_enabled(self, locator):
        ele = self.driver.find_element(locator[0], locator[1])
        return ele.is_enabled()
    def is_displayed(self, locator):
        ele = self.driver.find_element(locator[0], locator[1])
        return ele.is_displayed()

    def get_time_stamp(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_datetime

    def find_elements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])

    def scroll_to_ele(self,locator):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(locator[0], locator[1] ))

    def get_tag_attribute(self, locator, attirubute):
        get_value = self.driver.find_element(locator[0], locator[1]).get_attribute(attirubute)
        return get_value

    def random_number(self):
        random_num = ''.join(random.choice(string.digits) for x in range(7))
        return random_num

    def random_number_NPI(self):
        random_num = ''.join(random.choice(string.digits) for x in range(11))
        return random_num

    def random_letters(self):
        random_letters = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for x in range(8))
        return random_letters

    def random_letter(self):
        random_letters = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for x in range(12))
        return random_letters

    def get_search_detals(self):
        get_rows = (By.XPATH, "//tbody//tr")
        cell_data = (By.XPATH, "//tbody/tr[not(position()=1)]/td")
        table_headers = (By.XPATH, "//thead/tr/th/descendant::span[@class='ant-table-column-title']")
        dic = {}
        row_count = self.get_webtable_rows(get_rows)
        cell_count = self.get_webtable_rows(cell_data)
        print(row_count, cell_count)
        for r in range(2, row_count + 1):
            d = self.get_webtable_rows(table_headers)
            for d in range(1, d+1):

                th_data = (
                    By.XPATH, "(//thead/tr/th/descendant::span[@class='ant-table-column-title'])[" + str(d) + "]")
                header = self.cell_data_txt(th_data)
                # if d == 6:
                #     d = d + 2

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
        return dic
