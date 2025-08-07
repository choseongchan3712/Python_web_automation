import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

print(soup.select('td')[:4]) # ? [:4] -> 리스트 슬라이싱
# [<td class="rank">1</td>, <td class="channel">KBS2</td>, <td class="program">주말연속극(수상한삼형제)</td>, <td class="percent">33.4</td>]

td_tags = soup.select('td')[:4]
for tag in td_tags:
    print(tag.get_text())
# 1
# KBS2
# 주말연속극(수상한삼형제)
# 33.4

tr_tag = soup.select('tr')[1]
td_tags = tr_tag.select('td')
for tag in td_tags:
    print(tag.get_text())
# 1
# KBS2
# 주말연속극(수상한삼형제)
# 33.4