import requests
import json
url='https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
apiKey = 'b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e'
response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
outfile='outfile'
f=open(outfile,'w')
#print (response.json())
json.dump(repoJSON, f, indent=4)