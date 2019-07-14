import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
import pickle

NAME = 'aleksmolik'
PASSWORD = '1q2w3e4r5t'
MESSAGE = 'Салам алейкум, брат!'

def connect_to_db(user):
    con = sqlite3.connect('base.db')
    cur = con.cursor()

    try:
        cur.execute('SELECT * FROM Insta WHERE name ="{}"'.format(user)).fetchone()[0]
        print('Найдено')
        result = True
    except:
        data = [user, datetime.strftime(datetime.now(), "%H:%M:%S")]
        cur.execute('INSERT INTO Insta VALUES(?, ?)', data)
        print('Не найдено')
        result = False

    con.commit()
    cur.close()
    con.close()
    return result

def find_and_click(path, delay=1):
    driver.find_element_by_xpath(path).click()
    sleep(delay)

def find_and_write_by_name(name, message, delay=0):
    driver.find_element_by_name(name).send_keys(message)
    sleep(delay)

def find_and_write_by_path(path, message, delay=0):
    driver.find_element_by_xpath(path).send_keys(message)
    sleep(delay)


# настройки веб-дравйера
mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": """Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1	"""}

option = Options()
option.add_experimental_option("mobileEmulation", mobile_emulation)
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(chrome_options = option)

driver.get('https://www.google.ru/')
#sleep(5)

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


driver.get("https://www.instagram.com")
#driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")
# авторизация
'''

sleep(3)
find_and_write_by_name('username', NAME)
find_and_write_by_name('password', PASSWORD)




# кнопка авторизации + проверка на ублюдка

path_list = [
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button'
]


try:
    get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/button')
except:
    print('Тест на ублюдка не пройден')
    try:
        print('Второй тест на ублюдка')
        get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[6]/button')
    except:
        print('Третий тест на ублюдка')
        get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button')


get_in.click()
sleep(5)
print('Авторизация выполнена')

sleep(30)
#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

# послать уведомление

find_and_click('/html/body/div[3]/div/div/div[3]/button[2]')
print('Уведомление смело пошло нахер')
'''
# открыть уведомления
sleep(5)
find_and_click('/html/body/div[3]/div/div/div[3]/button[2]', delay=5)
driver.get('https://www.instagram.com/accounts/activity/')
sleep(1)
print('Уведомления открыты')




def main():
    print('Щас буду искать пользователей')
    #найти пользователя в уведомелниях

    try: find_and_click('//*[@id="react-root"]/section/main/div/div/div/div/div/div[2]/div/a')
    except: find_and_click('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a')
    print('Нашёл!')
    user = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1')
    if connect_to_db(user.text):
        print('Пользователь есть в базе')
        sleep(3)


        '''
        #кнопка для отпраки сообщения в профиле
        find_and_click('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[1]/button', delay=3)
        #ввод сообщения
        find_and_write_by_path('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/textarea', MESSAGE)
        #кнопка "отправить сообщение" в директе
        find_and_click('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div[2]/button')
        
        '''
    else:
        print("Пользователя нет в базе")
        find_and_click('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/span/span[1]/button', delay=5)
        find_and_click('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[1]/button', delay=5)
        find_and_write_by_path('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/textarea', MESSAGE)
        find_and_click('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div[2]/button')
        print('Сообщение отправлено пользователю: {} \n Текст сообщения: {}'.format(user.text, MESSAGE))
        sleep(15)

if __name__ == "__main__":
    while True:
        try: 
            main()
        except:
            driver.get('https://www.instagram.com/accounts/activity/')
            print('Перерыв')
            sleep(25)