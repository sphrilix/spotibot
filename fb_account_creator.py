from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pathlib


class FbAccountCreator:
    REGISTRATION_URL = "https://www.facebook.com/"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver\\chromedriver.exe")


if __name__ == "__main__":
    fb_acc_creator = FbAccountCreator()
