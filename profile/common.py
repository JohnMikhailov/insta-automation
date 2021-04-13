from time import sleep
from typing import Set

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


def get_users_amount(link_text: str):
    """
        текущий формат текста ссылки: 'n подписчиков'
    """

    return int(link_text.split()[0].rstrip())


def fetch_nicknames_from_list(browser, users_amount, window_with_list) -> Set[str]:
    print('users need to fetch:', users_amount)

    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.TAG_NAME, value='li'))

    list_element_surrounding = window_with_list.find_element(By.CLASS_NAME, value='d7ByH')

    action = ActionChains(browser)
    action.click(list_element_surrounding).perform()

    users_meta = []
    while len(users_meta) < users_amount - 1:
        action.send_keys(Keys.PAGE_DOWN).perform()
        wait.until(lambda p: p.find_element(By.TAG_NAME, value='li'))
        users_meta = window_with_list.find_elements(By.TAG_NAME, value='li')

        print('done:', f'{round((len(users_meta) / users_amount) * 100, 1)}%')

        sleep(0.3)  # to slow down server spamming

    user_nicknames = window_with_list.find_elements(By.CLASS_NAME, value='FPmhX.notranslate._0imsa')
    return set(elem.text for elem in user_nicknames)


def get_followers_nicknames(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='zwlfE'))
    profile_main_buttons = browser.find_element(By.CLASS_NAME, value='zwlfE')

    followers_number_as_button = profile_main_buttons.find_element(
        By.PARTIAL_LINK_TEXT,
        value='подписчиков'
    )

    followers_amount = get_users_amount(followers_number_as_button.text)
    followers_number_as_button.click()

    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='isgrP'))

    followers_list_window = browser.find_element(By.CLASS_NAME, value='isgrP')

    followers_nicknames = fetch_nicknames_from_list(
        browser,
        followers_amount,
        followers_list_window
    )

    return followers_nicknames


def close_window_with_users_list(browser):
    ActionChains(browser).send_keys(Keys.ESCAPE).perform()


def get_subs_nicknames(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='zwlfE'))
    profile_main_buttons = browser.find_element(By.CLASS_NAME, value='zwlfE')

    subscriptions_number_as_button = profile_main_buttons.find_element(
        By.PARTIAL_LINK_TEXT,
        value='подписок'
    )

    subs_amount = get_users_amount(subscriptions_number_as_button.text)
    subscriptions_number_as_button.click()

    wait.until(lambda p: p.find_element(By.CLASS_NAME, value='isgrP'))

    subscriptions_list_window = browser.find_element(By.CLASS_NAME, value='isgrP')

    subs_nicknames = fetch_nicknames_from_list(
        browser,
        subs_amount,
        subscriptions_list_window
    )

    return subs_nicknames
