from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import datetime
import calendar
import pause
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





subjects = {'monday' : ['dc','oops','vlsi','rtos','dip'],
            'tuesday' : ['awp','awp','dc','rtos','es'],
            'wednesday' :['vlsi','es','awp','dc','oops'],
            'thursday' :['rtos','es','vlsi','dip','dc'],
            'friday' :['oops','dip','comp','comp','mentoring']
            }



def find_day():
    date = datetime.date.today()
    date = date.weekday()
    day = calendar.day_name[date]
    return day.lower()


#to find the current class
def find_class():
    day = find_day()
    classes = subjects[day]
    times = ['08:35-09:35', '09:35-10:35', '10:35-11:35', '11:35-12:35', '12:35-13:35']
    ftimes = ['08:35-09:20', '09:20-10:10', '10:10-11:00', '11:00-11:50', '11:50-12:30']
    time = str(datetime.datetime.now().time()).split(':')
    cls = ''
    ti = time[0]+':'+time[1]
    tiee = "08:35"
    if day == 'friday':
        for i in range(5):
            if ti >= ftimes[i].split('-')[0] and ti < ftimes[i].split('-')[1]:
                cls = classes[i]
                tim = ftimes[i].split('-')[1]
            elif ti > ftimes[4].split('-')[1]:
                exit()
    else:
        for i in range(5):
            if ti >= times[i].split('-')[0] and ti < times[i].split('-')[1]:
                cls = classes[i]
                tim = times[i].split('-')[1]
            elif ti > times[4].split('-')[1]:
                exit()

    return cls, tim





def leave_class():
    time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body')))
    print('strt')
    a = True
    while a:
        try:
            total_num = driver.find_element_by_xpath('//span[@class="wnPUne N0PJ8e"]')
            total_number = int(total_num.text)
            print(total_number)
            a = False
            
            print("leave")
        except:
            pass

    a = True
    while a:
        try :
            time.sleep(5)
            current_coun = total_num.text

        except:
            break
        try:
            current_count = int(current_coun)
            print(current_count,total_number / 2)
            if current_count > total_number:
                total_number = current_count
            if current_count < 2:
                print('get out')
                driver.find_element_by_css_selector('span.DPvwYc.JnDFsc.grFr5.FbBiwc').click()
                break
            if current_count < (total_number / 3):
                driver.find_element_by_css_selector('span.DPvwYc.JnDFsc.grFr5.FbBiwc').click()
                break
        except:
            pass

def gmail_login(mail,password):
    t = True
    while t:
        try:
            driver.get('https://accounts.google.com')
            element_mail = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body')))
            element_mail = wait.until(EC.visibility_of_element_located((By.ID, 'identifierId')))
            mail_box = driver.find_element_by_id('identifierId')
            mail_box.send_keys(mail)
            next_button = driver.find_element_by_class_name('VfPpkd-RLmnJb')
            next_button.click()
            element_pass = wait.until(
                EC.visibility_of_element_located((By.NAME, 'password')))
            pass_box = driver.find_element_by_name('password')
            pass_box.send_keys(password)
            next_button = driver.find_element_by_class_name('VfPpkd-RLmnJb')
            next_button.click()
            t = False
        except:
            pass

    f = True
    while f:
        try:
            time.sleep(3)
            element_nxt = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body')))
            f = False
        except:
            driver.refresh()


def enter_meet(mail,password,code):
    global driver,wait
    driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe', options=opt)
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 20)
    url = 'https://meet.google.com/' + code
    driver.get(url)
    time.sleep(3)
    b = True
    while b:
        try:
            element_body = wait.until(
                EC.visibility_of_element_located((By.XPATH, '/html/body')))
            time.sleep(6)
            ele = element_body.get_attribute("outerHTML")
            if "can't join" in ele:
                gmail_login(mail,password)
            b = False
        except:
            driver.refresh()

    c = True
    while c:
        try:
            print('strt')
            driver.get(url)
            time.sleep(4)
            try:
                join_button = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')))
                time.sleep(5)
            except:
                element_body = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body')))
                ele = element_body.get_attribute("outerHTML")
                if "It's taking too long to connect you to this video call. Try again in a few minutes." in ele:
                    driver.refresh()
                    join_button = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                               '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')))
                    time.sleep(5)

            for i in range(3):
                bdy_source = driver.page_source
                if r'data-tooltip="Turn off microphone (ctrl + d)" data-is-muted="false"' in bdy_source:
                    driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL, 'd')
                if r'data-tooltip="Turn off camera (ctrl + e)" data-is-muted="false"' in bdy_source:
                    driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL, 'e')

            c = False
        except():
            driver.refresh()
        join_button.click()
    time.sleep(900)
    print("abc")
    element_body = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body')))
    ele = element_body.get_attribute("outerHTML")
    if "You'll join the call when someone lets you in" in ele or "You can't join this call" in ele:
        print('no class')
        driver.__exit__()
        return 0
    leave_class()
    driver.__exit__()






