from collections import defaultdict
import json
import requests

MEMBER_API_URL = "https://h5.48.cn/resource/jsonp/allmembers.php?gid=00"

# Remove inactive members from the JSON
def filter_response(json_info):
    snh_teams = defaultdict(list)
    all_members = json_info["rows"]
    for member in all_members:
        status = member["status"]
        team_name = member["tname"].lower()
        # status is 44 for inactive members
        if status == "99" and team_name != "idft":
            snh_teams[team_name].append(member)
    return snh_teams

# Return active SNH member info organized by team
def scrape_info():
    response = requests.get(MEMBER_API_URL)
    json_info = json.loads(response.text)
    snh_teams = filter_response(json_info)
    return snh_teams

# Regenerate the SNH48 Group member information file
if __name__ == "__main__":
    json_to_write = scrape_info()
    with open("members.json", "w") as f:
        json.dump(json_to_write, f, ensure_ascii=False)