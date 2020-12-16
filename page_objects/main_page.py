from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.login_page import LoginPage
from page_objects.signup_page import SignUpPage


class MainPage(object):
    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver
        try:
            self.web_driver.maximize_window()
        except WebDriverException:
            pass
        self.web_driver.get("https://demo.diprella.com/")
        self.diprella_logo = WebDriverWait(self.web_driver, 25).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".logo__icon"))
         )

        self.login_button = self.web_driver.find_element_by_css_selector("a.header__nav-link[href*='/sign-in']")
        self.sign_up_button = self.web_driver.find_element_by_css_selector("a[href*='/sign-up']")
        self.start_studying_button = self.web_driver.find_element_by_xpath("(//span[@class='student']/ancestor::div)[1]")
        self.start_teaching_button = self.web_driver.find_element_by_xpath("(//span[@class='lecturer']/ancestor::div"
                                                                           ")[1]")

    @allure.step("Click on the Sign Up button")
    def click_on_sign_up_button(self):
        self.sign_up_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return SignUpPage(self.web_driver)

    @allure.step("Click on the Sign In button")
    def click_on_login_link(self):
        self.login_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return LoginPage(self.web_driver)

    @allure.step("Click on the Start Studying button")
    def click_on_start_studying_button(self):
        self.start_studying_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return SignUpPage(self.web_driver)

    @allure.step("Click on the Start Teaching button")
    def click_on_start_studying_button(self):
        self.start_teaching_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return SignUpPage(self.web_driver)
