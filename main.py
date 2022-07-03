from webbrowser import Chrome
from numpy import mat
from selenium import webdriver
import time
user = input('请输入账号')
web = webdriver.Chrome()
web.get('http://fzszbh.101.com/uc-component/index.html?sdp-app-id=79cbf433-ed09-4947-90e1-09cbef4ede33#/login?redirect_uri=%2F%2Ffzszbh.101.com%2Fwjt%2Ffzszbhxq%2Fuc11CB%3Freturnurl%3Dhttp%253A%252F%252Fs.fzszbh.101.com%252F')
web.implicitly_wait(5)
time.sleep(2)
web.find_element_by_xpath('//*[@id="account101"]').send_keys(str(user))
web.find_element_by_xpath('//*[@id="password"]').send_keys('Abc123456')
web.find_element_by_xpath('//*[@id="agreementCheck"]').click()
web.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div/div[1]/form/div[3]/button').click()
time.sleep(5)
web.find_element_by_xpath('//*[@id="zoom-tip"]/p/a').click()
web.find_element_by_xpath('//*[@id="js_nav"]/li[6]/a/span').click()
web.switch_to.window(web.window_handles[1])
time.sleep(3)
web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div/div/div/a/div').click()
time.sleep(3)
web.switch_to.window(web.window_handles[2])
time.sleep(5)
web.find_element_by_xpath('//*[@id="waterfall"]/div[2]/span/a/div').click()
time.sleep(2)
web.find_element_by_xpath("//*[contains(text(),'进入问卷')]").click()
time.sleep(3)
tr = web.find_elements_by_xpath("//*[contains(@value,'0001')]")
text = web.find_elements_by_xpath("//*[contains(@class,'textInput') and contains(@name,'cq')]")
for i in tr:
    i.click()
    time.sleep(1)
for t in text:
    t.send_keys('非常好！！！')

input()
