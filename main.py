from bs4 import BeautifulSoup
import requests
from decouple import config

content = ''
print('Wait as we get the most trending news for you')
def scrape_news(url):
    print('Wait as we get the most trending news for you')
    cnt = ''
    cnt +=('<b>Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        #create rows for enumeration if tag isnt More, else throw a blank
        cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
        #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    return(cnt)

print('Content returned')

#take url input, format returned response
cnt = scrape_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>--------------<br>')
content +=('<br><br>This is we have for you')

print(cnt)

#Email authentication parameters
#Create email smtp server, and expose its port
SERVER = "smtp.gmail.com"
PORT = '587'

FROM = config('MYGMAIL')
print(FROM)
TO = config('MYGMAIL2')
print(TO)
PASS = config('PASS')
print(PASS)