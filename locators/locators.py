from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '// *[ @ id = "login"] / div[1] / label / input')
    LOCATOR_PASS_FIELD = (By.XPATH, '// *[ @ id = "login"] / div[2] / label / input')
    LOCATOR_ERROR_FIELD = (By.XPATH, '// *[ @ id = "app"] / main / div / div / div[2] / h2')
    LOCATOR_HELLO = (By.XPATH, '// *[ @ id = "app"] / main / nav / ul / li[3] / a')
    LOCATOR_NEW_POST_BTN = (By.XPATH, '// *[ @ id = "create-btn"]')
    LOCATOR_TITLE = (By.XPATH, '// *[ @ id = "create-item"] / div / div / div[1] / div / label / input')
    LOCATOR_DESCRIPTION = (By.XPATH, '// *[ @ id = "create-item"] / div / div / div[2] / div / label / span / textarea')
    LOCATOR_CONTENT = (By.XPATH, '// *[ @ id = "create-item"] / div / div / div[3] / div / label / span / textarea')
    LOCATOR_SAVE_BTN = (By.XPATH, '// *[ @ id = "create-item"] / div / div / div[7] / div / button / span')
    LOCATOR_FIND_NEW_POST = (By.XPATH, '// *[ @ id = "app"] / main / div / div[1] / h1')
    LOCATOR_CONTACT = (By.XPATH, '// *[ @ id = "app"] / main / div / div[1] / h1')
    LOCATOR_CONTACT_BTN = (By.XPATH, '// *[ @ id = "app"] / main / nav / ul / li[2] / a')
    LOCATOR_CONTACT_NAME = (By.XPATH, '// *[ @ id = "contact"] / div[1] / label / input')
    LOCATOR_CONTACT_EMAIL = (By.XPATH, '// *[ @ id = "contact"] / div[2] / label / input')
    LOCATOR_CONTACT_CONTENT = (By.XPATH, '// *[ @ id = "contact"] / div[3] / label / span / textarea')
    LOCATOR_CONTACT_SEND = (By.XPATH, '// *[ @ id = "contact"] / div[4] / button')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
