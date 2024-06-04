import requests
from bs4 import BeautifulSoup

def get_soundcloud_likes():
    url = "https://soundcloud.com/val_hash/likes"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    likes = []
    # 좋아요 목록에서 곡 제목을 선택
    titles = soup.select('a.soundTitle__title span')

    for title in titles:
        likes.append(title.text.strip())

    return likes

username = "val_hash"
likes = get_soundcloud_likes()
for idx, title in enumerate(likes, start=1):
    print(f"{idx}. {title}")
