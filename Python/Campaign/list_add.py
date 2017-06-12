import requests as req

url = 'https://pranaymithaigari.api-us1.com/admin/api.php?'
api_key = '887e34bf5d820c992775f31d571974af6dfe8242fd48a1eb8c1e09ded8345a25ae47397d'
action = 'list_add'
api_output = 'json'

url = url + 'api_action=' + action + '&api_key=' + api_key + '&api_output=' + api_output

name = 'list3'

params = {'name': name, 'subscription_notify': '', 'sender_addr1': '6263 McNeil Dr', 'sender_country': 'United States', 'sender_url': url, 'sender_zip': '78729', 'sender_city': 'Austin', 'sender_reminder': 'Thank you for subscribing', 'sender_name': 'Pranay'}

headers = {'Content-type': 'application/x-www-form-urlencoded'}

myresponse = req.post(url, data=params, headers=headers)

print myresponse.text
