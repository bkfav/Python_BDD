from behave import *
from Helper.SeleniumHelper import SeleniumHelper
from Locators import locator
from Logs import log_file
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log = log_file.get_logs()

@when('Navigate to url {HomePageURL}')
def step_impl(context,HomePageURL):
    status = SeleniumHelper(context.driver).open_page(SeleniumHelper(context.driver).without_quote(HomePageURL))
    assert status is True, context.driver.get_screenshot_as_file("Screenshots/OpenPageIssue-%s.png" % now)
@then('Verify that home page is visible successfully')
def step_impl(context):
    status = SeleniumHelper(context.driver).visible(locator.Label_OnHome)
    print(context.text)
    assert status is True, context.driver.get_screenshot_as_file("Screenshots/HomePageNotVisible-%s.png" % now)

@when('Click on "Signup / Login" button')
def step_impl(context):
    #SeleniumHelper(context.driver).clickSignupBtn()
    status = SeleniumHelper(context.driver).wait_till_element_is_present(locator.Label_signup_login,10)
    assert status is True, context.driver.get_screenshot_as_file("Screenshots/Signup_Login_Link_NotClickable-%s.png" % now)
    SeleniumHelper(context.driver).click(locator.Label_signup_login)
    
@then('Verify {NewUser_title_text} is shown')
def step_impl(context,NewUser_title_text):
    status = SeleniumHelper(context.driver).verify_Label(locator.Label_New_User_Signup,SeleniumHelper(context.driver).without_quote(NewUser_title_text))
    assert status is True, context.get_screenshot_as_file("Screenshots/"+status+"_NotFound-%s.png" % now)
@given('Enter "{name}" and "{email}" address')
def step_impl(context,name,email):
   status = SeleniumHelper(context.driver).fill_value(locator.InputField_Signup_Name,name) 
   assert status is True, context.driver.get_screenshot_as_file("Screenshots/Name_Element_NotFound-%s.png" % now) 
   status = SeleniumHelper(context.driver).fill_value(locator.InputField_Signup_Email,email)
   assert status is True, context.driver.get_screenshot_as_file("Screenshots/Email_Element_NotFound-%s.png" % now)
   
@when('Click "Signup" button')
def step_impl(context):
   status = SeleniumHelper(context.driver).click(locator.Btn_Signup)
   assert status is True, context.driver.get_screenshot_as_file("Screenshots/Signup_Button_NotFound-%s.png" % now)
 
@then('Verify that {title_text} is visible')
def step_impl(context,title_text):
    status = SeleniumHelper(context.driver).wait_till_element_is_present(locator.Label_Enter_Account_Information,10)
    assert status is True, context.driver.get_screenshot_as_file("Screenshots/Enter_Account_Information_TitleText_Element_NotFound-%s.png" % now)
    status = SeleniumHelper(context.driver).verify_Label(locator.Label_Enter_Account_Information,SeleniumHelper(context.driver).without_quote(title_text))
    assert status is True, context.driver.get_screenshot_as_file("Screenshots/Enter_Account_Information_Text_NotMatched-%s.png" % now)