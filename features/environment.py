from Webdriver import webdriver
import logging

def before_all(context):
    browser_type = context.config.userdata.get("browser")
    context.browser_type = browser_type

def before_feature(context, feature):
    #context.driver =  webdriver.get_chrome_browser()
    context.driver =  webdriver.get_browser(context.browser_type)
    context.driver.maximize_window()

def after_feature(context, feature):
    context.driver.quit

"""def before_all(context):
    print("Before all")

def after_all(context):
    print("After all")

def before_scenario(context, scenario):
    print("Before Scenario")

def after_scenario(context, scenario):
    print("After Scenario")

def before_step(context, step):
    print("Before step")

def after_step(context, step):
    print("After step")
"""