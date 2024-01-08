import urllib.request

url = 'https://www.google.com'

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
request = urllib.request.Request(url, None, headers)

handler = urllib.request.ProxyHandler({'https': '127.0.0.1:7890'})
opener = urllib.request.build_opener(handler)

response = opener.open(request)
content = response.read().decode('utf-8')
print(content)