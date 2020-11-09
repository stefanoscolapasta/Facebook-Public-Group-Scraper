from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = 'PutYourAccountEmailHere'
password = 'PutYourAccountPasswordHere'
url = 'PutTheURLhere'
browser = webdriver.Chrome(executable_path='PutTheChromeDriverPathHere')
browser.get(url)
browser.find_element_by_id('email').send_keys(email)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input').click()
pyautogui.typewrite(password)
browser.find_element_by_id('loginbutton').click()
time.sleep(5)
pyautogui.click(700, 700)
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]').click()
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]').send_keys('GroupNameHere' + Keys.RETURN)
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[1]/a').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/a').click()

Lista_iscritti = []
SCROLL_PAUSE_TIME = 3
last_height = browser.execute_script("return document.body.scrollHeight")

PERIOD_OF_TIME = 25200
start = time.time()
while True:
    if time.time() > start + PERIOD_OF_TIME:
        break
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

elems = browser.find_elements_by_class_name("_60ri>a")
for elem in elems:
    Lista_iscritti.append(elem.get_attribute("href"))
with open('List.txt', 'w') as f:
    for item in Lista_iscritti:
        f.write("%s\n" % item)
