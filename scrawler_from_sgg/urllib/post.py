import urllib.request
import urllib.parse
import json

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

# If we don't use cookie, then we will get the unknown error.
headers = {
# 'Accept': '*/*',

# Accept-Encoding must be commented because we use utf-8.
# 'Accept-Encoding': 'gzip, deflate, br',

# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Acs-Token': '1704539257108_1704558513498_u9Ggt5Z6QuGNl80jZNndTVRVsqCZJFuFt7Fo+/X8kN0SYtJV5vwbmIfqDTcSqUWJLLXagRalPQuFvrn3lxqxkdQghHhjHJPLybxmZvfokfvqUCunKXXlxWrk621jpem+DxUJUAgG24hlsAg2hugFNt58Fpc2q/smavqMgqype2R6B6tNecHsLaAbZuHLyeN0q1AtcwOpYSvF9vwA5jS3+2tThC3mTv4Tuu1Xhe7DmV8DN98102GAgBzdy9qfKvnoVPAxrf/VUwnAu1Y4JJ0SkDuHxyfvFYbXbnteG54iJPy2uhDmZ2erDiF9+AHpoGAoH28+7QvzZJ1PvC6Eqbh5zD/FUhDbpsZ2qhQM3IIlMezCHZSOw4RxnbOlbfoUl5scKdVGqTA0UPSGCWO0EF2/Lhaj+qSEe/8vNCSFvEjHLF8fXu+p7Kh0ilHSHiKDRPUk',
# 'Connection': 'keep-alive',
# 'Content-Length': '135',
# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'BAIDUID_BFESS=1FCF10722F2C7C1DD36C40DFE28DFC53:FG=1; BIDUPSID=1FCF10722F2C7C1DD36C40DFE28DFC53; PSTM=1683714315; ZFY=svFgfEAd7SusFPiRrKC0SqTbSKA:AAVB9k9QHdf5oOME:C; H_PS_PSSID=39998_40008_40053; BA_HECTOR=81012k210h2g802k8ga52g20uluu3k1ipil141t; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=3; delPer=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1704552344; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_MjkzYTBmODAzZTVhZjdmM2ZhMDQzOThiNDZmMzBmNjkyMDAwN2VkYmRkYWVmNTcyZDY4YzBmNTBjZDFiOGRjNDg2MzdkMDM4YmY0MzY2MWZhZDdhODQ0Mzc5ZDNkNDdiOGVhOGVhN2E3ZmNkMGFkZTZjZDM1ODJlZDRkMmE3NzljYTkxZmYyM2VmNjZlMTMxNDFjOTZjZjFhNGYwODJjNQ==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1704558513',
# 'Host': 'fanyi.baidu.com',
# 'Origin': 'https://fanyi.baidu.com',
# 'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
# 'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
# 'Sec-Ch-Ua-Mobile': '?0',
# 'Sec-Ch-Ua-Platform': '"Windows"',
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
# 'X-Requested-With': 'XMLHttpRequest',
}

# We use the powerful regular expressions to add quote for each key-value pair.
# :15, 22s/([^ ]*): (.*)/"\1": "\2",/g
data = {
  "from": "en",
  "to": "zh",
  "query": "travel",
  "simple_means_flag": "3",
  "sign": "823696.553633",
  "token": "8547711ea03cdc46304b1c134c52a079",
  "domain": "common",
  "ts": "1704558513469",
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

readable_content = json.loads(content)
print(readable_content)
