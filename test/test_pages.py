import random
import string

import allure
import pytest


class TestPages(object):

    @allure.title("Verify that Diprella main page is correctly displayed")
    @pytest.mark.regression
    @pytest.mark.test_main_page
    def test_main_page(self, main_page, email, password):
        assert main_page.diprella_logo.is_displayed(), "Diprella Logo is not displayed"
        assert main_page.login_button.is_displayed(), "Login Button is not displayed on the page"
        assert main_page.sign_up_button.is_displayed(), "Sign Up button is not displayed on the page"
        assert main_page.start_studying_button.is_displayed(), "Start Studying button is not displayed on the page"
        assert main_page.start_teaching_button.is_displayed(), "Start Teaching button is not displayed on the page"

    @allure.title("Verify that Diprella login page is correctly displayed")
    @pytest.mark.regression
    @pytest.mark.test_login_page
    def test_login_page(self, main_page, email, password):
        login_page = main_page.click_on_login_link()

        assert login_page.diprella_logo.is_displayed(), "Diprella Logo is not displayed"
        assert login_page.google_login_button.is_displayed(), "Google signin button is not displayed"
        assert login_page.google_login_button.is_enabled(), "Google signin button is not clickable"
        assert login_page.facebook_login_button.is_displayed(), "Facebook signin button is not displayed"
        assert login_page.facebook_login_button.is_enabled(), "Facebook signin button is not clickable"
        assert login_page.linkedin_login_button.is_displayed(), "LinkedIn signin button is not displayed"
        assert login_page.linkedin_login_button.is_enabled(), "LinkedIn signin button is not clickable"
        assert login_page.username_field.is_displayed(), "Username input field is not displayed"
        assert login_page.password_field.is_displayed(), "Password field is not displayed"
        assert login_page.login_button.is_displayed(), "Login submit button is not displayed"
        assert login_page.login_button.is_enabled(), "Login submit button is not clickable"
        assert login_page.register_button.is_displayed(), "Register button is not displayed"
        assert login_page.register_button.is_enabled(), "Register button is not clickable"
        assert login_page.close_button.is_displayed(), "Close button is not displayed"
        assert login_page.close_button.is_enabled(), "Close button is not clickable"

    @allure.title("Verify that Diprella logins with correct credentials")
    @pytest.mark.regression
    @pytest.mark.test_login_process
    def test_login_process(self, main_page, email, password):
        login_page = main_page.click_on_login_link()
        workspace_page = login_page.enter_login(email) \
            .enter_password(password) \
            .click_on_login_button()
        assert workspace_page.diprella_logo.is_displayed(), "Diprella Logo is not displayed"
        assert workspace_page.main_tab_button.is_displayed(), "Main tab button is not displayed"
        assert workspace_page.courses_management_tab_button.is_displayed(), "Courses management tab is not displayed"
        assert workspace_page.bookmarks_tab_button.is_displayed(), "Bookmarks tab is not displayed"
        assert workspace_page.profile_tab_button.is_displayed(), "Profile tab is not displayed"
        assert workspace_page.user_menu.is_displayed(), "User menu is not displayed"

    @allure.title("Verify that Diprella signup page shows correctly")
    @pytest.mark.regression
    @pytest.mark.test_signup_page
    def test_signup_page(self, main_page, email, password):
        signup_page = main_page.click_on_sign_up_button()

        assert signup_page.diprella_logo.is_displayed(), "Diprella Logo is not displayed"
        assert signup_page.google_login_button.is_displayed(), "Google signup button is not displayed"
        assert signup_page.facebook_login_button.is_displayed(), "Facebook signup button is not displayed"
        assert signup_page.linkedin_login_button.is_displayed(), "LinkedIn signup button is not displayed"
        assert signup_page.first_name_field.is_displayed(), "First Name input field is not displayed"
        assert signup_page.last_name_field.is_displayed(), "Last Name input field is not displayed"
        assert signup_page.email_field.is_displayed(), "Email input field is not displayed"
        assert signup_page.password_field.is_displayed(), "Password field is not displayed"
        assert signup_page.terms_checker.is_displayed(), "Agree to terms checker is not displayed"
        assert signup_page.register_button.is_displayed(), "Registration submit button is not displayed"
        assert not signup_page.register_button.is_enabled(), "Registration submit button is enabled"

    @allure.title("Verify that signing up by email leads to the workspace page")
    @pytest.mark.regression
    @pytest.mark.test_signup_by_email
    def test_signup_by_email(self, main_page, email, password):
        sign_up_page = main_page.click_on_sign_up_button()
        first_name = ''.join(random.choices(string.ascii_letters, k=10))
        last_name = ''.join(random.choices(string.ascii_letters, k=10))
        password = ''.join(random.choices(string.ascii_letters, k=20))
        email = f"{''.join(random.choices(string.ascii_letters, k=10))}@gmail.com"

        workspace_page = sign_up_page.enter_first_name(first_name).enter_last_name(last_name).enter_email(
           email).enter_password(password).check_on_terms().click_on_register_button()

        assert workspace_page.diprella_logo.is_displayed(), "Diprella Logo is not displayed"
        assert workspace_page.main_tab_button.is_displayed(), "Main tab button is not displayed"
        assert workspace_page.courses_management_tab_button.is_displayed(), "Courses management tab is not displayed"
        assert workspace_page.bookmarks_tab_button.is_displayed(), "Bookmarks tab is not displayed"
        assert workspace_page.profile_tab_button.is_displayed(), "Profile tab is not displayed"
        assert workspace_page.user_menu.is_displayed(), "User menu is not displayed"

    @allure.title("Verify that Diprella search finds patterns which is present on the page")
    @pytest.mark.regression
    @pytest.mark.test_search_existing
    def test_search_existing(self, main_page, email, password):
        search_pattern = "pdf"
        search_results = main_page \
            .click_on_login_link() \
            .enter_login(email) \
            .enter_password(password) \
            .click_on_login_button() \
            .search(search_pattern) \
            .search_results

        assert len(search_results), f"Search results for query '{search_pattern}' are not shown"

    @allure.title("Verify that Login -> Register link is working correctly")
    @pytest.mark.regression
    @pytest.mark.test_login_to_signup
    def test_login_to_signup(self, main_page, email, password):
        login_page = main_page.click_on_login_link()
        signup_page = login_page.click_on_register_button()

        assert signup_page.diprella_logo.is_displayed(), "Diprella Logo is not displayed"
        assert signup_page.google_login_button.is_displayed(), "Google signup button is not displayed"
        assert signup_page.facebook_login_button.is_displayed(), "Facebook signup button is not displayed"
        assert signup_page.linkedin_login_button.is_displayed(), "LinkedIn signup button is not displayed"
        assert signup_page.first_name_field.is_displayed(), "First Name input field is not displayed"
        assert signup_page.last_name_field.is_displayed(), "Last Name input field is not displayed"
        assert signup_page.email_field.is_displayed(), "Email input field is not displayed"
        assert signup_page.password_field.is_displayed(), "Password field is not displayed"
        assert signup_page.terms_checker.is_displayed(), "Agree to terms checker is not displayed"
        assert signup_page.register_button.is_displayed(), "Registration submit button is not displayed"
        assert not signup_page.register_button.is_enabled(), "Registration submit button is enabled"

    @allure.title("Verify that Register -> Login link is working correctly")
    @pytest.mark.regression
    @pytest.mark.test_signup_to_login
    def test_signup_to_login(self, main_page, email, password):
        signup_page = main_page.click_on_sign_up_button()
        login_page = signup_page.click_on_login_button()

        assert login_page.diprella_logo.is_displayed(), "Diprella Logo is not displayed"
        assert login_page.google_login_button.is_displayed(), "Google signin button is not displayed"
        assert login_page.google_login_button.is_enabled(), "Google signin button is not clickable"
        assert login_page.facebook_login_button.is_displayed(), "Facebook signin button is not displayed"
        assert login_page.facebook_login_button.is_enabled(), "Facebook signin button is not clickable"
        assert login_page.linkedin_login_button.is_displayed(), "LinkedIn signin button is not displayed"
        assert login_page.linkedin_login_button.is_enabled(), "LinkedIn signin button is not clickable"
        assert login_page.username_field.is_displayed(), "Username input field is not displayed"
        assert login_page.password_field.is_displayed(), "Password field is not displayed"
        assert login_page.login_button.is_displayed(), "Login submit button is not displayed"
        assert login_page.login_button.is_enabled(), "Login submit button is not clickable"
        assert login_page.register_button.is_displayed(), "Register button is not displayed"
        assert login_page.register_button.is_enabled(), "Register button is not clickable"
        assert login_page.close_button.is_displayed(), "Close button is not displayed"
        assert login_page.close_button.is_enabled(), "Close button is not clickable"
