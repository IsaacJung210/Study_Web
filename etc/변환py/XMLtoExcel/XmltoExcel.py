# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

output_path = "output"
output_file = "car1.csv"           #excel파일 이름
if not os.path.exists(output_path):
    os.makedirs(output_path)

df = pd.DataFrame(columns=['statNm', 'statId', 'chgerId', 'chgerType', 'addr', 'location', 'lat','lng','useTime','busiId','bnm','busiNm','busiCall','stat','statUpdDt','lastTsdt','lastTedt','nowTsdt','powerType','output','method','zcode','parkingFree','note','limitYn','limitDetail','delYn','delDetail']) # 엑셀 헤더정보

i=0

#XML 주소 넣는 곳
url = 'http://apis.data.go.kr/B552584/EvChargerInfo?serviceKey=blria7TY6VCPbn8QUgYrHz5RNNYWej29%2BHalh6YgL1DzuZApx70h2jqf9Y3bMDXQcfleL1v%2Fl548DEzZXKMSWg%3D%3D&pageNo=1&numOfRows=18500&zcode=11'

data = urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")
items = soup.find("items")

charge = "-"

for item in items.findAll("item"):

    if (item.charge != None):
        charge = item.charge.text
    else:
        charge = "-"

    df.loc[i] = [item.arrplacenm.text, item.arrplandtime.text, charge, item.depplacenm.text,
                 item.depplandtime.text, item.gradenm.text, item.routeid.text]

    i=i+1

df.to_csv(os.path.join(output_path, output_file), encoding='euc-kr', index=False)

df['arrPlandTime'] = '="' + df['arrPlandTime'] + '"'
df['depPlandTime'] = '="' + df['depPlandTime'] + '"'