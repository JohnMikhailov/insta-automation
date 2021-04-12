from time import sleep
from typing import List

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


def fetch_user_nicknames_from_list(browser, users_amount, window_with_list) -> List[str]:
    action = ActionChains(browser)
    action.send_keys([Keys.TAB] * 2).perform()

    users_meta = []
    while len(users_meta) < users_amount:
        tabs_by_list_item = 3
        items_available_at_once = 15
        tabs = tabs_by_list_item * items_available_at_once
        keys = [Keys.TAB] * tabs

        action.send_keys(keys).perform()

        users_meta = window_with_list.find_elements(By.TAG_NAME, value='li')

        sleep(1)

        print('found:', len(users_meta))

    user_nicknames = window_with_list.find_elements(By.CLASS_NAME, value='FPmhX.notranslate._0imsa')
    user_nicknames = [elem.text for elem in user_nicknames]

    print(user_nicknames)
    return user_nicknames


def get_follower_nicknames(browser):
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

    return fetch_user_nicknames_from_list(
        browser,
        followers_amount,
        followers_list_window
    )
