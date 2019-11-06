# Get my Github dataRepresentation repository info, into file outfile2
import requests
import json
url='https://api.github.com/repos/NigelSlack/dataRepresentation'
response = requests.get(url)
repoJSON = response.json()
outfile='outfile2'
f=open(outfile,'w')
json.dump(repoJSON, f, indent=4)