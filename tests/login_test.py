from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

	@pytest.fixture(scope="class")
	#class functions have to include self
	def test_setup(self):
		global driver
		driver = webdriver.Chrome(executable_path='/Users/anaqnx/chromedriver')
		driver.implicitly_wait(10)
		driver.maximize_window()
		yield
		driver.close()
		driver.quit()
		print("Test completed")

	def test_login(self, test_setup):
		driver = self.driver
		driver.get(utils.URL)
		login = LoginPage(driver)
		login.enter_username(utils.USERNAME)
		login.enter_password(utils.PASSWORD)
		login.click_login()
		
		# driver.find_element_by_id("txtPassword").send_keys("admin123")
		# driver.find_element_by_id("btnLogin").click()

	def test_logout(self, test_setup):
		try:
			driver = self.driver
			homepage = HomePage(driver) #create object of HomePage
			homepage.click_welcome()
			homepage.click_logout()
			x = driver.title
			assert x == "OrangeHRM" #true assertion
		except AssertionError as error:
			print("Assertion error occured")
			print(error)
			currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
			testName = utils.whoami()
			#raise #will be shown as failure
			screenshotName = testName + "_" + currTime
			allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
			driver.get_screenshot_as_file("/Users/anaqnx/Desktop/udemyselenium/AutomationFramework1/screenshots" + screenshotName + ".png") #selenium fucntion
			raise
		except:
			print("Some exception occured")
			#raise
		else:
			print("No exceptions occured")
		finally:
			print("This block will always execute | Close DB") #close DB connections in this finally block
	
# if __name__ == '__main__':
# 	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/anaqnx/Desktop/udemyselenium/SampleProjectTwo/Reports'))