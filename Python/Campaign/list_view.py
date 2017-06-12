import requests as req
import json

url = 'https://pranaymithaigari.api-us1.com/admin/api.php?'
api_key = '887e34bf5d820c992775f31d571974af6dfe8242fd48a1eb8c1e09ded8345a25ae47397d'
action = 'list_view'
api_output = 'json'
s_id = '3'

url = url + 'api_action=' + action + '&api_key=' + api_key + '&api_output=' + api_output + '&id=' + s_id

headers = {'Content-type': 'application/x-www-form-urlencoded'}

myresponse = req.get(url, headers=headers)

print myresponse.text
#print json.loads(myresponse.content).get('id')