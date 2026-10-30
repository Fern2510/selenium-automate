from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

# ตั้งค่า browser
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://archiving.infinityrp.com")

    time.sleep(3)
    # กรอกข้อมูล login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "signin_username"))
    ).send_keys("test_aware")

    driver.find_element(By.ID, "signin_password").send_keys("test_@ware")

    # เก็บ URL ก่อน login
    start_url = driver.current_url

    # คลิก login
    (driver.find_element(By.XPATH, '//*[@id="UserloginAddForm"]/table/tbody/tr[8]/td[2]/div/button').click())

    # รอให้ URL เปลี่ยน
    WebDriverWait(driver, 10).until(EC.url_changes(start_url))

    # ตรวจสอบ URL ปัจจุบัน
    current_url = driver.current_url
    print("📍 URL หลัง login:", current_url)

    # ตรวจสอบว่า URL เป็นหน้า dashboard หรือไม่
    page_text = driver.page_source

    if "displayMainCategory" in current_url:
        print("✅ ล็อกอินสำเร็จ: เข้าสู่ Dashboard แล้ว")

        time.sleep(5)
        element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="menu"]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a/img'))
        )
        # print("➡️ กำลังคลิกรูปภาพเพื่อไปยังหน้ารายละเอียด...")
        # element.click()
        # print("✅ คลิกสำเร็จ")

        driver.execute_script("arguments[0].style.border='3px solid red'", element)
        print("🖱️ กำลังคลิก...")
        element.click()
        print("✅ คลิกสำเร็จ")

        time.sleep(5)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="menu"]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table[3]/tbody/tr[1]/td[2]/strong/a'))
        )

        driver.execute_script("arguments[0].style.border='3px solid red'", element)
        print("🖱️ กำลังคลิก...")
        element.click()
        print("✅ คลิกสำเร็จ")

        time.sleep(5)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,'//*[@id="menu"]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table[3]/tbody/tr/td/a/img'))
        )

        driver.execute_script("arguments[0].style.border='3px solid red'", element)
        print("🖱️ กำลังคลิก...")
        element.click()
        print("✅ คลิกสำเร็จ")
        #การ search หาคำ

        time.sleep(5)
        # ... search_box + search_button
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="topRightKeyword"]'))
        )
        search_box.send_keys("DIOR")

        time.sleep(5)
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="SigninDisplayForm"]/table/tbody/tr[2]/td[2]/button'))
        )
        driver.execute_script("arguments[0].style.border='3px solid red'", search_button)
        search_button.click()

        time.sleep(5)
        # Logout
        logout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="menu"]/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td/a/img'))
        )
        driver.execute_script("arguments[0].style.border='3px solid red'", logout)
        logout.click()
        print("✅ logout successful")


    elif "pages/display/1" in current_url:
        print("⛔ ล็อกอินไม่สำเร็จ: username หรือ password ผิด")
    else:
        print("⚠️ ล็อกอินไม่แน่ชัด: ต้องตรวจสอบเพิ่มเติม")

except TimeoutException:
    print("⛔ ระบบล็อกอินไม่สำเร็จ: Timeout หรือไม่เปลี่ยน URL")

except Exception as e:
    print(f"⛔ เกิดข้อผิดพลาด: {e}")


