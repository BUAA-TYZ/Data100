import os
import urllib.parse
import urllib.request

def create_request(page):
  base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"
  headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
  }
  data = {
     "start": 20 * (page - 1),
     "limit": 20,
  }
  url = base_url + urllib.parse.urlencode(data)
  return urllib.request.Request(url, headers=headers)

def get_content(request):
  response = urllib.request.urlopen(request)
  content = response.read().decode('utf-8')
  return content

if __name__ == "__main__":
  print("Now you are getting the page from www.movie.douban.com")
  print("This is a top list where you can query the movies. Each page has 20 movies.")
  start_page = int(input("Please input the start page: "))
  end_page = int(input("Please input the end page: "))

  if start_page > end_page:
      raise ArithmeticError("Start page must be smaller than end page.")
    
  if not os.path.isdir('douban_data'):
    os.mkdir('douban_data')

  for i in range(start_page, end_page + 1):
    request = create_request(i)
    content = get_content(request)
    with open('./douban_data/douban_'+str(i)+'.json', 'w', encoding='utf-8') as fp:
      fp.write(content)
