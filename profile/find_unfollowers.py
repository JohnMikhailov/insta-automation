from profile.common import open_profile, get_followers_nicknames, get_subs_nicknames, close_window_with_users_list
from profile.login import login, close_popups_after_login



def subscribtions_info(browser):  # noqa
    with browser:
        login(browser)
        close_popups_after_login(browser)
        open_profile(browser)
        # f = get_followers_nicknames(browser)
        # close_window_with_users_list(browser)
        s = get_subs_nicknames(browser)
        close_window_with_users_list(browser)

        # friends = f & s
        # i_am_not_follow = f - s
        # not_follow_me_back = s - f
        #
        # print('not follow me', not_follow_me_back)
        # print('i am not follow', i_am_not_follow)
        # print('friends', friends)
