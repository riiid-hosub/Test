from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('#gb_70').click()

action.send_keys('hosub.lee@riiid.co').perform()
action.reset_actions()
driver.find_element_by_css_selector('.CwaK9').click()

time.sleep(2)
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('operation1@')
driver.find_element_by_css_selector('.CwaK9').click()
time.sleep(2)

driver.get('https://mail.google.com/mail/u/0/?ogbl#inbox')
time.sleep(2)

driver.find_element_by_css_selector('.T-I.J-J5-Ji.T-I-KE.L3').click()
time.sleep(1)

send_buton = driver.find_element_by_css_selector('.gU.Up')

(
action.send_keys('hosub.lee@riiid.co').key_down(Keys.ENTER).pause(2).key_down(Keys.TAB)
.send_keys('Subject').pause(2).key_down(Keys.TAB)
.send_keys('abcde').pause(2).key_down(Keys.ENTER)
.key_down(Keys.SHIFT).send_keys('abcde').key_up(Keys.SHIFT).pause(2)
.move_to_element(send_buton).click()
.perform()
)