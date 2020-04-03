from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import configparser
import os
#===============================================
config = configparser.ConfigParser()
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config.read(os.path.join(path, 'config.ini'))
etoro_account = config['ETORO']['ACCOUNT']
etoro_password = config['ETORO']['PASSWORD']
#===============================================


# options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
# options.add_argument("--start-maximized")     #最大化視窗
# options.add_argument("--incognito")           #開啟無痕模式



driver = webdriver.Firefox(firefox_options=Options())

def login():
    #login etoro account
    driver.get("https://www.etoro.com/")
    time.sleep(1)
    # account_input = driver.find_element_by_css_selector("input#username")
    # account_input.send_keys(etoro_account)
    # password_input = driver.find_element_by_css_selector("input#password")
    # password_input.send_keys(etoro_password)
    # sign_in_btn = driver.find_elements_by_css_selector("div.w-login-btn-wrapp")

    # sign_in_btn[-1].click()
    # time.sleep(1)

login()

    # login_btn = driver.find_elements_by_css_selector("button#login-sts-btn-sign-in")
    # print(login_btn)
    # time.sleep(1)

    # driver.close()