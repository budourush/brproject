import requests
from bs4 import BeautifulSoup

# view-source:http://www.boatrace.jp/owpc/pc/race/raceresult?rno=12&jcd=02&hd=20200902
# base_url = "http://www.boatrace.jp/owpc/pc/race/"
# racelist = "racelist?"
#
# rno = "1"
# jcd = "01"
# hd = "20200909"
#
# url = base_url + racelist + "rno={}&jcd={}&hd={}".format(rno, jcd, hd)
# response = requests.get(url)
path = "text/01_20200909_1_racelist.txt"
with open(path, encoding="utf_8") as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

# 出走選手取得
players_info_soup = soup.find_all("tbody", {"class": "is-fs12"})
players_info_dict = {"player_name": None, "player_number": None, "player_rank": None, "player_area": None,
                     "player_birth_area": None, "player_age": None, "player_weight": None}
players_info_list = []
player_names = [tmp for tmp in soup.find_all("div", {"class": "is-fs18 is-fBold"})]
for player_name in player_names:
    for name in player_name.find_all("a"):
        # TODO "全角スぺース"削除
        tmp_dict = players_info_dict.copy()
        tmp_dict["player_name"] = name.get_text()
        players_info_list.append(tmp_dict)

for i, player_info_soup in enumerate(players_info_soup):
    for turn, tmp in enumerate(player_info_soup.find_all("div", {"class": "is-fs11"})):
        if turn == 0:
            players_info_list[i]["player_number"] = tmp.get_text().split()[0]
            players_info_list[i]["player_rank"] = tmp.get_text().split()[2]
        if turn == 1:
            area_list = tmp.get_text().split()[0].split("/")
            players_info_list[i]["player_area"] = area_list[0]
            players_info_list[i]["player_birth_area"] = area_list[1]
            player_status_list = tmp.get_text().split()[1].split("/")
            # TODO "歳"削除
            players_info_list[i]["player_age"] = player_status_list[0]
            # TODO kg"削除
            players_info_list[i]["player_weight"] = player_status_list[1]
print(players_info_list)
