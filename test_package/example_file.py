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

    sidebar = driver.find_elements_by_css_selector("#app-")

    main_menu_counter = 0
    for item in sidebar:
        main_menu_counter += 1
        sub_menu_counter = 0
        driver.find_element_by_xpath('//ul[@id="box-apps-menu"]/li['+ str(main_menu_counter) +']').click()
        are_elements_present(driver, By.XPATH, ".//*[@id='app-']//li")
        sidebar_sub_item = driver.find_elements_by_css_selector("#app- li")
        for sub_item in sidebar_sub_item:
            sub_menu_counter += 1
            driver.find_element_by_xpath('.//*[@id="app-"]//li[' + str(sub_menu_counter) + ']').click()


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0

