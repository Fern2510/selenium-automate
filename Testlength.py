from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)



# สลับไปยัง frame login
driver.switch_to.frame("mainFrame")

# หา input username
username_field = driver.find_element(By.ID, "txtUserName")

# ดึง maxlength ถ้ามี
maxlength = username_field.get_attribute("maxlength")
print(f"🧪 maxlength ที่ระบบตั้งไว้: {maxlength}")

# กำหนดข้อความที่ยาวเกิน
long_input = "A" * 30  # 30 ตัวอักษร

# ส่งข้อความเข้าไป
username_field.send_keys(long_input)

# ตรวจสอบว่าถูกตัดเหลือเท่าไหร่
actual_value = username_field.get_attribute("value")
print(f"📥 ส่งค่าไป: {long_input}")
print(f"📤 ค่าใน input จริง: {actual_value}")

# ตรวจสอบความยาวจริง
if len(actual_value) < len(long_input):
    print("⚠️ ระบบตัดความยาวอัตโนมัติ")
else:
    print("✅ ระบบไม่จำกัด หรือยังรับข้อความครบ")
