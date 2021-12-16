from selenium import webdriver
import time
import math

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector("button.btn").click()

	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	x = browser.find_element_by_id("input_value")
	x = x.text

	def calc(x):
  		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)

	input = browser.find_element_by_id("answer")
	input.send_keys(y)

	submit = browser.find_element_by_css_selector("button.btn").click()

finally:
	time.sleep(15)
	browser.quit()




