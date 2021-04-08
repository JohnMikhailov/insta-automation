from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.config import config


def open_profile(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='gmFkV'))
    profile_icon_as_button = browser.find_element(By.CLASS_NAME, value='gmFkV')
    profile_icon_as_button.click()


def open_followers_list(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='zwlfE'))
    profile_main_buttons = browser.find_element(By.CLASS_NAME, value='zwlfE')
    followers_number_as_button = profile_main_buttons.find_element(
        By.PARTIAL_LINK_TEXT,
        value='подписчиков'
    )
    followers_number_as_button.click()
