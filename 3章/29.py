import requests
fig_name = data_info['国旗画像'].replace(' ', '_')
url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + fig_name + '&prop=imageinfo&iiprop=url&format=json'
data = requests.get(url).text
print(data)
print('\n')

pattern = r'\"url\":\"([^\"]+?)\"'
res_url = re.findall(pattern, data)
print(res_url[0])