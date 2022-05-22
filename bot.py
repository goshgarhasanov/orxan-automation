import random

from selenium.webdriver.common.by import By
import db
from selenium import webdriver
import tkinter as tk
import time
from anycaptcha import AnycaptchaClient, ImageToTextTask

myFakeData = db.getDB()


def imagetotext(apikey="73308e7a069a4f4aaa5c7eeb10ec6172", img: str = ''):
    client = AnycaptchaClient(apikey)
    task = ImageToTextTask(img)
    job = client.createTask(task, typecaptcha="text")
    job.join()
    result = job.get_solution_response()
    if result.find("ERROR") != -1:
        return ("error ", result)
    else:
        return result


if (myFakeData['webdriver'] == 1):
    driver = webdriver.Edge(executable_path='webdrivers/edge/msedgedriver.exe')
else:
    driver = webdriver.Chrome(executable_path='webdrivers/chrome/chromedriver.exe')

driver.get(myFakeData['siteUrl'])
driver.execute_script(f"""document.body.style.zoom='{myFakeData["browserResolution"]}%'""")
driver.fullscreen_window()


def fillForm(userInfo):
    fname = driver.find_element(By.CSS_SELECTOR, "[aria-label='First name *']")
    fname.send_keys(userInfo['fname'])
    sname = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Surname *']")
    sname.send_keys(userInfo['sname'])
    phone = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Contact Phone Number *']")
    phone.send_keys(userInfo['phone'])
    email = driver.find_element(By.CSS_SELECTOR, "input[aria-label='E-mail *']")
    email.send_keys(userInfo['email'])
    ctship = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Citizenship *']")
    ctship.send_keys(userInfo['ctship'])
    passportNumber = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Passport number *']")
    passportNumber.send_keys(userInfo['passportNumber'])
    captchaCode = driver.find_element(By.CSS_SELECTOR,"[aria-label='Copy the text from the picture *']")
    captchaCode.send_keys('')
    img = driver.find_element(By.XPATH,
                              '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/div[7]/div[1]/img')
    src = img.get_attribute('src')
    src = src[22:]
    captchaResult = imagetotext('73308e7a069a4f4aaa5c7eeb10ec6172', src)
    c1 = driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/div[8]/div/div/div[1]/div/div').click()
    c2 = driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/div[9]/div/div/div[1]/div/div').click()
    c3 = driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/div[10]/div/div/div[1]/div/div').click()
    captchaCode.send_keys(captchaResult)
    # time.sleep(2)
    submitBtn = driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/form/button')
    if (userInfo['submitBtn']):
        submitBtn.click()


def getSite(userInfo):
    time.sleep(1)
    collectBtn = driver.find_elements(By.CLASS_NAME, 'queue-button')
    collectBtn[userInfo['collectBtn']].click()
    time.sleep(1)
    cityBtn = driver.find_elements(By.CLASS_NAME, 'queue-button')
    if (userInfo['city'] == 's1'):
        cityBtn[2].click()
    else:
        cityBtn[3].click()
    if (userInfo['rightBtn']):
        time.sleep(2)
        calendarRightBtn = driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/button[2]').click()
    time.sleep(2)
    calendars = driver.find_elements(By.CLASS_NAME, 'v-btn')
    for calendar in calendars:
        calendarClass = calendar.get_attribute('class')
        if (calendarClass == 'v-btn v-btn--flat v-btn--floating theme--light'):
            calendar.click()
    time.sleep(2)
    stimes = driver.find_elements(By.CLASS_NAME, 'xs6')
    for stms in stimes:
        stmBtn = stimes[random.randint(0, 8)].find_element(By.TAG_NAME, 'button')
        if not (stmBtn.get_attribute(
                'class') == 'v-btn v-btn--block v-btn--large v-btn--outline v-btn--depressed theme--light info--text'):
            continue
        else:
            stmBtn.click()
            break
    time.sleep(1.2)
    fillForm(userInfo)


def StartBot():
    getSite(myFakeData)


def FormStart():
    fillForm(myFakeData)


def RefreshPage():
    driver.refresh()
    driver.fullscreen_window()


root = tk.Tk()
root.title("Bot Başlatma Programı")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='img/icon.png'))
root.geometry('200x150')
root.configure(bg='brown')
startBtn = tk.Button(root, text="Formu Doldur!", command=FormStart,background='yellow',font=("Helvetica 15 bold"),cursor='hand2')
developer=tk.Label(text="Development By hasnaov@gmail.com").pack()
# refreshBtn = tk.Button(root, text="REFRESH", command=RefreshPage,background='yellow',font=("Helvetica 15 bold"),cursor='hand2')
# startBotBtn = tk.Button(root, text="Botu Başlat!", command=StartBot,background='yellow',font=("Helvetica 15 bold"),cursor='hand2')
# startBtn.config['']

# root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', '1')

# if (myFakeData['autoStarted'] == 0):
#     startBtn.pack(pady=5)
#
# elif (myFakeData['autoStarted'] == 1):
#     startBotBtn.pack(pady=5)
#     refreshBtn.pack(pady=5)
# else:
#     root.destroy()
#     StartBot()
startBtn.pack(pady=5)
root.mainloop()
