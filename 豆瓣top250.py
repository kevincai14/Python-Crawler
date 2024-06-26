import requests

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
res = requests.get("https://movie.douban.com/top250", headers=headers)

with open("豆瓣top250.txt", "w", encoding="utf-8") as file:
    file.write(res.text)

print(res.text)
