from config import Config
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
import time

driver = Config.driver

driver.get(Config.server)

login_page = LoginPage(driver)
login_page.enter_username(Config.user)
login_page.enter_password(Config.password)
login_page.login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_search_field("fitness")
main_page.click_result_with_text("#fitness")

search_page = SearchResultPage(driver)
time.sleep(5)
search_page.check_button_text("Follow")

driver.quit()
