import os
import urllib.parse
import urllib.request

def create_request(page):
  url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
  data = {
    'cname': '北京',
    'pid': '',
    'pageIndex': str(page),
    'pageSize': '10',
  }

  headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
  }
  return urllib.request.Request(url=url, data=urllib.parse.urlencode(data).encode('utf-8'), headers=headers)

def get_content(request):
  response = urllib.request.urlopen(request)
  content = response.read().decode('utf-8')
  return content

if __name__ == '__main__':
  print('Here is a list of kfc locations in Beijing.')
  print('Each page of the list has 10 locations.')
  start_page = int(input('Start page: '))
  end_page = int(input('End page: '))
  if start_page > end_page:
    raise ArithmeticError('Start page must be smaller than end page.')

  if not os.path.isdir('./kfc_data'):
    os.mkdir('./kfc_data')

  for i in range(start_page, end_page + 1):
    request = create_request(i)
    content = get_content(request)
    with open('./kfc_data/kfc_loc_' + str(i) + '.json', 'w', encoding='utf-8') as fp:
      fp.write(content)