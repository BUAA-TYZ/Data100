# When we want to collect data from the web page which needs us to log in, we should use cookie.
# 个人信息界面是utf-8，但 request 报编码错误。说明进入到了登录界面，而登录界面的编码不是utf-8

# Cookie 会携带登录信息
import urllib.request

# url = 'https://www.zhihu.com/people/hui-bu-lai-de-yong-yuan-hui-bu-lai'
url = 'https://github.com/'

# Even i use eage to login and use chrome's UA, i get the correct page.
headers = {
  "Cookie": "octo=GH1.1.1508794398.1687603975; user_session=OT9mhuU-flmMi0XWRzyPmd16FtLeoOJ4XhpMu8zOwdWoKDz9; __Host-user_session_same_site=OT9mhuU-flmMi0XWRzyPmd16FtLeoOJ4XhpMu8zOwdWoKDz9; logged_in=yes; dotcom_user=BUAA-TYZ; _device_id=8c0e726e0b01db3e6cbdd8d5e5d90318; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; has_recent_activity=1; _gh_sess=rcmmFFv3ehubOH0Xm411UV66%2FvdMzB81JSCmbxdt9VFUV1iWWORveGQKn%2B8Nb1fb6Er36hAR2qXM0C7KY900bgpzwQM2fy2%2BtRa2iBnv627SrzgEMkRplJLcc0SfZBCHPJ6p%2F2KiHISIVBkserB240lXG%2Bmq65%2FI8LI01YkTMQHJXt6zlnx8OkDfWAlXizQ0W5xtXo4TjqFu90t%2Fa4yiY%2FDu7V79wxsrCqmYoqsIhvz06EWbQz4uyVoqCdsGYRrnr9uaeEighb%2FG1pY%2FoAfT9qSSwu38%2BBO%2FYyH2UxiHr7X439SfD1AYXBQP3ZQd%2FFkKgzoDRgbtK3BG49vvsriTVKkGVXb531LYX4JXL3rJ4VqqLiK2th4a11FFDhLDDFC5uvyokIWi2KPB%2FaPvRmifWKJqT2B7vDBqN6ptE5NX39EL1DLwGnHHaeH%2F1lom%2FJzdzMjDpTtl5sSxaUjYLXkTi7KUqdf5Hc6AA8Lt1RSCv3yny6fxYG7oLr%2BUdhLsFGYEJoYWaPUkONxv8lpCkagOj9ALViclfzvWq284rjxZO2v4s%2Brvpq6pj0blQDK4chsT90KsI89a0q4Jnap9O7VyqxnDntgZJRD6Ex3JzEkqQ8EAtSo5VCyNQ8qI7B11U1nI37DJcrwvQBvAN02AXJHgGCqp4mYJHDW6OHhI7bnGB8FFC7Y5kLkfZ2fSxlleE4H3D%2FQbagpwNMlbr9TClK26iNHVpNmOadbNRuNqbxBa6cKNB3Bgze2PIlxMJYPTY6fr14RS%2FLC5d1GxsohhPsqUOB29Y3cQP80kMVv6BTrFjznsK5BQFnDlOmYTAmYErSIN514zC69R7bRSiiLULVp%2B9QXhde0FYkb6hmwZu%2BqN4ki0yCbPDQxqM6SHdTYF2grhBwnSWvHf%2BAiwjPj36e0Hs%2F3kJRY%2FsdLBHJPrPWe8cE6Haz4AFJc%2BylN8iGMknnn%2FoedTq99C8hdgwcAV%2FyvZYdu6kh5pU%2Bg2izAeWCt%2BE3uU7l9CDRXCBuuDXEK2pVSzG%2BKBiEQxqhxF2jO9Vxj%2FEMnP5RYbM9oNO8QAf9w2GetQ54n4W61wd49fwcBru8PAcY%2Bxds2i0jJ2WphcNtcZBkXnQrMiHkukjoPDKPPZES2bSFTGijgo4ujfcD1ROuUz%2FLvbsca35XOTt4fcjfizwjeGangYhGib9cA4yUAY9HV%2BRMoV79ERlrFkH%2FQCW4CRYvKSIYzFPJ694hUEO4cFFN0%2FPjMy%2F2Tn0twkBncJ5Zii5B4ApXyQyXflC2a39uHxEE3hQG4wjPaoRmPWSwFFtF8JGI2oEI3MUk5OJej71Co6l9qDRjQ826uxUUZVKRD2S%2FVUZtpJjLnpcPerK0P5osavj9b2VcJyP6qXLW7S%2BMZWHMprX5B4jhBmYWzpOp9r--PihUqCzcWT1KPHId--krxwWRovoLZw7XQq4CigsA%3D%3D",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('github_tyz.html', 'w', encoding='utf-8') as fp:
  fp.write(content)