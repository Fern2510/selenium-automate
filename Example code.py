# การเรียกใช้ selenium และใช้เพื่อการกำหนด element ต่างๆ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

# เปิด Browser
options = webdriver.ChromeOptions()
# เป็นการตั้งค่าให้ browser ทำงานในโหมดที่สามารถแยกตัวเองออกจาก web driver ได้ หลังทำงานเสร็จแล้ว browser จะไม่ถูกปิดอัตโนมัติ
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

# เปิด web page

driver.get('http://google.com')
driver.get('https://pypi.org/project/selenium/')
# driver.back()
# driver.forward()
# driver.refresh()


# การระบุ element หรือตำแหน่ง
# element = driver.find_element(By.ID, '')
# element1 = driver.find_element(By.CLASS_NAME,'')
# element2 = driver.find_element(By.TAG_NAME,'')
element3 = driver.find_element(By.LINK_TEXT,'Help')
# element4 = driver.find_element(By.XPATH,'//*[@id="txtUserName"]')

# คำสั่งการกระทำบนเว็บไซต์
# การคลิก (Click)
time.sleep(10)
btn1 = driver.find_element(By.XPATH, '//*[@id="user-indicator"]/nav[1]/ul/li[1]/a')
btn1.click()
print("✅ Go to Help page successfully")

