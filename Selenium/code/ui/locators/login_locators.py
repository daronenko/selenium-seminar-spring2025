from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BTN_LOCATOR = (By.CLASS_NAME, 'gtm-auth-header-btn')
    CONTINUE_WITH_CREDS_BTN_LOCATOR = (By.CLASS_NAME, 'gtm-signup-modal-link')
    EMAIL_INPUT_LOCATOR = (By.ID, 'email')
    PASSWORD_INPUT_LOCATOR = (By.ID, 'password')
    SUBMIT_BTN_LOCATOR = (By.CLASS_NAME, 'gtm-login-btn')
