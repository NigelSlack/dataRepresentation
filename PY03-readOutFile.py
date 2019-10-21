from bs4 import BeautifulSoup
with open("C:/Users/dingl/Documents/Data Representation/carviewer.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
print (soup.tr)
