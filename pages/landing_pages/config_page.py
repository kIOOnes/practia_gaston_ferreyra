from core.elements import Elements
from selenium.webdriver.common.by import By

# -------------------------
# LOCATORS
# -------------------------

ACCEPT_COOKIES_BTN = (By.XPATH, "//button[contains(.,'Aceptar')]")

# -------------------------
# CONFIG FUNCTIONS
# -------------------------

class configPage:

    def __init__(self, driver):
        self.driver = driver
        self.elm = Elements(driver)

    def accept_cookies(self):
        self.elm.click_if_present(ACCEPT_COOKIES_BTN)