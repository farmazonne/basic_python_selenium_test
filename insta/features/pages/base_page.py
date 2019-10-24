from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        pass

    def on_this_page(self, *args):
        for locator in args:
            self.get_element(locator)

    def get_element(self, locator):
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(expected_condition, "Unable to locate element")

    def click_on(self, locator):
        self.get_element(locator).click()

    def set_text(self, locator, text):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

    def get_text(self, locator):
        expected_condition = ec.presence_of_element_located(locator)
        WebDriverWait(self.driver, 5).until(expected_condition, "Text value was not found in element")
        return self.get_element(locator).text

