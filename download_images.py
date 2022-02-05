import json
import requests
import shutil

# Download image given a single member_id
def download_image(member_id):
    image_url = f"https://www.snh48.com/images/member/zp_{member_id}.jpg"
    filename = f"{member_id}.jpg"

    r = requests.get(image_url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    else:
        print("Image Couldn\'t be retreived")

# Download images of all members in members.json
if __name__ == "__main__":
    f = open("members.json")
    members = json.load(f)
    for team in members:
        for member in members[team]:
            download_image(member["sid"])