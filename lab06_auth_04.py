# try to change a field in Github repository
import requests
import json
url='https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
apiKey = 'b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e'
response = requests.get(url, auth=('token',apiKey))
data = response.json()
co=data['stargazers_count']
data['stargazers_count']=2
print(data)
print(' ')
print('------------------------------------------------------------------------')
print(' ')
response = requests.post(url, auth=('token',apiKey),json=data)
print(response.status_code)
print (response.json())
print(' ')
print('------------------------------------------------------------------------')
print(' ')
data['stargazers_count']=co
response = requests.post(url, auth=('token',apiKey),json=data)
print(response.status_code)
print (response.json())