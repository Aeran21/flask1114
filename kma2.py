from urllib import request
from bs4 import BeautifulSoup
 
# https://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
# 경상남북도 중기예보
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=133")
 
# BeautifulSoup을 사용해 웹 페이지를 분석합니다.
soup = BeautifulSoup(target, "html.parser")
 
# 제목발표날짜 출력
 
output =""

for item in soup.select("item"):
    output += "<h3>{}</h3><hr/>".format(item.select_one("title").string)
# location 태그를 찾습니다.

for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()
 
# 제목, 날짜, 지역, 세부정보 출력
print(soup.select_one("title").string)
print("날짜:", location.select_one("tmEf").string)
print("지역:", soup.select_one("province").string)
