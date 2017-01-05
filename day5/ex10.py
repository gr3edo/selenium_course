import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/")

    name = driver.find_element_by_css_selector("#box-campaigns .name").text #get product name
    old_price = driver.find_element_by_css_selector("#box-campaigns .regular-price").text #get old price
    new_price = driver.find_element_by_css_selector("#box-campaigns .campaign-price").text #get new price

    #check styles on main page - gray, crossed, small
    assert driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("color") == "rgba(119, 119, 119, 1)"
    assert driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("text-decoration") == "line-through"
    assert driver.find_element_by_css_selector("#box-campaigns .regular-price").value_of_css_property("font-size") == "14.4px"
    #check styles on main page - red, bold, big
    assert driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("color") == "rgba(204, 0, 0, 1)"
    assert driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("font-weight") == "bold"
    assert driver.find_element_by_css_selector("#box-campaigns .campaign-price").value_of_css_property("font-size") == "18px"

    driver.find_element_by_xpath("//div[@id='box-campaigns']//li[1]").click() #open first item in Campaign
    product_page_name = driver.find_element_by_css_selector("#box-product h1").text #get product page name

    assert name == product_page_name

    product_page_old_price = driver.find_element_by_css_selector("#box-product .regular-price").text
    product_page_new_price = driver.find_element_by_css_selector("#box-product .campaign-price").text

    # check styles on product page - gray, crossed, small
    assert driver.find_element_by_css_selector("#box-product .regular-price").value_of_css_property("color") == "rgba(102, 102, 102, 1)"
    assert driver.find_element_by_css_selector("#box-product .regular-price").value_of_css_property("text-decoration") == "line-through"
    assert driver.find_element_by_css_selector("#box-product .regular-price").value_of_css_property("font-size") == "16px"
    # check styles on product page - red, bold, big
    assert driver.find_element_by_css_selector("#box-product .campaign-price").value_of_css_property("color") == "rgba(204, 0, 0, 1)"
    assert driver.find_element_by_css_selector("#box-product .campaign-price").value_of_css_property("font-weight") == "bold"
    assert driver.find_element_by_css_selector("#box-product .campaign-price").value_of_css_property("font-size") == "22px"

    assert old_price == product_page_old_price
    assert new_price == product_page_new_price