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


global count
count = 1




moodle_creds = {'email': 'basilshah.cm@gmail.com', 'passwd' : 'Basil@1511'}
subjects = {'monday' : ['dc','oops','vlsi','rtos','dip'],
            'tuesday' : ['awp','awp','dc','rtos','CElab'],
            'wednesday' :['vlsi','es','awp','dc','oops'],
            'thursday' :['rtos','es','vlsi','dip','dc'],
            'friday' :['oops','dip','es','MClab','']
            }



def find_day():
    date = datetime.date.today()
    date = date.weekday()
    day = calendar.day_name[date]
    return day.lower()


#to find the current class
def find_class():
    global tiee
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
                tiee = ftimes[i].split('-')[1]
            elif ti > ftimes[4].split('-')[1]:
                exit()

    else:
        for i in range(5):
            if ti >= times[i].split('-')[0] and ti < times[i].split('-')[1]:
                cls = classes[i]
                tiee = times[i].split('-')[1]
            elif ti > ftimes[4].split('-')[1]:
                exit()

    return cls, tiee

# attendence marking...................................................................

def submit():
    time.sleep(3)
    u = True
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="region-main"]')))
            driver.find_element_by_xpath('''//span[.='Attendance']''').click()
            u = False
        except:
            driver.refresh()
    time.sleep(3)
    u = True
    cun = 1
    tii = find_class()[1]
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="region-main"]')))
            driver.find_element_by_link_text("Submit attendance").click()
            u = False

        except:
            time.sleep(240)
            cun+=1
            print(cun)

            t = tii.split(':')
            timmm = t[0] + ':' + str(int(t[1]) + 20)
            timee = str(datetime.datetime.now().time()).split(':')
            ti = timee[0] + ':' + timee[1]
            print(ti,timmm)
            if ti > timmm:
                print('no attendence ')
                driver.__exit__()
                return 0
            driver.refresh()

    time.sleep(3)
    u = True
    while u:
        try:
            time.sleep(10)
            body = wait.until(EC.visibility_of_element_located((By.ID, 'id_submitbutton')))
            a = driver.find_elements_by_xpath("//input[@type='radio']")
            a[0].click()

            time.sleep(3)
            u = False
        except:
            driver.refresh()

    driver.find_element_by_id('id_submitbutton').click()
    print("attendence marked")
    driver.__exit__()


def CElab():
    u = True
    time.sleep(3)
    while u:
        try:
            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))
            # find element by the text name
            driver.find_element_by_xpath('''//span[.=' S6 ECB COMMUNICATION LAB ']''').click()
            u = False
        except:
            driver.refresh()
    submit()

def MClab():
    u = True
    time.sleep(3)
    while u:
        try:
            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))
            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            MICROCONTROLLER LAB
        ']''').click()
            u = False
        except:
            driver.refresh()
    submit()


def awp():
    u = True
    time.sleep(3)
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))

            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            EC306 Antenna and Wave Propagation
        ']''').click()
            u = False
        except:
            driver.refresh()

    submit()




def vlsi():
    u = True
    while u:
        try:
            body = wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))

            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            EC 304 VLSI
        ']''').click()
            u = False
        except:
            driver.refresh()
    submit()

def dc():
    u = True
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))

            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            ECB 302 DIGITAL COMMUNICATION 
        ']''').click()
            u = False
        except:
            driver.refresh()
    submit()

def dip():
    u = True
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))

            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            EC370 DIGITAL IMAGE PROCESSING
        ']''').click()
            u = False
        except:
            driver.refresh()

    submit()


def oops():
    u = True
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))

            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            EC312-Object Oriented Programming
        ']''').click()
            u = False
        except:
            driver.refresh()
    submit()

def es():
    u = True
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))

            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            EC 308 Embedded Systems
        ']''').click()
            u = False
        except:
            driver.refresh()
    submit()

def comp():
    u = True
    while u:
        try:

            body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card.dashboard-card')))

            # find element by the text name
            driver.find_element_by_xpath('''//span[.='
            Comprehensive Exam
        ']''').click()
            u = False
        except:
            driver.refresh()
    submit()


def attendence(email,passwd,subject):
    global driver ,wait
    driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe', options=opt)
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 20)
    u = True
    while u:
        try:

            driver.get('http://moodle.mec.ac.in/my/')
            time.sleep(3)
            usrname = wait.until(EC.visibility_of_element_located((By.ID, 'username')))
            driver.find_element_by_id('username').send_keys(email)
            driver.find_element_by_id('password').send_keys(passwd)
            driver.find_element_by_id('loginbtn').click()
            u = False
        except:
            driver.refresh()
    time.sleep(3)

    if subject == 'awp':
        awp()

    if subject == 'vlsi':
        vlsi()

    if subject == 'dc':
        dc()

    if subject == 'dip':
        dip()

    if subject == 'oops':
        oops()

    if subject == 'es':
        es()
    if subject == 'comp':
        comp()
    if subject == 'MClab':
        MClab()

    if subject == 'CElab':
        CElab()


def mark_attend():
    clss = find_class()[0]
    tim = find_class()[1]
    print(clss)
    print(tim)
    attendence(moodle_creds['email'],moodle_creds['passwd'],clss)


q = datetime.datetime.now()
z = q.replace(hour=8,minute=35)

if q < z :
    print('pause')
    pause.until(z)

while True:
    tim = find_class()[1]
    q = datetime.datetime.now()
    timee = str(q.time()).split(':')
    ti = timee[0] + ':' + timee[1]
    a = datetime.datetime.strptime(tim,'%H:%M')
    b= datetime.datetime(q.year,q.month,q.day,a.hour,a.minute)
    if ti < tim :
        mark_attend()
        try:
            driver.__exit__()
        except:
            pass
        print("pause untile : ",b)
        pause.until(b)

