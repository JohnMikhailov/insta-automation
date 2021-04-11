from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from app.config import config


def open_profile(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='gmFkV'))
    profile_icon_as_button = browser.find_element(By.CLASS_NAME, value='gmFkV')
    profile_icon_as_button.click()


def get_followers_amount(link_text: str):
    """
        текущий формат текста ссылки: 'n подписчиков'
    """

    return int(link_text.split()[0].rstrip())


def open_followers_list(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='zwlfE'))
    profile_main_buttons = browser.find_element(By.CLASS_NAME, value='zwlfE')
    followers_number_as_button = profile_main_buttons.find_element(
        By.PARTIAL_LINK_TEXT,
        value='подписчиков'
    )
    followers_amount = get_followers_amount(followers_number_as_button.text)
    followers_number_as_button.click()

    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='isgrP'))

    followers_list_window = browser.find_element(By.CLASS_NAME, value='isgrP')

    action = ActionChains(browser)
    action.send_keys([Keys.TAB]*2).perform()

    followers_meta = []
    while len(followers_meta) < followers_amount:
        action.send_keys([Keys.ARROW_DOWN]*(followers_amount//10)).perform()
        followers_meta = followers_list_window.find_elements(By.TAG_NAME, value='li')

        sleep(1)

    print('found:', len(followers_meta))
