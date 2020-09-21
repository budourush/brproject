import requests
import datetime

base_url = "https://www.boatrace.jp/owpc/pc/race/index"
racelist = "racelist?"

response = requests.get(base_url)
response.text
dt_today = datetime.date.today()
date_str = dt_today.strftime('%Y%m%d')

file = "race_list_{}.txt".format(date_str)
fileobj = open("./text/" + file, "w", encoding="utf_8")
fileobj.write(response.text)
fileobj.close()
