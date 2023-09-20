import allure
import pytest

from PageObjects.LoginPage import loginData
from PageObjects.UserManagement import UserManagement_data
from Utilities.BaseClass import BaseClass


class Test_Add_users(BaseClass):

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(3)
    def test_add_users(self):
        add_users = UserManagement_data(self.driver)
        add_users.add_user(add_users.users_list)
