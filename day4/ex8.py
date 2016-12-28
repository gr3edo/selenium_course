import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/")

    items = driver.find_elements_by_css_selector(".image-wrapper div")

    items_counter = 0
    for item in items:
        is_element_present(driver, By.CSS_SELECTOR, ".image-wrapper div")

def is_element_present(driver, *args):
    return len(driver.find_elements(*args)) == 1