from pathlib import Path

from selenium import webdriver


class Config:
    data_folder = Path("data/")
    user = 'pyautomation'
    password = 'Ab123456789!'
    server = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome("C:/Users/farmazonne/Desktop/PythonCourse/chromedriver")

