import os
import chromedriver_autoinstaller

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(autouse=True)
def take_screenshot(request):
    yield
    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True, scope="class")
def setUp(request):
    global driver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        print(browser + " is started")
        chrome_option = webdriver.ChromeOptions()
        path = os.getcwd()
        list_path = list(path)

        preferences = {
            "profile.default_content_settings.popups": 0,
            "download.default_directory": list_path[0] + ":\\CP StarterKIT AutomationLatest\\DownloadFiles",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True
        }

        chrome_option.add_experimental_option("prefs", preferences)
        driver = webdriver.Chrome(options=chrome_option)
        driver.maximize_window()
        driver.delete_cookie(browser)
        driver.implicitly_wait(3.2)

    elif browser == "firefox":
        path = os.getcwd()
        list_path = list(path)

        fp = webdriver.FirefoxOptions()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.dir", list_path[0] + ":\\CP StarterKIT AutomationLatest"
                                                                 "\\DownloadFiles")
        fp.set_preference("browser.download.useDownloadDir", True)
        fp.set_preference("browser.download.viewableInternally.enabledTypes", "")
        fp.set_preference("browser.download.manager.useWindow", False)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.manager.closeWhenDone", True)
        fp.set_preference('browser.helperApps.neverAsk.openFile', "application/zip")
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
        fp.set_preference("pdfjs.disabled", True)

        # driver = webdriver.Firefox(firefox_profile=fp)

        print(browser + " is started")
        driver = webdriver.Firefox(options=fp)
        driver.maximize_window()
        driver.delete_cookie(browser)
        driver.implicitly_wait(3.2)
    elif browser == "edge":
        print(browser + " is started")
        driver = webdriver.Edge(browser)
        driver.maximize_window()
        driver.delete_cookie(browser)
        driver.implicitly_wait(3.2)
    else:

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "C:\\old data\\chrome-win64\\chrome.exe"
        path = os.getcwd()
        list_path = list(path)
        preferences = {
            "profile.default_content_settings.popups": 0,
            "download.default_directory": list_path[0] + ":\\CP StarterKIT AutomationLatest\\DownloadFiles",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True,
        }

        chrome_options.add_experimental_option("prefs", preferences)
        # SeleniumManager.driver_location("chrome")
        driver = webdriver.Chrome(options=chrome_options, service=Service("\\old data\\CP StarterKIT AutomationLatest"
                                                                          "\\venv\\Scripts\\chromedriver.exe"))

        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(3.2)

    # we are creating driver at class level
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossbrowser(request):
    return request.param
