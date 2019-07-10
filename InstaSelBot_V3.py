from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from db import connect_to_db

NAME = 'aleksmolik'
PASSWORD = '1q2w3e4r5t'
MESSAGE = 'Салам алейкум, брат!'

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
    "userAgent": """Mozilla/5.0 
    (Linux;
     Android 4.2.1;
     en-us;
     Nexus 5 Build/JOP40D)
     AppleWebKit/535.19
    (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"""}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)



# авторизация
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")
sleep(3)
find_and_write_by_name('username', NAME)
find_and_write_by_name('password', PASSWORD)
# кнопка авторизации + проверка на ублюдка
'''
path_list = [
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button'
]
'''

try:
    get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/button')
except:
    print('Тест на ублюдка не пройден')

    """
        try:
        get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[6]/button')
    except:
        get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button')
    """

get_in.click()
sleep(3)
print('Авторизация выполнена')


# послать уведомление
find_and_click('/html/body/div[3]/div/div/div[3]/button[2]')
print('Уведомление смело пошло нахер')
# открыть уведомления
driver.get('https://www.instagram.com/accounts/activity/')
sleep(1)
print('Уведомления открыты')

def main():
    print('Щас буду искать пользователей')
    #найти пользователя в уведомелниях

    #find_and_click('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a')
    find_and_click('//*[@id="react-root"]/section/main/div/div/div/div/div/div[2]/div/a')
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
        print('Сообщение отправлено пользователю: {} \n Текст сообщения: {}'.format(user.text,MESSAGE))
        '''
    else:
        print("Пользователя нет в базе")
        print(user.text)
        find_and_click('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/span/span[1]/button', delay=3)
        find_and_click('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[1]/button', delay=3)
        find_and_write_by_path('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/textarea', MESSAGE)
        find_and_click('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div[2]/button')
        print('Ваще не ебу, что я здесь делаю')


if __name__ == "__main__":
    while True:
        try: 
            main()
        except:
            driver.get('https://www.instagram.com/accounts/activity/')
            print('Перерыв')
            sleep(15)