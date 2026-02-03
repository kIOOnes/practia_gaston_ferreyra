import pytest
from pages.landing_pages.menu_page import menuPage
import time
import allure

@allure.feature("Navigation by Category")
@allure.story("Tecnologia")
@allure.title("Select Accesorios para Celulares category and validate breadcrumbs")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("navigation", "category", "tecnologia")
def test_select_accesorios_celulares(driver):

    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------
    
    landing_page = menuPage(driver)
    
    # -------------------------
    # Act
    # -------------------------

    landing_page.select_tecnologia_accesorios_celulares()

    # -------------------------
    # Assert
    # -------------------------
    
    header_category = landing_page.get_header_category_text()
    bread_crumb_title = landing_page.get_bread_crumb_title()
    bread_crumb_category_name = landing_page.get_bread_crumb_category_name()
    
    assert header_category == "Accesorios para Celulares"
    assert bread_crumb_title == "Accesorios para Celulares"
    assert bread_crumb_category_name == "Celulares y Teléfonos"
    assert landing_page.results_is_presents


@allure.feature("Navigation by Category")
@allure.story("Construccion")
@allure.title("Select Griferia para Baño category and validate results")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("navigation", "category", "griferia")
def test_select_griferia_para_baño(driver):

    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------    
    
    landing_page = menuPage(driver)

    # -------------------------
    # Act
    # -------------------------

    landing_page.select_griferia_para_baño()

    # -------------------------
    # Assert
    # -------------------------

    bread_crumb_title = landing_page.get_bread_crumb_title()
    assert bread_crumb_title == "Grifería para Baño"
    assert landing_page.results_is_presents


@allure.feature("Special Sections")
@allure.story("Deals")
@allure.title("Open Ofertas del Dia and validate assert")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("navigation", "category", "ofertas de dia")
def test_ofertas_del_dia(driver):
    
    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------    
    
    landing_page = menuPage(driver)
    
    # -------------------------
    # Act
    # -------------------------

    landing_page.select_ofertas_del_dia()

    # -------------------------
    # Assert
    # -------------------------

    time.sleep(5)

    assert landing_page.is_ofertas_title_present()


@allure.feature("Product Search")
@allure.story("Supermercado")
@allure.title("Find product containing 'capsulas' in despensa")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("navigation", "capsulas")
def test_supermercados_capsulas(driver):

    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------    
    
    landing_page = menuPage(driver)
    
    # -------------------------
    # Act
    # -------------------------

    landing_page.select_supermercados_despensa()

    # -------------------------
    # Assert
    # -------------------------

    assert landing_page.find_product_despensa("capsulas")


@allure.feature("Category Metrics")
@allure.story("Results Counter")
@allure.title("Get total products in category and validate greater than zero")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("amount_results")
def test_get_total_products_in_category(driver):

    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------    
    
    landing_page = menuPage(driver)
    
    # -------------------------
    # Act
    # -------------------------

    landing_page.select_griferia_para_baño()
    time.sleep(5)
    total = landing_page.get_total_products_in_category()

    # -------------------------
    # Assert
    # -------------------------

    print(f"Total products found: {total}")

    assert total > 1, f"No products found — total results: {total}"


@pytest.fixture(params=[
    "Duchadores",
    "Griferías Convencionales",
    "Sets Completos",
    ])
def griferia_filter(request):
    return request.param
@allure.feature("Category Filters")
@allure.story("Griferia Filters")
@allure.title("Apply griferia filter and validate breadcrumb and results")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("filters", "parametrized")
def test_get_total_products_with_filter(driver,griferia_filter):
    allure.dynamic.parameter("filter", griferia_filter)
    # -------------------------
    # A-A-A TEST DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------    
    
    landing_page = menuPage(driver)
    
    # -------------------------
    # Act
    # -------------------------

    landing_page.select_griferia_para_baño()
    landing_page.apply_griferia_filter(griferia_filter)
    total = landing_page.get_total_products_in_category()
    
    # -------------------------
    # Assert
    # -------------------------

    bread_crumb_title = landing_page.get_bread_crumb_title()
    assert griferia_filter.lower() in bread_crumb_title.lower(), \
    f"El título no contiene el filtro aplicado: {griferia_filter}" 
    assert total > 0, "No se encontraron productos"