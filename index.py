from selenium import webdriver
from time import sleep

browser = webdriver.Chrome() # ブラウザ起動

browser.get('https://scraping-for-beginner.herokuapp.com/login_page') # urlにアクセス
sleep(3)

# 操作の大前提（1:どの場所に 2:どんな処理を行いたいか）

# ログインする
elem_username = browser.find_element_by_id('username') # 要素を取得
elem_username.send_keys('imanishi') # 文字を入力

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

login_button = browser.find_element_by_id('login-btn')
sleep(1)
login_button.click() # クリックする




sleep(5)
browser.quit() # Chromeを閉じる