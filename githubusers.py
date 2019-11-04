import requests, json, sys
from xlwt import *
#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
print (type(data))
#key, val = data.items()[0]
#print(key)
cl=[]
for i in data[0]:
  cl.append(i)  
  print(i)

print(cl)
#Get the file name for the new file to write
# filename = 'githubusers.json'
# with open(filename, 'w') as f:
# json.dump(data, f, indent=4)
# sys.exit()

w=Workbook()
ws=w.add_sheet('GitFollowers')
row=0
ic=0
for i in data[0]:
  ws.write(row,ic,i)
  ic+=1

row+=1
for i in data:  
  ic=0  
  for ix in cl:  
      ws.write(row,ic,i[ix])
      ic+=1
  row+=1    

w.save('gitfollowers.xls')