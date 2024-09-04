from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'uiautomator2' # insall uiautomator2 
options.udid = 'IFLZFAJJHASOEE95' # cara cek di cmd= adb devices 
options.device_name = 'POCO X6 Pro 5G'
options.app_package = 'com.nunomics.app' # cara cek di cmd= adb shell dumpsys window | find "mCurrentFocus"
options.app_activity = 'com.nunomics.app.ui.SplashActivity' # Acitivity di ambil di splashscreen
options.no_reset = False # noReset untuk memulai ulang aplikasi

appium_server_url = 'http://127.0.0.1:4723/wd/hub' # Appium Server

# Variable ID/checkbox/btn/XPATH
# Di ambil dari APPIUM INSPECTOR
btn_next = 'com.nunomics.app:id/btnNext'
btn_login = 'com.nunomics.app:id/btnLogin'

def open_app():
    try:
        driver = webdriver.Remote(appium_server_url, options=options)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, btn_next))
        ).click()
        print("Step 1: Klik tombol 'Mulai Sekarang'")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, btn_login))
        ).click()
        print("Step 2: Klik tombol 'Masuk' ")
        return driver  # Kembalikan driver

    except Exception as e:
        print(f"Terjadi kesalahan saat inisialisasi: {e}")
        return None
    
if __name__ == "__main__":
    open_app()