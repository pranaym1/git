import requests as req


url = 'https://pranaymithaigari.api-us1.com/admin/api.php?'
api_key = '887e34bf5d820c992775f31d571974af6dfe8242fd48a1eb8c1e09ded8345a25ae47397d'
action = 'contact_add'
api_output = 'json'

url = url + 'api_action=' + action + '&api_key=' + api_key + '&api_output=' + api_output

params = {'email': 'pranay.mithaigari15@gmail.com', 'p[3]': 3, 'p[5]': 5}

headers = {'Content-type': 'application/x-www-form-urlencoded'}

myresponse = req.post(url, data=params, headers=headers)

print myresponse.text