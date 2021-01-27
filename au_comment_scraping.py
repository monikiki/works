import requests
import time
from bs4 import BeautifulSoup
import pandas as pd 

writer = pd.ExcelWriter("/Users/Caijing/Desktop/au comment.xlsx")
reviewList = []
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"}
for i in range(1, 171):
    time.sleep(3)
    url = f"https://news.yahoo.co.jp/comment/plugin/v1/full/?origin=https%3A%2F%2Fnews.yahoo.co.jp&page={i}&sort=lost_points&order=desc&type=t&topic_id=20210113-00000032-zdn_m&space_id=2079510507&content_id=&full_page_url=https%3A%2F%2Fheadlines.yahoo.co.jp%2Fcm%2Fmain%3Fd%3D20210113-00000032-zdn_m-sci&comment_num=10&ref=&bkt=&flt=2&grp=&opttype=&disable_total_count=&compact=&compact_initial_view=&display_author_banner=off&mtestid=mfn_3895%3D%26mfn_5169%3D%26mfn_5358%3D%26mfn_5608%3Dp02ct&display_blurred_comment=off&ua=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2011_1_0)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F87.0.4280.141%20Safari%2F537.36"

    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    content_all = soup.find_all(class_="cmtBody")

    for content in content_all:
        review = content.text
        reviewList.append(review)

dic = {"review": reviewList}
info = pd.DataFrame(dic)
info.to_excel(writer, sheet_name="review")
writer.save()
writer.close()  

print("done")   

