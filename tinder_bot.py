import time
from selenium import webdriver
from variable import number
from variable import password

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://tinder.com/');
time.sleep(5)
login_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_btn.click()

time.sleep(3)
fb_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_btn.click()
#ポップアップ画面変更
base_window = driver.window_handles[0]
driver.switch_to_window(driver.window_handles[1])

email_in = driver.find_element_by_xpath('//*[@id="email"]')
email_in.send_keys(number)

pw_in = driver.find_element_by_xpath('//*[@id="pass"]')
pw_in.send_keys(password)

login_btn2 = driver.find_element_by_xpath('//*[@id="u_0_0"]')
login_btn2.click()

driver.switch_to_window(base_window)
time.sleep(3)

cookie = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookie.click()

time.sleep(2)

popup_1 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
popup_1.click()

popup_2 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
popup_2.click()

time.sleep(10)

like_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
dislike_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')



for i in range(10):
    like_btn.click()
    time.sleep(1)
