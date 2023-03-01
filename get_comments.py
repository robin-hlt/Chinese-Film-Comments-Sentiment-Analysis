from urllib import request
from bs4 import BeautifulSoup
import time
import random


def get_page(url,headers):
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    url_string = response.read().decode('utf-8')
    return url_string


def write_file(rating,content):
    f = open('raw_comments.txt', 'a',encoding='utf-8')
    f.write(rating)
    f.write('\t')
    f.write(str(content))
    f.write('\n')
    f.close()

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
]
for i in range(20,5000,20):
    rand = random.randint(0,7)
    headers = {'User-Agent': user_agents[rand]}
    url = 'https://movie.douban.com/subject/19944106/comments?start=' + str(i) + '&limit=20&status=P&sort=new_score'
    s = get_page(url, headers)
    soup = BeautifulSoup(s, 'html.parser')
    comments = soup.find_all(class_='comment-item')
    for item in comments:
        content = item.find(class_='short').string
        rating = item.find(class_='comment-info').find_all('span')[1].get('title')
        print(content)
        print(rating)
        write_file(rating,content)
    time.sleep(10)



