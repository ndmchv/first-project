from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ndmchv.github.io/first-project/")
driver.set_window_size(1050, 840)
driver.find_element(By.NAME, "a").click()
driver.find_element(By.NAME, "a").send_keys("3")
driver.find_element(By.NAME, "b").click()
driver.find_element(By.NAME, "b").send_keys("44")
driver.find_element(By.XPATH, "/html/body/input[3]").click()

assert driver.find_element(By.XPATH, "/html/body/h1").text == "blablablablab blabla"

