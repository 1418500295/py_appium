import os

from appium import webdriver
from utils.operate_yaml import ReadYaml

yaml_data = ReadYaml.get_yaml("app_config.yaml")


class DriverUtil():

    @staticmethod
    def get_driver():
        project_path = os.path.dirname(os.getcwd())
        app_path = project_path + "/config/"

        capabilities = {
            "platformName": yaml_data["platformName"],
            "deviceName": yaml_data["deviceName"],
            # "app": app_path + yaml_data["app"],
            "appPackage": yaml_data["appPackage"],
            "appActivity": yaml_data["appActivity"],
            # "noReset": yaml_data["noReset"]

        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)

        return driver

if __name__ == '__main__':
    print(DriverUtil.get_driver())

