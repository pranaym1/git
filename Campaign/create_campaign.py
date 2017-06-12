import requests as req

url = 'https://pranaymithaigari.api-us1.com/admin/api.php?'
api_key = '887e34bf5d820c992775f31d571974af6dfe8242fd48a1eb8c1e09ded8345a25ae47397d'
action = 'campaign_create'
api_output = 'json'

url = url + 'api_action=' + action + '&api_key=' + api_key + '&api_output=' + api_output

params={'type': 'single', 'name': 'First_Campaign', 'sdate': '2017-04-26 00:40:00', 'status': '1', 'public': '0', 'tracklinks': 'all', 'p[1]': 3, 'm[1]': 100}

headers = {'Content-type': 'application/x-www-form-urlencoded'}

myresponse = req.post(url, data=params, headers=headers)

print myresponse.text
