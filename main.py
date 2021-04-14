from app.browser import chrome
from app.config import config
from profile.subs_info import subscribtions_info


subscribtions_info(chrome, result_path=config.REPORT_PATH)
