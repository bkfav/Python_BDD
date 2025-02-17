from selenium import webdriver


def get_chrome_browser():
    driver = webdriver.Chrome()
    return driver
def get_browser(webdriver_type):
    if webdriver_type == "edge":
        driver = webdriver.Edge()
    elif webdriver_type == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver