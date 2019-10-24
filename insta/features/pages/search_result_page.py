from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class SearchResultPage(BasePage):

    BUTTON_FOLLOW = (By.XPATH, "//button[@type= 'button']")

    def _verify_page(self):
        self.on_this_page(self.BUTTON_FOLLOW)

    def check_button_text(self, text):
        value = self.get_text(self.BUTTON_FOLLOW)
        assert text in value
