import urllib.request

url = "http://www.baidu.com"

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

# print(content)

# for i in response.getheaders():
#   print(i)

print(response.getcode())

print(response.geturl())