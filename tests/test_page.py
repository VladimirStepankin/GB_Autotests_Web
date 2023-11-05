import logging
from time import sleep
from pages.page import OperationsHelper
from yaml_reader import data


class TestPage:
    login = data['login']
    password = data['passwd']
    title = data['title']
    description = data['description']
    content = data['content']
    content_contact = data['content_contact']
    user_name = data['user_name']
    user_email = data['user_email']

    def test_auth_negative(self, browser):
        logging.info("Testing authorization_negative")
        page = OperationsHelper(browser)
        page.go_to_site()
        page.input_login("test")
        page.input_password("test")
        page.click_login_button()
        assert page.get_error_text() == "401", "test_auth_negative FAILED"

    def test_auth_success(self, browser):
        logging.info("Testing authorization_success")
        page = OperationsHelper(browser)
        page.go_to_site()
        page.input_login(self.login)
        page.input_password(self.password)
        page.click_login_button()
        assert page.login_success() == f"Hello, {self.login}", "test_auth_negative FAILED"

    def test_add_post(self, browser):
        logging.info("Testing add_post")
        page = OperationsHelper(browser)
        page.click_add_post_button()
        page.add_title(self.title)
        page.add_description(self.description)
        page.add_content(self.content)
        page.click_save_button()
        sleep(1)
        assert page.new_post_title() == f"{self.title}", "test_add_post FAILED"

    def test_contact_us(self, browser):
        logging.info("Testing contact_us")
        page = OperationsHelper(browser)
        sleep(1)
        page.click_contact_button()
        page.add_name(self.user_name)
        page.add_email(self.user_email)
        page.add_content_contact(self.content_contact)
        page.click_contact()
        assert page.get_alert_message() == "Form successfully submitted", "test_contact_us FAILED"
