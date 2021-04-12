from profile.common import open_profile, get_follower_nicknames
from profile.login import login, close_popups_after_login



def find_unfollowers(browser):  # noqa
    # with browser:
    login(browser)
    close_popups_after_login(browser)
    open_profile(browser)
    get_follower_nicknames(browser)
