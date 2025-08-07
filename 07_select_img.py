import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

print(soup.select('img'))
# [<img alt="logo" class="logo-img" src="/images/music/logo.png"/>, <img class="icon" src="/images/music/search.png"/>, <img alt="user" class="profile" src="/images/music/user.png"/>, <img alt="up" class="und" src="/images/music/up.png"/>, <img alt="down" class="und" src="/images/music/down.png"/>, <img alt="up" class="und" src="/images/music/up.png"/>, <img alt="up" class="und" src="/images/music/up.png"/>, <img alt="down" class="und" src="/images/music/down.png"/>, <img alt="up" class="und" src="/images/music/up.png"/>, <img :src="item.imageUrl" alt="background" class="playlist__img"/>, <img :src="item.authorProfileImageUrl" alt="owner" class="owner"/>, <img alt="like" class="data__like-img" src="/images/music/like.png"/>, <img alt="music" class="data__music-img" src="/images/music/music.png"/>]

for data in soup.select('img'):
    print(data.attrs)
# {'class': ['logo-img'], 'src': '/images/music/logo.png', 'alt': 'logo'}
# {'class': ['icon'], 'src': '/images/music/search.png'}
# {'class': ['profile'], 'src': '/images/music/user.png', 'alt': 'user'}
# {'class': ['und'], 'src': '/images/music/up.png', 'alt': 'up'}
# {'class': ['und'], 'src': '/images/music/down.png', 'alt': 'down'}
# {'class': ['und'], 'src': '/images/music/up.png', 'alt': 'up'}
# {'class': ['und'], 'src': '/images/music/up.png', 'alt': 'up'}
# {'class': ['und'], 'src': '/images/music/down.png', 'alt': 'down'}
# {'class': ['und'], 'src': '/images/music/up.png', 'alt': 'up'}
# {'class': ['playlist__img'], ':src': 'item.imageUrl', 'alt': 'background'}
# {'class': ['owner'], ':src': 'item.authorProfileImageUrl', 'alt': 'owner'}
# {'class': ['data__like-img'], 'src': '/images/music/like.png', 'alt': 'like'}
# {'class': ['data__music-img'], 'src': '/images/music/music.png', 'alt': 'music'}

for data in soup.select('img'):
    if data.has_attr('src'):
        print(data['src'])
    elif data.has_attr(':src'):
        print(data[':src'])
    else:
        pass
# /images/music/logo.png
# /images/music/search.png
# /images/music/user.png
# /images/music/up.png
# /images/music/down.png
# /images/music/up.png
# /images/music/up.png
# /images/music/down.png
# /images/music/up.png
# item.imageUrl
# item.authorProfileImageUrl
# /images/music/like.png
# /images/music/music.png