import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
# ? pip3 install openpyxl -> 설치 명령어

# ? 워크북 만들기
wb = Workbook(write_only=True)
# ? 워크시트 만들기
ws = wb.create_sheet('TV Ratings')
# ? 행 추가하기
ws.append(['순위', '채널', '프로그램', '시청률'])

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')
for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(), # 순위
        td_tags[1].get_text(), # 채널
        td_tags[2].get_text(), # 프로그램
        td_tags[3].get_text(), # 시청률
    ]
    ws.append(row)

# ? 저장하기
wb.save('시청률_2010년1월1주차.xlsx')