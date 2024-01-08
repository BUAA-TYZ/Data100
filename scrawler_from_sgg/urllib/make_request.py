import urllib.request

url = "https://www.baidu.com"

# UA 反爬
# response = urllib.request.urlopen(url)

# content = response.read().decode('utf-8')

headers = {
  # eage
  # "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.203"
  # google chrome
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)