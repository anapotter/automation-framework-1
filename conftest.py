import pytest

def pytest_addoption(parser):
	parser.addoption("--browser", action="store", default="chrome", help="Type in browser name ex. chrome or firefox")


@pytest.fixture(scope="class")
	#class functions have to include self
def test_setup(request):
	from selenium import webdriver

	browser = request.config.getoption("--browser")
	
	if browser == 'chrome':
		driver = webdriver.Chrome(executable_path='/Users/anaqnx/chromedriver')
	elif browser == 'firefox'
		driver = webdriver.Firefox(executable_path='/Users/anaqnx/geckodriver')
	driver.implicitly_wait(10)
	driver.maximize_window()
	request.cls.driver = driver
	yield
	driver.close()
	driver.quit()
	print("Test completed")