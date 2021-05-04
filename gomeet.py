from selenium import webdriver
import selenium

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Load Chrome with default setttings
opt = Options()
opt.add_argument('start-maximized')
opt.add_argument('--disable-extensions')
opt.add_experimental_option('prefs', { \
    'profile.default_content_setting_values.media_stream_mic': 1,
    'profile.default_content_setting_values.media_stream_camera': 1,
    'profile.default_content_setting_values.geolocation': 1,
    'profile.default_content_setting_values.notifications': 1
})

def gomet(num):
    driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe', options=opt)
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 20)

    driver.get('https://app.gotomeeting.com/index.html?meetingId='+num)

    time.sleep(3)
    u = 1
    while u< 2:
        try:

            body = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body')))
            driver.find_element_by_xpath('''//button[.='Save and continue']''').click()
            u = False
        except:
            driver.refresh()
        u+=1

    time.sleep(3)
    u = 1
    while u <2 :
        try:

            body = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body')))
            driver.find_element_by_xpath('''//button[.='Save and continue']''').click()
        except:
            driver.refresh()
        u+=1

    time.sleep(3)
    u = True
    while u:
        try:

            body = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Share microphone after join"]')))
            driver.find_element_by_css_selector('button[aria-label="Share microphone after join"]').click()
            u = False
        except:
            driver.refresh()
    time.sleep(3)
    driver.find_element_by_css_selector('button[aria-label="Share camera after join"]').click()
    try:

        driver.find_element_by_css_selector('''//button[.='Join when session starts']''').click()
    except:


        a = driver.find_elements_by_xpath("//button[@type='button']")
        a[-1].click()
    u = True
    while u:
        try:
            #time.sleep(60)
            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Share microphone after join"]')))
            driver.find_element_by_xpath('''//input[@data-automation-id="change-name-and-email-dialog__edit-name"]''').send_keys('muhammed basil shah')
            driver.find_element_by_xpath("//button[@type='submit']").click()
            u = False

        except:
            time.sleep(900)

    u =True
    while u:
        try:
            total_num = driver.find_elements_by_xpath("//button[@type='button']")[2]
            tot = total_num.text.split('+')
            totatt = tot[0]
            total_number = int(totatt)

            print(total_number)
            u = False
        except:
            time.sleep(60)
            pass


    a = True
    while a:
        try:
            time.sleep(3)
            current_coun = total_num.text
            print(current_coun)
        except:
            break
        try:
            current_count = int(current_coun)
            if current_count > total_number:
                total_number = current_count
            if current_count < 3:
                driver.get('https://www.google.com/')
                driver.__exit__()

                break
            if current_count < (total_number / 2):
                driver.get('https://www.google.com/')
                driver.__exit__()
                break
        except:
            pass
    driver.__exit__()








