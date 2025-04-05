from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BTN = (By.CLASS_NAME, 'gtm-auth-header-btn')
    CONTINUE_WITH_CREDS_BTN = (By.CLASS_NAME, 'gtm-signup-modal-link')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BTN = (By.CLASS_NAME, 'gtm-login-btn')
