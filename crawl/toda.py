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

players_start_win_percent_dict = {"flying": None, "delay": None, "average_start": None,
                                  "world_area_in_first": None, "world_area_in_second": None,
                                  "world_area_in_third": None,
                                  "local_area_in_first": None, "local_area_in_second": None,
                                  "local_area_in_third": None}
players_start_win_percent_list = []
machine_win_percent_dict_dict = {"motor_no": None, "motor_in_second": None, "motor_in_third": None,
                                 "boat_no": None, "boat_in_second": None, "boat_in_third": None}
machine_win_percent_dict_list = []
# start_status, win_percent
for player_index, player_info_soup in enumerate(players_info_soup):
    for type_index, tmp in enumerate(player_info_soup.find_all("td", {"class": "is-lineH2", "rowspan": "4"})):
        # print(player_index)
        # print(type_index)
        # print(tmp.get_text().split())
        if type_index == 0:
            tmp_dict_1 = players_start_win_percent_dict.copy()
            tmp_dict_1["flying"] = tmp.get_text().split()[0]
            tmp_dict_1["delay"] = tmp.get_text().split()[1]
            tmp_dict_1["average_start"] = tmp.get_text().split()[2]
            players_start_win_percent_list.append(tmp_dict_1)
        if type_index == 1:
            players_start_win_percent_list[player_index]["world_area_in_first"] = tmp.get_text().split()[0]
            players_start_win_percent_list[player_index]["world_area_in_second"] = tmp.get_text().split()[1]
            players_start_win_percent_list[player_index]["world_area_in_third"] = tmp.get_text().split()[2]
        if type_index == 2:
            players_start_win_percent_list[player_index]["local_area_in_first"] = tmp.get_text().split()[0]
            players_start_win_percent_list[player_index]["local_area_in_second"] = tmp.get_text().split()[1]
            players_start_win_percent_list[player_index]["local_area_in_third"] = tmp.get_text().split()[2]
        if type_index == 3:
            tmp_dict_2 = machine_win_percent_dict_dict.copy()
            tmp_dict_2["motor_no"] = tmp.get_text().split()[0]
            tmp_dict_2["motor_in_second"] = tmp.get_text().split()[1]
            tmp_dict_2["motor_in_third"] = tmp.get_text().split()[2]
            machine_win_percent_dict_list.append(tmp_dict_2)
        if type_index == 4:
            machine_win_percent_dict_list[player_index]["boat_no"] = tmp.get_text().split()[0]
            machine_win_percent_dict_list[player_index]["boat_in_second"] = tmp.get_text().split()[1]
            machine_win_percent_dict_list[player_index]["boat_in_third"] = tmp.get_text().split()[2]

print(players_start_win_percent_list)
print(machine_win_percent_dict_list)