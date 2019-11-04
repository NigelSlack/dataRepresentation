# Get gitub data for Andrew Beatty followers. Put into json and excel files.
import requests, json, sys
from xlwt import *

# Get the data
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()

# Extract the field names into a variable cl 
cl=[]
for i in data[0]:
  cl.append(i)  
  
#Get the file name for the new file to write, and put the data into a json file
filename = 'githubusers.json'
with open(filename, 'w') as f:
  json.dump(data, f, indent=4)

# Write the data into an excel file
w=Workbook()
ws=w.add_sheet('GitFollowers')

# Write the field names into the first row
row=0
ic=0
for i in data[0]:
  ws.write(row,ic,i)
  ic+=1

# Put the details for each follower into separate rows
row+=1
for i in data:  
  ic=0  
  for ix in cl:  
      ws.write(row,ic,i[ix])
      ic+=1
  row+=1    

# Save the file as gitfollowers.xls
w.save('gitfollowers.xls')