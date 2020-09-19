import requests
from bs4 import BeautifulSoup

# view-source:http://www.boatrace.jp/owpc/pc/race/raceresult?rno=12&jcd=02&hd=20200902
base_url = "http://www.boatrace.jp/owpc/pc/race/"
racelist = "racelist?"

rno = "1"
jcd = "01"
hd = "20200909"

url = base_url + racelist + "rno={}&jcd={}&hd={}".format(rno, jcd, hd)
response = requests.get(url)
response.text

file = "{}_{}_{}_{}.txt".format(jcd, hd, rno, racelist[:-1])
fileobj = open("./text/" + file, "w", encoding="utf_8")
fileobj.write(response.text)
fileobj.close()
