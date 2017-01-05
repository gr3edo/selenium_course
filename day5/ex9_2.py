from telnetlib import EC

import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    counter = 1
    countries = driver.find_elements_by_xpath("//tr[@class='row']/td[5]/a")

    for country in countries:
        counter += 1
        geo_zones = []
        driver.find_element_by_xpath(".//*[@id='content']/form/table/tbody/tr["+ str(counter) +"]/td[5]/a/i").click()
        list_gz = driver.find_elements_by_xpath(".//*[@id='table-zones']//tr[2]/td[3]/select")
        for zone in list_gz:
            under_zones = zone.find_elements_by_xpath(".//option")
            for under_zone in under_zones:
                geo_zones.append(under_zone.get_attribute("textContent"))
            geo_zones.pop(0)
            print(geo_zones)
        sorted_gz = sorted(geo_zones)
        assert sorted_gz == geo_zones
        driver.find_element_by_name("cancel").click()