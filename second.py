import requests 
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)

# htmlを取得して、みやすく整形している (整形にBeautifulSoup)を使用する
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify)

print(soup.find_all('p')) # soupで読み込んだhtmlからpタグを全て取得

# find_all -> 全て取得 find_all('p')[2] どれを取るか指定可能
# find -> 最初の一件を取得
# soup.p -> pを全て取得

# print(soup.p.text)

# pタグ && classがsubscribersのものを取得
soup.find_all('p', attrs={'class': 'subscribers'})
print(soup.find_all('p', attrs={'class': 'subscribers'})[0])