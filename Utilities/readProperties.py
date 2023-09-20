import configparser
config = configparser.RawConfigParser()
config.read("\\old data\\CP StarterKIT AutomationLatest\\Configurations\\config.ini")

# C:\old data\CP StarterKIT AutomationLatest
class configRead:
    @staticmethod
    def get_url():
        return config.get("common info", "url")

    @staticmethod
    def get_uname():
        return config.get("common info", "uname")

    @staticmethod
    def get_pwd():
        return config.get("common info", "pwd")

    @staticmethod
    def get_SAdmin():
        return config.get("UserRoles", "super_admin")

    @staticmethod
    def get_CEUser():
        return config.get("UserRoles", "ce_user")

    @staticmethod
    def get_PharmaUser():
        return config.get("UserRoles", "pharma_user")

    @staticmethod
    def get_standard_User():
        return config.get("UserRoles", "standard_user")




    # def send_keybord_keys(self,  keyvalue):


