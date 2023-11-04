import logging
import time

from .base_page import BasePage
from locators.locators import Locators


class OperationsHelper(BasePage):
    locators = Locators()

    def filling_fields(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    # INPUT TEXT
    def input_login(self, word):
        self.filling_fields(self.locators.LOCATOR_LOGIN_FIELD, word, description="login form")

    def input_password(self, word):
        self.filling_fields(self.locators.LOCATOR_PASS_FIELD, word, description="password form")

    def add_title(self, string):
        self.filling_fields(self.locators.LOCATOR_TITLE, string, description="title")

    def add_description(self, string):
        self.filling_fields(self.locators.LOCATOR_DESCRIPTION, string, description="description")

    def add_content(self, string):
        self.filling_fields(self.locators.LOCATOR_CONTENT, string, description="content")

    def add_name(self, string):
        self.filling_fields(self.locators.LOCATOR_CONTACT_NAME, string, description="contact_name")

    def add_email(self, string):
        self.filling_fields(self.locators.LOCATOR_CONTACT_EMAIL, string, description="contact_email")

    def add_content_contact(self, string):
        self.filling_fields(self.locators.LOCATOR_CONTACT_CONTENT, string, description="contact_content")

    # GET TEXT
    def new_post_title(self):
        return self.get_text_from_element(self.locators.LOCATOR_FIND_NEW_POST, description="new_post_title")

    def get_error_text(self):
        return self.get_text_from_element(self.locators.LOCATOR_ERROR_FIELD, description="error label")

    def login_success(self):
        return self.get_text_from_element(self.locators.LOCATOR_HELLO, description="username")

    def get_alert_message(self):
        time.sleep(2)
        logging.info("Get alert message")
        text = self.get_alert_text()
        logging.debug(f"Alert message is {text}")
        return text

# CLICK
    def click_save_button(self):
        self.click_button(self.locators.LOCATOR_SAVE_BTN, description="save")

    def click_add_post_button(self):
        self.click_button(self.locators.LOCATOR_NEW_POST_BTN, description="new post")

    def click_contact(self):
        self.click_button(self.locators.LOCATOR_CONTACT_SEND, description="contact")

    def click_contact_button(self):
        self.click_button(self.locators.LOCATOR_CONTACT_BTN, description="send")

    def click_login_button(self):
        self.click_button(self.locators.LOCATOR_LOGIN_BTN, description="login")
