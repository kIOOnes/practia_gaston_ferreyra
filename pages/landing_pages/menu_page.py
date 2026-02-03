from core.elements import Elements
from selenium.webdriver.common.by import By
import time

# -------------------------
# LOCATORS
# -------------------------

OPEN_CATEGORIES_MENU = (By.CSS_SELECTOR, '[data-js="nav-menu-categories-trigger"]')
HEADER_CATEGORY = (By.XPATH,"//b[contains(@class,'ui-category-trends-header-title-category-name')]")
BREADCRUMB_TITLE = (By.CSS_SELECTOR,"h1.ui-search-breadcrumb__title, h2.ui-search-breadcrumb__title")
BREADCRUMB_CATEGORY_NAME = (By.XPATH,"//span[@itemprop='name']")
RESULTS_QUANTITY_LABEL = (By.XPATH,"//span[contains(@class,'ui-search-search-result__quantity-results') and contains(text(),'resultados')]")

SELECT_TECNOLOGIA = (By.XPATH, "//a[normalize-space()='Tecnología']")
SELECT_TECNOLOGIA_ACCESORIOS = (By.XPATH, "//a[normalize-space()='Accesorios para Celulares']")

SELECT_CONSTRUCCION = (By.XPATH, "//a[normalize-space()='Construcción']")
SELECT_CONSTRUCCION_VER_MAS = (By.XPATH, "//a[normalize-space(text())='Ver más']")
SHOW_BAÑOS_Y_SANITARIOS_MOSTRAR_MAS = (By.XPATH,"//a[@title='Mostrar más' and normalize-space()='Mostrar más']")
MODAL_GRIFERIA_PARA_BAÑO = (By.XPATH, "//span[contains(@class,'andes-modal__title') and normalize-space()='Categorías']")
GRIFERIA_BAÑO_OPTION = (By.XPATH,"//span[contains(@class,'ui-search-search-modal-filter-name') and normalize-space()='Grifería para Baño']")

SELECT_OFERTAS_MENU = (By.XPATH,"//a[normalize-space()='Ofertas']")
SELECT_OFERTAS_DEL_DIA_FILTER = (By.XPATH,"//section[@aria-labelledby='promotion_type-title']//span[contains(normalize-space(.), 'Oferta del día')]")
OFERTAS_TITLE = (By.XPATH,"//div[contains(@class,'carousel_header')]//h1[normalize-space()='Ofertas']")

SELECT_SUPERMERCADOS = (By.XPATH, "//ul[@class='nav-categs-departments']/li/a[normalize-space()='Supermercado']")
SELECT_GONDOLAS_MENU = (By.XPATH, "//li[contains(@class,'ui-ms-profile__item') and contains(., 'Góndolas')]")
SELECT_DESPENSA = (By.LINK_TEXT, "Despensa")
SHOW_VER_TODA_LA_GONDOLA = ("xpath", "//section[@aria-label='Despensa']//a[normalize-space()='Ver toda la góndola']")

TOTAL_RESULTS = (By.CSS_SELECTOR, "span.ui-search-search-result__quantity-results")


# -------------------------
# PAGE OBJECT
# -------------------------

class menuPage:
    def __init__(self, driver):
        self.driver = driver
        self.elm = Elements(driver)

    def select_tecnologia_accesorios_celulares(self):
        self.elm.click(OPEN_CATEGORIES_MENU)
        self.elm.click(SELECT_TECNOLOGIA)
        self.elm.click(SELECT_TECNOLOGIA_ACCESORIOS)  

    def select_griferia_para_baño(self):
        self.elm.click(OPEN_CATEGORIES_MENU)
        self.elm.click(SELECT_CONSTRUCCION)
        self.elm.click(SELECT_CONSTRUCCION_VER_MAS)     
        self.elm.click(SHOW_BAÑOS_Y_SANITARIOS_MOSTRAR_MAS)
        self.elm.click_safe(GRIFERIA_BAÑO_OPTION)

    def select_ofertas_del_dia(self):
        self.elm.click(SELECT_OFERTAS_MENU)
        self.elm.click(SELECT_OFERTAS_DEL_DIA_FILTER)

    def select_supermercados_despensa(self):
        self.elm.click(OPEN_CATEGORIES_MENU)
        self.elm.click(SELECT_SUPERMERCADOS)
        time.sleep(5)
        self.elm.wait_for_element_clickable(SELECT_GONDOLAS_MENU)
        self.elm.move_to_element(SELECT_GONDOLAS_MENU)

        self.elm.wait_for_element_clickable(SELECT_DESPENSA)
        self.elm.click(SELECT_DESPENSA)
        time.sleep(5)
        
    def find_product_despensa(self, product_name):
        locator = (
            By.XPATH,
            f"//h3[contains(translate(., '{product_name.upper()}', '{product_name.lower()}'), '{product_name.lower()}')]/ancestor::a"
        )

        if self.elm.try_clickable(locator):
            self.elm.click(locator)
            return True
        else:
            print(f"No se encontró producto con '{product_name}' — test continúa")
            return False
        
    def is_ofertas_title_present(self):
        return self.elm.is_present(OFERTAS_TITLE)
    
    def get_header_category_text(self):
        return self.elm.get_text(HEADER_CATEGORY)
    
    def get_bread_crumb_title(self):
        return self.elm.get_text(BREADCRUMB_TITLE)
    
    def get_bread_crumb_category_name(self):
        return self.elm.get_text(BREADCRUMB_CATEGORY_NAME)
    
    def get_total_products_in_category(self):
        amount_text = self.elm.get_text(TOTAL_RESULTS)
        amount = amount_text.split()[0]
        amount = amount.replace(".", "")
        return int(amount)

    def results_is_presents(self):
        return self.elm.is_present(RESULTS_QUANTITY_LABEL)
    
    def get_griferia_filter_locator(self, filter_name: str):
        return (
            By.XPATH,
            f"//a[contains(@class,'ui-search-link') and "
            f".//span[contains(@class,'ui-search-filter-name') "
            f"and normalize-space()='{filter_name}']]"
        )

    def apply_griferia_filter(self, filter_name: str):
        locator = self.get_griferia_filter_locator(filter_name)
        self.elm.click_safe(locator)