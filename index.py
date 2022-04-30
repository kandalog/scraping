from optparse import Option
from selenium import webdriver # ブラウザを外部のソフトから操作可能にするもの
from time import sleep
from selenium.webdriver.chrome.options import Options # option設定を可能にする
from selenium.webdriver.common.by import By # find_elementが使える

options = Options()
options.add_argument('--headless') # ヘッドレスモードをオプションに設定 (CLIで実行する)

browser = webdriver.Chrome(options=options) # ブラウザ起動 # options=optionsを引数に渡してCLIで実行する
browser.get('https://scraping-for-beginner.herokuapp.com/login_page') # urlにアクセス
# sleep(1)

# ログインする     （1:どの場所に 2:どんな処理を行いたいか）
elem_username = browser.find_element(By.ID, 'username') # 要素を取得
elem_username.send_keys('imanishi') # 文字を入力

elem_password = browser.find_element(By.ID, 'password')
elem_password.send_keys('kohei')

login_button = browser.find_element(By.ID, 'login-btn')
# sleep(1)
login_button.click() # クリックする

elem = browser.find_element(By.ID, 'name')
name = elem.text

elem = browser.find_element(By.ID, 'company')
company = elem.text

elem = browser.find_element(By.ID, 'birthday')
birthday = elem.text

elem = browser.find_element(By.ID, 'come_from')
birthplace = elem.text

elem = browser.find_element(By.ID, 'hobby')
hobby = elem.text
hobby = hobby.replace('\n', ',')
# print(hobby)

# 繰り返し処理で全件取得
elems_th = browser.find_elements(By.TAG_NAME, 'th')
keys = []
for item in elems_th:
  key = item.text
  keys.append(key)
print(keys)

elems_td = browser.find_elements(By.TAG_NAME, 'td')
values = []
for item in elems_td:
  value = item.text
  values.append(value)
print(values)

import pandas as pd

df = pd.DataFrame()
df['項目'] = keys
df['値'] = values



# sleep(2)
browser.quit() # Chromeを閉じる