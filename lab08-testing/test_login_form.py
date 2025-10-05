import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///C:/Users/Nam/Desktop/NHAPMONCNPM/lab04-loginform/login.html")
        self.driver.maximize_window()
        print("\n🚀 Bắt đầu test:", self._testMethodName)

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
        print("✅ Kết thúc test:", self._testMethodName)
        print("--------------------------------------------------")

    def test_empty_fields(self):
        """Kiểm tra khi để trống Username và Password"""
        driver = self.driver
        driver.find_element(By.CLASS_NAME, "login-btn").click()
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Vui lòng nhập Username và Password!")
        alert.accept()
        print("📋 Mô tả: Kiểm tra cảnh báo khi người dùng để trống Username/Password.")
        print("🎯 Kết quả: Hiển thị thông báo 'Vui lòng nhập Username và Password!'")

    def test_invalid_login(self):
        """Kiểm tra đăng nhập sai thông tin"""
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("user")
        driver.find_element(By.ID, "password").send_keys("wrong")
        driver.find_element(By.CLASS_NAME, "login-btn").click()

        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Sai Username hoặc Password!")
        alert.accept()
        print("📋 Mô tả: Kiểm tra khi nhập sai Username/Password.")
        print("🎯 Kết quả: Hiển thị thông báo 'Sai Username hoặc Password!'")

    def test_valid_login(self):
        """Kiểm tra đăng nhập hợp lệ"""
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("123")
        driver.find_element(By.CLASS_NAME, "login-btn").click()

        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Đăng nhập thành công!")
        alert.accept()
        print("📋 Mô tả: Kiểm tra khi nhập đúng thông tin đăng nhập.")
        print("🎯 Kết quả: Hiển thị thông báo 'Đăng nhập thành công!'")

    def test_cancel_button(self):
        """Kiểm tra nút Hủy (Cancel) có reset form không"""
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("someuser")
        driver.find_element(By.ID, "password").send_keys("somepass")
        driver.find_element(By.ID, "remember").click()

        driver.find_element(By.CLASS_NAME, "cancel-btn").click()

        self.assertEqual(driver.find_element(By.ID, "username").get_attribute("value"), "")
        self.assertEqual(driver.find_element(By.ID, "password").get_attribute("value"), "")
        self.assertFalse(driver.find_element(By.ID, "remember").is_selected())

        print("📋 Mô tả: Kiểm tra nút 'Cancel' có xóa toàn bộ thông tin đã nhập không.")
        print("🎯 Kết quả: Form được reset về trạng thái ban đầu.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
