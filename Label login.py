from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

import time



# ตั้งค่า browser
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

try:
    # เปิดหน้า login
    driver.get("https://www.infinitybarcode.com")

    username = 'zawtest'
    password = 'zawtest'

    # รอจน element ของฟอร์ม login โหลดเสร็จ
    wait = WebDriverWait(driver, 3)

    time.sleep(2)
    user = driver.find_element(By.ID, "txtUserName")
    pas = driver.find_element(By.ID, "txtPassword")
    user.send_keys(username)
    pas.send_keys(password)

    time.sleep(2)
    login = driver.find_element(By.XPATH, '//*[@id="fmlogin"]/table/tbody[2]/tr/td/table/tbody/tr[5]/td/input[1]')
    login.click()


    print("✅ เข้าสู่ระบบสำเร็จ (URL เปลี่ยนไปแล้ว)")
    print("✅ หน้า dashboard พร้อมใช้งาน")


    time.sleep(5)
    # ให้เลือก dropdown list เพื่อทำการ search
    # รอให้ dropdown ปรากฏ
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mlabel-mlabeltype"]'))
    )

    # 👉 ใส่กรอบสีแดงก่อนคลิก
    driver.execute_script("arguments[0].style.border='3px solid red'", dropdown_element)

    # 👉 คลิก dropdown
    dropdown_element.click()

    # 👉 เลือก option
    dropdown = Select(dropdown_element)
    dropdown.select_by_value("U")

    time.sleep(5)
    # กดปุ่ม search
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submitItem"]'))
    )

    # 👉 ใส่กรอบสีแดงให้ปุ่ม
    driver.execute_script("arguments[0].style.border='3px solid red'", submit_button)

    # 🕐 รอสักครู่เพื่อให้เห็นกรอบแดง

    time.sleep(5)

    # 👉 คลิกปุ่ม Submit
    submit_button.click()

    time.sleep(3)
    # ทำการออกจากระบบ
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1-5"]'))
    )
    time.sleep(5)
    # 👉 ใส่กรอบสีแดงให้ปุ่ม
    driver.execute_script("arguments[0].style.border='3px solid red'", logout_button)

    # 🕐 รอสักครู่เพื่อให้เห็นกรอบแดง

    time.sleep(3)

    # 👉 คลิกปุ่ม Submit
    logout_button.click()

    print("✅ logout successful")

except TimeoutException:
    driver.save_screenshot("login_failed.png")
    print("⛔ ระบบล็อกอินไม่สำเร็จ หรือ Timeout")

except Exception as e:
    print(f"⛔ เกิดข้อผิดพลาด: {e}")

    # driver.close() --ปิดหน้าต่าง window

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys
# import time
#
#
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
#
# driver.get("https://www.infinitybarcode.com")
#
# username = 'zawtest'
# password = 'zawtes'
#
# # รอให้ฟอร์มล็อกอินโหลด
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtUserName")))
#
# user = driver.find_element(By.ID, "txtUserName")
# pas = driver.find_element(By.ID, "txtPassword")
#
# user.send_keys(username)
# pas.send_keys(password)
# driver.find_element(By.XPATH, '//*[@id="fmlogin"]/table/tbody[2]/tr/td/table/tbody/tr[5]/td/input[1]').click()
#
# # รอให้หน้าเว็บโหลด
# time.sleep(2)
#
# # ตรวจสอบข้อความแสดงข้อผิดพลาด
# page_source = driver.page_source
# if "users" in page_source or "รหัสผ่าน" in page_source:
#     print("⛔ ล็อกอินไม่สำเร็จ: ใส่รหัสผิด")
# else:
#     current_url = driver.current_url
#     print("📍 URL หลัง login:", current_url)
#     if "expected_url" in current_url:
#         print("✅ ล็อกอินสำเร็จ")
#     else:
#         print("⚠️ สถานะไม่แน่ชัด: กรุณาตรวจสอบด้วยตนเอง")




