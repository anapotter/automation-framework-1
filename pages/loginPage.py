class LoginPage():

	def __init__(self, driver): #constructor, always be called when creating object for this class
		self.driver = driver

		self.username_textbox_id = "txtUsername"
		self.password_textbox_id = "txtPassword"
		self.login_button_id = "btnLogin"

	def enter_username(self, username):
		self.driver.find_element_by_id(self.username_textbox_id).clear()
		self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)