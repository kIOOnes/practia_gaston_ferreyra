from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class Elements:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_and_click(self, hover_locator, click_locator):
        hover_element = self.wait.until(EC.visibility_of_element_located(hover_locator))
        ActionChains(self.driver).move_to_element(hover_element).perform()
        click_element = self.wait.until(EC.element_to_be_clickable(click_locator))
        click_element.click()

    def move_to_element(self, locator):
        
        element = self.wait.until(EC.visibility_of_element_located(locator))
        
        ActionChains(self.driver).move_to_element(element).perform()    

    def send_keys(self, locator, text, clear_first=True):
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def wait_for_element_clickable(self, locator, timeout=10, poll_frequency=0.5):
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            print(f"[WARN] Elemento {locator} no clickeable en {timeout} segundos")
            return False

    def click_if_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
            return True
        except TimeoutException:
            return False
    
    def click_safe(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
            )

            element.click()
            return True
        except TimeoutException:
            print(f"[ERROR] No clickeable: {locator}")
            return False

    def is_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_enabled(self, locator, timeout=30, poll_frequency=0.5):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            print(f"[WARN] Elemento {locator} no habilitado en {timeout} segundos")
            return False
        
    def try_clickable(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            if element.is_enabled() and element.is_displayed():
                return True
            else:
                return False

        except (TimeoutException, NoSuchElementException):
            return False

    def get_text(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except TimeoutException:
            print(f"[FAIL] Elemento {locator} no visible en {timeout} segundos")
            return None