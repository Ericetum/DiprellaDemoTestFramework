from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import allure
from page_objects.user_workspace_page import UserWorkSpacePage


class LoginPage(object):
    def __init__(self, web_driver: WebDriver):

        self.web_driver = web_driver
        self.close_button = WebDriverWait(self.web_driver, 25).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div.page__close.page__close_login"))
        )
        self.diprella_logo = self.web_driver.find_element_by_css_selector(".page-logo")
        self.google_login_button = self.web_driver.find_element_by_id("googleButton")
        self.facebook_login_button = self.web_driver.find_element_by_css_selector('a.social__icons-box-link.facebook')
        self.linkedin_login_button = self.web_driver.find_element_by_css_selector('a.social__icons-box-link.linkedin')
        self.username_field = self.web_driver.find_element_by_xpath("//input[@formcontrolname='email']")
        self.password_field = self.web_driver.find_element_by_xpath("//input[@formcontrolname='password']")
        self.login_button = self.web_driver.find_element_by_xpath("//button[@type='submit']")
        self.register_button = self.web_driver.find_element_by_css_selector("div.image-container-btn.white--btn--hover")

    @allure.step("Enter username: {1}")
    def enter_login(self, email):
        self.username_field.send_keys(email)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Filling in the password")
    def enter_password(self, password):
        self.password_field.send_keys(password)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Clicking on the Login Button")
    def click_on_login_button(self):
        self.web_driver.execute_script("arguments[0].click()", self.login_button)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return UserWorkSpacePage(self.web_driver)

    @allure.step("Clicking on the Register Button")
    def click_on_register_button(self):
        from page_objects.signup_page import SignUpPage
        self.web_driver.execute_script("arguments[0].click()", self.register_button)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return SignUpPage(self.web_driver)
