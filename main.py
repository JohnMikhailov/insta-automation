from selenium import webdriver
from selenium.webdriver.common.by import By


from dotenv import load_dotenv
from os import environ


from time import sleep


url = 'https://www.instagram.com/'

load_dotenv()


browser = webdriver.Chrome(executable_path='/usr/local/webdrivers/chromedriver89')
browser.get(url)
sleep(1)

username = browser.find_element(By.NAME, value='username')
password = browser.find_element(By.NAME, value='password')

username.send_keys('ivamnikhailov')
password.send_keys(environ.get('PASSWORD'))

submit_button = browser.find_element(By.CLASS_NAME, value='Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB')
submit_button.click()

sleep(2)

not_now_button = browser.find_element(By.CLASS_NAME, value='sqdOP.yWX7d.y3zKF')
not_now_button.click()

sleep(3)
disable_notifications_button = browser.find_element(By.CLASS_NAME, value='aOOlW.HoLwm')
disable_notifications_button.click()
