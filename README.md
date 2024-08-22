# <img src="https://brandslogos.com/wp-content/uploads/images/large/appium-logo.png" alt="Appium Logo" width="39" style ="display: block;, margin-top: 10px;"/> Automation Appium

## Selector Android

1. **AppiumBy.ID**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan resource-id Android.
    - **Contoh:**
      ```python
      (AppiumBy.ID, "com.example.app:id/username_input")
      ```

2. **AppiumBy.CLASS_NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan nama kelas Android.
    - **Contoh:**
      ```python
      (AppiumBy.CLASS_NAME, "android.widget.EditText")
      ```

3. **AppiumBy.ACCESSIBILITY_ID**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan content-description Android.
    - **Contoh:**
      ```python
      (AppiumBy.ACCESSIBILITY_ID, "login_button")
      ```

4. **AppiumBy.ANDROID_UIAUTOMATOR**
    - **Deskripsi:** Menggunakan UiAutomator string untuk mengidentifikasi elemen.
    - **Contoh:**
      ```python
      (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
      (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example.app:id/login_button")')
      ```

5. **AppiumBy.XPATH**
    - **Deskripsi:** Menggunakan XPath untuk mengidentifikasi elemen.
    - **Contoh:**
      ```python
      (AppiumBy.XPATH, "//android.widget.Button[@text='Login']")
      ```

6. **AppiumBy.NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan atribut "name" (biasanya sama dengan teks yang ditampilkan).
    - **Contoh:**
      ```python
      (AppiumBy.NAME, "Login")
      ```

7. **AppiumBy.TAG_NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan jenis widget Android.
    - **Contoh:**
      ```python
      (AppiumBy.TAG_NAME, "android.widget.Button")
      ```

## Contoh Penggunaan dengan Variable

```python
# Variable ID
# Di ambil dari APPIUM INSPECTOR
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_daftar = 'com.nunomics.app.debug:id/btnApply'
input_otp = 'com.nunomics.app.debug:id/firstPinView'

WebDriverWait(self.driver, 5).until(
    EC.visibility_of_element_located((AppiumBy.ID, field_nama))
)

WebDriverWait(self.driver, 10).until(
    EC.visibility_of_element_located((AppiumBy.ID, field_username))
)       

WebDriverWait(self.driver, 10).until(
    EC.visibility_of_element_located((AppiumBy.ID, field_email))
)
                    
WebDriverWait(self.driver, 10).until(
    EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
)
WebDriverWait(self.driver, 5).until(
    EC.visibility_of_element_located((AppiumBy.ID, field_pass))
)
WebDriverWait(self.driver, 5).until(
    EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
)
cb_kebijakan = WebDriverWait(self.driver, 12).until(
    EC.element_to_be_clickable((AppiumBy.ID, checkbox))
)                    
daftar = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
)
```