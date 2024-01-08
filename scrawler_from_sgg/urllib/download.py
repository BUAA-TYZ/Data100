import urllib.request

# url_page = "http://www.baidu.com"

# urllib.request.urlretrieve(url_page, "./scrawler_from_sgg/urllib/baidu_index.html")

url_image = "data:image/jpeg;base64,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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//9k="

urllib.request.urlretrieve(url_image, "./scrawler_from_sgg/urllib/python.png")