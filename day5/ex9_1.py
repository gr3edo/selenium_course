from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    country = get_array_of_countries(driver)
    sorted_country = sorted(country)

    assert (country == sorted_country)

    # develop timezones check

    countries = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr[@class='row']")
    counter = 1
    for i in countries:
        counter += 1
        tz = driver.find_element_by_xpath(".//*[@id='content']/form/table/tbody/tr["+ str(counter) +"]/td[6]")
        tz = tz.text
        if int(tz) > 0:
            driver.find_element_by_xpath(".//*[@id='content']/form/table/tbody/tr[" + str(counter) + "]/td[7]/a").click()
            tz_countries = driver.find_elements_by_xpath(".//*[@id='table-zones']/tbody/tr/td[3]/input")
            tz_countries_array = []
            for element in tz_countries:
                tz_countries_array.append(element.get_attribute("value"))
            tz_countries_array.pop()
            sorted_tz_countries = sorted(tz_countries_array)
            assert (tz_countries_array == sorted_tz_countries)
            print(sorted_tz_countries)
            driver.find_element_by_name("cancel").click()

def get_array_of_countries(driver):
    item = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody//td[5]/a")
    country = []
    for element in item:
        country.append(element.text)
    return country