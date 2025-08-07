import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

print(soup.select('ul.popular__order li'))
# [<li class="list">
# <span class="list__index blue">1</span> 아이유 (IU)
#           </li>, <li class="list">
# <span class="list__index blue">2</span> 방탄소년단
#           </li>, <li class="list">
# <span class="list__index blue">3</span> Red Velvet (레드벨벳)
#           </li>, <li class="list">
# <span class="list__index">4</span> IKON
#           </li>, <li class="list">
# <span class="list__index">5</span> 멜로망스
#           </li>, <li class="list">
# <span class="list__index">6</span> 다비치
#           </li>, <li class="list">
# <span class="list__index">7</span> 윤딴딴
#           </li>, <li class="list">
# <span class="list__index">8</span> 수지 (SUZY)
#           </li>, <li class="list">
# <span class="list__index">9</span> 김동률
#           </li>, <li class="list">
# <span class="list__index">10</span> 폴킴
#           </li>]

# ! get_text()

for tag in soup.select('ul.popular__order li'):
    print(tag.get_text())
# 1 아이유 (IU)


# 2 방탄소년단


# 3 Red Velvet (레드벨벳)


# 4 IKON


# 5 멜로망스


# 6 다비치


# 7 윤딴딴


# 8 수지 (SUZY)


# 9 김동률


# 10 폴킴

for tag in soup.select('ul.popular__order li'):
    print(tag.get_text().strip())
# 1 아이유 (IU)
# 2 방탄소년단
# 3 Red Velvet (레드벨벳)
# 4 IKON
# 5 멜로망스
# 6 다비치
# 7 윤딴딴
# 8 수지 (SUZY)
# 9 김동률
# 10 폴킴

popular_artists = []
for tag in soup.select('ul.popular__order li'):
    popular_artists.append(tag.get_text().strip())

print(popular_artists)
# ['1 아이유 (IU)', '2 방탄소년단', '3 Red Velvet (레드벨벳)', '4 IKON', '5 멜로망스', '6 다비치', '7 윤딴딴', '8 수지 (SUZY)', '9 김동률', '10 폴킴']


# ! strings stripped_strings

for tag in soup.select('ul.popular__order li'):
    print(list(tag.strings))
# ['\n', '1', ' 아이유 (IU)\n          ']
# ['\n', '2', ' 방탄소년단\n          ']
# ['\n', '3', ' Red Velvet (레드벨벳)\n          ']
# ['\n', '4', ' IKON\n          ']
# ['\n', '5', ' 멜로망스\n          ']
# ['\n', '6', ' 다비치\n          ']
# ['\n', '7', ' 윤딴딴\n          ']
# ['\n', '8', ' 수지 (SUZY)\n          ']
# ['\n', '9', ' 김동률\n          ']
# ['\n', '10', ' 폴킴\n          ']

for tag in soup.select('ul.popular__order li'):
    print(list(tag.stripped_strings))
# ['1', '아이유 (IU)']
# ['2', '방탄소년단']
# ['3', 'Red Velvet (레드벨벳)']
# ['4', 'IKON']
# ['5', '멜로망스']
# ['6', '다비치']
# ['7', '윤딴딴']
# ['8', '수지 (SUZY)']
# ['9', '김동률']
# ['10', '폴킴']

for tag in soup.select('ul.popular__order li'):
    print(list(tag.stripped_strings)[1])
# 아이유 (IU)
# 방탄소년단
# Red Velvet (레드벨벳)
# IKON
# 멜로망스
# 다비치
# 윤딴딴
# 수지 (SUZY)
# 김동률
# 폴킴

popular_artists = []
for tag in soup.select('ul.popular__order li'):
    popular_artists.append(list(tag.stripped_strings)[1])

print(popular_artists)
# ['아이유 (IU)', '방탄소년단', 'Red Velvet (레드벨벳)', 'IKON', '멜로망스', '다비치', '윤딴딴', '수지 (SUZY)', '김동률', '폴킴']