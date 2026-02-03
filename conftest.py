import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.landing_pages.config_page import configPage
import allure


# -------------------------
# ALLURE SCREENSHOT ON FAIL
# -------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            try:
                png = driver.get_screenshot_as_png()

                allure.attach(
                    png,
                    name=f"screenshot_failure_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )

                allure.attach(
                    driver.page_source,
                    name="page_source",
                    attachment_type=allure.attachment_type.HTML
                )

            except Exception as e:
                print(f"Could not attach screenshot: {e}")


# -------------------------
# ENV OPTION
# -------------------------

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="Environment: prod | qa | dev"
    )


# -------------------------
# BASE URL
# -------------------------

@pytest.fixture(scope="session")
def base_url(request):

    env = request.config.getoption("--env")

    urls = {
        "prod": "https://www.mercadolibre.com.ar",
        "qa": "https://qa.mercadolibre.com",
        "dev": "https://dev.mercadolibre.com"
    }

    return urls[env]


# -------------------------
# DRIVER
# -------------------------

@pytest.fixture(scope="session")
def driver(base_url):

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(5)

    driver.get(base_url)

    try:
        config_page = configPage(driver)
        config_page.accept_cookies()
    except:
        pass

    yield driver

    driver.quit()

@pytest.fixture(autouse=True)
def go_home_each_test(driver, base_url):
    driver.get(base_url)

    try:
        config_page = configPage(driver)
        config_page.accept_cookies()
    except:
        pass