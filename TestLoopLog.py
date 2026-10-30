from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time

# ตั้งค่า browser
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

try:
    # เปิดหน้า login
    driver.get("https://www.igisonline.com/orders/")

    # สลับไปที่ frame "mainFrame" หลังจากโหลดหน้า
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "mainFrame"))
    )

    # กรอก username
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txtUserName"))
    ).send_keys("testaw")

    # กรอก password
    driver.find_element(By.ID, "txtPassword").send_keys("Testaw@08")

    # กดปุ่ม Login
    driver.find_element(By.ID, "login").click()

    # รอให้ URL เปลี่ยนหลังจาก login เสร็จ
    WebDriverWait(driver, 10).until(EC.url_changes("https://www.igisonline.com/orders/"))
    print("✅ เข้าสู่ระบบสำเร็จ (URL เปลี่ยนไปแล้ว)")

    # เช็ค URL ปัจจุบันหลังจาก URL เปลี่ยน
    print(f"URL หลังจากเปลี่ยน: {driver.current_url}")

    # หลังจาก URL เปลี่ยน, รอให้ element ในหน้าใหม่ปรากฏ
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ID, "menuMain"))  # หรือใช้ ID ที่เหมาะสมกับหน้าใหม่
    # )
    print("✅ หน้า dashboard พร้อมใช้งาน")

except TimeoutException:
    driver.save_screenshot("login_failed.png")
    print("⛔ ระบบล็อกอินไม่สำเร็จ หรือ Timeout")

except Exception as e:
    print(f"⛔ เกิดข้อผิดพลาด: {e}")


