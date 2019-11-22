#터미널 > pip install bs4
#터미널 > pip install lxml

from bs4 import BeautifulSoup       #html 구조적으로 변환하자
from urllib.request import urlopen  #url에 해당하는 html 가져오자

if __name__ == '__main__':
    #네이버 웹툰 > 신의 탑 제목 가져오자
    # data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559")
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=651673")   #유미의 세포들
    soup = BeautifulSoup(data, "lxml")
    # print(soup)
    cartoon_titles = soup.find_all("td", attrs={'class':'title'})   #<td class="title">
    html = "<html><head><meta charset='utf-8'></head><body>"
    for title in cartoon_titles:
        t = title.find('a').text    #제목 가져오자
        link = title.find('a').get("href")
        link = "http://comic.naver.com"+link
        # print(t)
        # print(link)
        # print("<a href='"+link+"'>"+t+"</a>")
        html+="<a href='"+link+"'>"+t+"</a><br/>"
    html+="</body></html>"
    outoutSoup = BeautifulSoup(html, "lxml")        #htmlstring ->
    prettyHtml = str(outoutSoup.prettify())
    with open("유미의세포들.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)

    #다음 웹툰 > 어쩌다 발견한 7월 제목 가져오자
    # data = urlopen("http://webtoon.daum.net/webtoon/view/findjuly")     #url -> httpResponse객체
    # soup = BeautifulSoup(data, "lxml")
    # print(soup)
    # cartoon_titles = soup.find_all("strong", attrs={"class":"tit_wt"})
    # for title in cartoon_titles:
    #     print(title)