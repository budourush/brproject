from bs4 import BeautifulSoup
import db_insert

path = "text/race_list_{}.txt".format("20200921")
with open(path, encoding="utf_8") as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

area_list = soup.find_all("td", {"class": "is-arrow1 is-fBold is-fs15"})
for aa in area_list:
    print(aa.find("img")["alt"][:-1])
