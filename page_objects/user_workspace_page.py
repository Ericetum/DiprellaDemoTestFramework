import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UserWorkSpacePage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver
        self.diprella_logo = WebDriverWait(self.web_driver, 25).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".logo__icon"))
        )
        self.user_menu = self.web_driver.find_element_by_css_selector("a.home__header-nav-link.ng-star-inserted")
        self.main_tab_button = self.web_driver.find_element_by_xpath("//a[@routerlink='/']")
        self.courses_management_tab_button = self.web_driver.find_element_by_xpath("//a[@routerlink='/courses"
                                                                                   "-management/dashboard/main']")
        self.bookmarks_tab_button = self.web_driver.find_element_by_xpath("//a[@routerlink='/bookmarks']")
        self.profile_tab_button = self.web_driver.find_element_by_css_selector(".nav-link.ng-star-inserted")
        self.search_field = self.web_driver.find_element_by_id("search")
        self.profile = None

    @property
    def search_results(self):
        if "deviceName" in self.web_driver.desired_capabilities.keys():
            self.web_driver.find_elements_by_css_selector("[aria-controls=search]").click()
        return self.web_driver.find_elements_by_css_selector(".search-result") \
            if "deviceName" in self.web_driver.desired_capabilities.keys() \
            else self.web_driver.find_elements_by_class_name('course-box-container-content')

    @allure.step("Searching for the next pattern: {1}")
    def search(self, request):
        self.search_field.send_keys(request)
        ActionChains(self.web_driver).send_keys(Keys.ENTER).perform()
        return self

    @allure.step("Opening profile page")
    def click_on_profile(self):
        self.user_menu.click()
        self.profile = self.web_driver.find_elements_by_css_selector("a.user__dropdown-link")[1]
        self.profile.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self
