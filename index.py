from optparse import Option
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options # option設定を可能にする

options = Options()
options.add_argument('--headless') # ヘッドレスモードをオプションに設定 (CLIで実行する)

browser = webdriver.Chrome() # ブラウザ起動 # options=optionsを引数に渡してCLIで実行する
browser.get('https://scraping-for-beginner.herokuapp.com/login_page') # urlにアクセス
sleep(3)

# ログインする     （1:どの場所に 2:どんな処理を行いたいか）
elem_username = browser.find_element_by_id('username') # 要素を取得
elem_username.send_keys('imanishi') # 文字を入力

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

login_button = browser.find_element_by_id('login-btn')
sleep(1)
login_button.click() # クリックする










sleep(5)
browser.quit() # Chromeを閉じる