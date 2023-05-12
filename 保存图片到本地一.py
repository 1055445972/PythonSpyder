import requests
url = 'https://img08.tooopen.com/20230408/tooopen_tp_16380838856060.jpg'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
}
res = requests.get(url, headers=headers)

with open('test.jpg', 'wb') as f:
    f.write(res.content)
    print(res.content)