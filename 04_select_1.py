import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

# ! select 메서드

soup = BeautifulSoup(rating_page, 'html.parser')
print(soup.select('td.program'))
# [<td class="program">주말연속극(수상한삼형제)</td>, <td class="program">일일연속극(다함께차차차)</td>, <td class="program">해피선데이</td>, <td class="program">MBC연기대상2부</td>, <td class="program">주말극장(천만번사랑해)</td>, <td class="program">MBC방송연예대상2부</td>, <td class="program">MBC방송연예대상1부</td>, <td class="program">SBS연예대상2부</td>, <td class="program">주말기획드라마(보석비빔밥)</td>, <td class="program">일일시트콤(지붕뚫고하이킥)</td>]

program_title_tags = soup.select('td.program')

for tag in program_title_tags:
    print(tag.get_text())
# 주말연속극(수상한삼형제)
# 일일연속극(다함께차차차)
# 해피선데이
# MBC연기대상2부
# 주말극장(천만번사랑해)
# MBC방송연예대상2부
# MBC방송연예대상1부
# SBS연예대상2부
# 주말기획드라마(보석비빔밥)
# 일일시트콤(지붕뚫고하이킥)

program_titles = []

for tag in program_title_tags:
    program_titles.append(tag.get_text())

print(program_titles)
# ['주말연속극(수상한삼형제)', '일일연속극(다함께차차차)', '해피선데이', 'MBC연기대상2부', '주말극장(천만번사랑해)', 'MBC방송연예대상2부', 'MBC방송연예대상1부', 'SBS연예대상2부', '주말기획드라마(보석비빔밥)', '일일시트콤(지붕뚫고하이킥)']

# ! select_one 메서드
print(soup.select_one('td.program'))
# <td class="program">주말연속극(수상한삼형제)</td>