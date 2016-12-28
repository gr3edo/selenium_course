import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    # sidebar = driver.find_elements_by_css_selector("#app-")
    sidebar = driver.find_element_by_id("box-apps-menu")
    sidebar_item = sidebar.find_elements_by_tag_name("li")

    for counter in sidebar_item:
        counter.find_element_by_tag_name("a").click()


