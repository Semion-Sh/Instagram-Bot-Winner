from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import config
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path='Instagram-Bot/chromedriver')
time.sleep(1)
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome("chromedriver", options=options)
browser.get('https://www.instagram.com/')


username = browser.find_element(By.NAME, "username")
username.send_keys(config.username)
time.sleep(3)

password = browser.find_element(By.NAME, "password")
password.send_keys(config.password)
time.sleep(2)

solid = 1

def cookie():
    cookie = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
    cookie.click()
    return;
cookie();
time.sleep(2)


def clickentry():
  login = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
  login.click()
  return;
clickentry();
time.sleep(10)


def notnow():
    notnow = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    notnow.click()
    return;
notnow();
time.sleep(4)


browser.get(f'https://www.instagram.com/{link}/')
time.sleep(5)


def get_post():
    post = browser.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]')
    post.click()
    return;
get_post();
time.sleep(4)


def get_text():
    post = browser.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]')
    # post.click()
    photo = browser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div/div/div[1]/img').get_attribute("src")
    post_text = post.text[116:]

    print(post_text)
    print(photo)
    return;


get_text();
time.sleep(4)
time.sleep(4)
for i in following:
    comment = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button')
    time.sleep(1)
    comment.click()
    comment = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
    driver.execute_script("arguments[0].innerHTML = '{}'".format(i), comment)
    comment.send_keys('@')
    time.sleep(2)

    post = driver.find_element(By.XPATH,
                           '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button')
    post.click()
    time.sleep(1)
    driver.refresh()
time.sleep(5)


while solid == 1:
    for i in following:
        driver.refresh()
        commentt = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button')
        time.sleep(1)
        commentt.click()
        commentt = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        commentt.click()
        time.sleep(2)
        driver.execute_script("arguments[0].innerHTML = '{}'".format(i), commentt)
        commentt.send_keys('@')
        posty = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button')
        posty.click()
