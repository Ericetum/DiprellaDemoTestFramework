from config.test_conf import Config

from page_objects.main_page import MainPage


def get_browser():
    for i in Config.webdrivers:
        yield i


def get_main_page(browser):
    print(f"Browser: {Config.webdrivers[browser].name}")
    webdriver = Config.webdrivers[browser](command_executor=Config.grid_address) if "Remote" in Config.webdrivers[
        browser].name or "Android" in Config.webdrivers[browser].name or "IOS" in Config.webdrivers[browser].name else \
        Config.webdrivers[browser]()
    return MainPage(webdriver.web_driver)
