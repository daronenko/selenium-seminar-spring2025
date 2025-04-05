from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.feed_page import FeedPage
from ui.pages.people_page import PeoplePage
from ui.pages.schedule_page import SchedulePage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import os


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def feed_page(driver):
    return FeedPage(driver=driver)


@pytest.fixture
def people_page(driver):
    return PeoplePage(driver=driver)


@pytest.fixture
def schedule_page(driver):
    return SchedulePage(driver=driver)


@pytest.fixture(scope='session')
def credentials() -> dict[str, str]:
    return {
        'email': os.environ.get('VKEDU_EMAIL'),
        'password': os.environ.get('VKEDU_PASSWORD')
    }


@pytest.fixture(scope='session')
def cookies(credentials, driver) -> list[dict]:
    login_page = LoginPage(driver)
    login_page.login(credentials['email'], credentials['password'])
    return driver.get_cookies()

