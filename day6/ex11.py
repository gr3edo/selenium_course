import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart")
    driver.find_element_by_xpath(".//*[@id='box-account-login']//tr[5]//a").click()
    text_temp = "11113"
    email_temp = text_temp + "@a.a"
    pswd_temp = "qweqwe"

    driver.find_element_by_name("tax_id").send_keys(text_temp) #enter taxID
    driver.find_element_by_name("company").send_keys(text_temp) #enter company
    driver.find_element_by_name("firstname").send_keys(text_temp) #enter first
    driver.find_element_by_name("lastname").send_keys(text_temp) #enter last
    driver.find_element_by_name("address1").send_keys(text_temp) #enter addr1
    driver.find_element_by_name("address2").send_keys(text_temp) #enter addr2
    driver.find_element_by_name("postcode").send_keys(text_temp)  # enter postcode
    driver.find_element_by_name("city").send_keys(text_temp)  # enter city
    driver.find_element_by_name("email").send_keys(email_temp)  # enter email
    driver.find_element_by_name("phone").send_keys("+3801111111")  # enter phone
    driver.find_element_by_name("password").send_keys(pswd_temp)  # enter paswd
    driver.find_element_by_name("confirmed_password").send_keys(pswd_temp)  # enter pswd again
    driver.find_element_by_name("create_account").click()

    driver.find_element_by_xpath(".//*[@id='box-account']//li[4]/a").click() # logout

    # email_login = driver.find_element_by_name("email").clear()
    # email_login.send_keys(email_temp)
    # password_login = driver.find_element_by_name("password").clear()
    # password_login.send_keys(pswd_temp)

    driver.find_element_by_name("email").send_keys(email_temp)
    driver.find_element_by_name("password").send_keys(pswd_temp)

    driver.find_element_by_name("login").click()  # login
    driver.find_element_by_xpath(".//*[@id='box-account']//li[4]/a").click()  # logout
