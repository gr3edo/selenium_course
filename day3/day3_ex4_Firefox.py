import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    pass