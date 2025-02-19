from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logs import log_file

log = log_file.get_logs()
TIMEOUT = 5

class SeleniumHelper:
    def __init__(self,driver):
        self.driver = driver
    def without_quote(self,input_text):
        return input_text.strip("\"")
    def open_page(self, pageURL):
        flag = False
        try:
            self.driver.get(pageURL)
            flag = True
            log.info(f"Successfully navigated to page {pageURL}")
        except Exception as e:
            log.error(f"Unable to navigate to page {pageURL} with exception: {e}")
        return flag
    def click(self,locator):
        flag = False
        try:
            self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()
            log.info(f"{locator} element is clicked")
            flag = True
        except Exception as e:
            log.error(f"Element {list(locator.values())[0]} is not found with exception: {e}")
        return flag
    def visible(self,locator):
        flag = False
        try:
            assert self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).is_displayed
            log.info(f"Label is visible in {locator}")
            flag = True
        except Exception as e:
            log.error(f"Element {list(locator.values())[0]} is not found with exception: {e}")
        return flag
    def verify_Label(self,locator,input_text):
        flag = False
        try:
            assert self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).text.casefold() == input_text.casefold()
            log.info(f"{input_text} is available in {locator}")
            flag = True
        except Exception as e:
            log.error(f"Element {list(locator.values())[0]} is not found with exception: {e}")
        return flag
    def fill_value(self,locator,input_text):
        flag = False
        try:
            self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)
            log.info(f"{input_text} value is filled in {locator}")
            flag = True
        except Exception as e:
            log.error(f"Element {list(locator.values())[0]} is not found with exception: {e}")
        return flag
    def wait_till_element_is_present(self,locator,timeout):
        flag = False
        try:
            log.info(f"Waiting {timeout} seconds for element {list(locator.values())[0]} presence")
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((list(locator.keys())[0], list(locator.values())[0])))
            flag = True
            log.info(f"Element is found")
        except Exception as e:
            log.error(f"Element {list(locator.values())[0]} is not found after waiting {timeout} seconds with exception: {e}")
            #print(f"Exception while checking element {e}")
        return flag
    
    
    #def OnHomePage(self):
    #    assert self.driver.find_element(By.CSS_SELECTOR,"a[href='/'][style='color: orange;']").is_displayed
    
    def signUpPageTitle(self):
        assert self.driver.find_element(By.XPATH,"//*[@id=\"form\"]/div/div/div[3]/div/h2").text == "New User Signup!"
    def fillUserName(self, username):
        try:
            uname = self.driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-name']") #WebDriverWait(self.driver,TIMEOUT).until(EC.presence_of_element_located(By.CSS_SELECTOR,"input[data-qa='signup-name']"))
            uname.send_keys(username)
        except:
            print("Timeout for finding username")
    def fillPassword(self, pwd):
        try:
            passwd = self.driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-email']") #WebDriverWait(self.driver,TIMEOUT).until(EC.presence_of_element_located(By.CSS_SELECTOR,"input[data-qa='signup-email']"))
            passwd.send_keys(pwd)
        except:
            print("Timeout for finding password")  
    def clickSignUpBtn(self):
        try:
            signupBtn = self.driver.find_element(By.CSS_SELECTOR,"button[data-qa='signup-button'")#WebDriverWait(self.driver,TIMEOUT).until(EC.element_to_be_clickable(By.CSS_SELECTOR,"button[data-qa='signup-button'"))
            signupBtn.click()
        except:
            print("Timeout for finding sign-up button")    
    def assertSignup(self):
        self.driver.implicitly_wait(10)
        assert self.driver.find_element(By.CSS_SELECTOR,'h2.title').text == 'ENTER ACCOUNT INFORMATION' 
