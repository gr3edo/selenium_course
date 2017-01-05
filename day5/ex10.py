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

    name = driver.find_element_by_css_selector("#box-campaigns .name")
    name = name.text # get product name
    old_price = driver.find_element_by_css_selector("#box-campaigns .regular-price")
    old_price = old_price.text #get old price
    new_price = driver.find_element_by_css_selector("#box-campaigns .campaign-price")
    new_price = new_price.text #get new price

    #проверить на главной странице стили цен

    driver.find_element_by_xpath("//div[@id='box-campaigns']//li[1]").click() #open first item in Campaign

    product_page_name = driver.find_element_by_css_selector("#box-product h1")
    product_page_name = product_page_name.text #get product page name

    product_page_old_price = driver.find_element_by_css_selector("#box-product .regular-price")
    product_page_old_price = product_page_old_price.text
    product_page_new_price = driver.find_element_by_css_selector("#box-product .campaign-price")
    product_page_new_price = product_page_new_price.text

    #проверить на странице продукта стили цен

    assert name == product_page_name
    assert old_price == product_page_old_price
    assert new_price == product_page_new_price