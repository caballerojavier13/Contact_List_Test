__author__ = 'Javier Caballero'
from selenium.webdriver.common.by import By
from base_page_object import BasePage
import time

class IndexPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "sign_in": (By.CSS_SELECTOR, '.login')
    }

    def sign_in(self):
        self.find_element(*self.locator_dictionary['sign_in']).click()


    class HeaderPage(BasePage):
        def __init__(self, context):
            BasePage.__init__(self, context.browser)

        locator_dictionary = {
            "menu_women": (By.XPATH, "//*[@title='Women']")
        }