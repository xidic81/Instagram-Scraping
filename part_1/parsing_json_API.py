import requests, json

url = 'https://www.instagram.com/graphql/query'

short_code = input('Masukin short code: ')

var = {"shortcode":short_code,"include_reel":True,"first":50}
headers = {'cookie': 'sessionid=352906921%3AMO1jDpfOUQLSzB%3A29'}
params = {
    'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
    'variables': json.dumps(var)
}

r = requests.get(url, headers=headers, params=params).json()

users = r['data']['shortcode_media']['edge_liked_by']['edges']

count = 0
for user in users:
    username = user['node']['username']
    full_name = user['node']['full_name']
    profil_pic = user['node']['profile_pic_url']

    print(username, full_name, profil_pic)
    count += 1
    print(count)