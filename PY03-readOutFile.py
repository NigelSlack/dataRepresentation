from bs4 import BeautifulSoup
with open("C:/Users/dingl/Documents/Data Representation/carviewer.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
rows = soup.findAll("tr")
for row in rows:
 #print(row)
 cols = row.findAll("td")
 dataList = []
 for col in cols:
   dataList.append(col.text)
 print (dataList)

