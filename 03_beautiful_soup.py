import requests
# pip3 install beautifulsoup4 설치 명령어
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')
print(soup.select('title'))
# [<title>티비랭킹닷컴</title>]
print(soup.select('table'))
# [<table cellpadding="7" style="margin-left: auto;margin-right: auto;">
# <tr class="top-table row" height="64">
# <th class="rank">순위</th>
# <th class="channel">채널</th>
# <th class="program">프로그램</th>
# <th class="percent">시청률</th>
# </tr>
# <tr class="row">
# <td class="rank">1</td>
# <td class="channel">KBS2</td>
# <td class="program">주말연속극(수상한삼형제)</td>
# <td class="percent">33.4</td>
# </tr>
# <tr class="row">
# <td class="rank">2</td>
# <td class="channel">KBS1</td>
# <td class="program">일일연속극(다함께차차차)</td>
# <td class="percent">33.1</td>
# </tr>
# <tr class="row">
# <td class="rank">3</td>
# <td class="channel">KBS2</td>
# <td class="program">해피선데이</td>
# <td class="percent">27.1</td>
# </tr>
# <tr class="row">
# <td class="rank">4</td>
# <td class="channel">MBC</td>
# <td class="program">MBC연기대상2부</td>
# <td class="percent">24.4</td>
# </tr>
# <tr class="row">
# <td class="rank">5</td>
# <td class="channel">SBS</td>
# <td class="program">주말극장(천만번사랑해)</td>
# <td class="percent">24.2</td>
# </tr>
# <tr class="row">
# <td class="rank">6</td>
# <td class="channel">MBC</td>
# <td class="program">MBC방송연예대상2부</td>
# <td class="percent">24.0</td>
# </tr>
# <tr class="row">
# <td class="rank">7</td>
# <td class="channel">MBC</td>
# <td class="program">MBC방송연예대상1부</td>
# <td class="percent">22.4</td>
# </tr>
# <tr class="row">
# <td class="rank">8</td>
# <td class="channel">SBS</td>
# <td class="program">SBS연예대상2부</td>
# <td class="percent">21.1</td>
# </tr>
# <tr class="row">
# <td class="rank">9</td>
# <td class="channel">MBC</td>
# <td class="program">주말기획드라마(보석비빔밥)</td>
# <td class="percent">20.9</td>
# </tr>
# <tr class="row">
# <td class="rank">10</td>
# <td class="channel">MBC</td>
# <td class="program">일일시트콤(지붕뚫고하이킥)</td>
# <td class="percent">19.9</td>
# </tr>
# </table>]