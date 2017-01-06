import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    text_temp = "lorem ipsum 1"
    code_temp = "code01"

    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_xpath(".//*[@id='box-apps-menu']/li[2]/a").click() # open category
    driver.find_element_by_xpath(".//*[@id='content']/div[1]/a[2]").click() # click on add new product btn

    driver.find_element_by_xpath(".//*[@id='tab-general']//label[1]").click # enable product
    driver.find_element_by_xpath(".//*[@id='tab-general']//tr[2]//span/input").send_keys(text_temp) # enter name
    driver.find_element_by_xpath(".//*[@id='tab-general']/table/tbody/tr[3]//input").send_keys(code_temp) # enter code
    driver.find_element_by_xpath(".//*[@id='tab-general']//tr[4]//tr[2]/td[1]/input").click() # select category
    driver.find_element_by_xpath(".//*[@id='tab-general']/table//tr[7]//tr[3]//input").click() # select male product groups
    driver.find_element_by_css_selector("[name = quantity]").send_keys("1")# enter quantity
    driver.find_element_by_css_selector("[type = file]").send_keys("D:\pic.jpg") # upload image
    driver.find_element_by_css_selector("[name = date_valid_from]").send_keys(Keys.HOME + "06.01.2017") # date valid from
    driver.find_element_by_css_selector("[name = date_valid_to]").send_keys(Keys.HOME + "16.01.2017") # date valid to

    driver.find_element_by_xpath("//*[@id='content']//li[2]/a").click() # go to Information tab

