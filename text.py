import requests

r = requests.get("https://www.dropbox.com/sh/afegxsw8f41vfbm/AABgihmIL0wui7WpNqD2JyWLa")
my_content = r.text.split('"fileSharedLinkInfos": [{"url":')[0].split('"contents": ')[1]

null = 0
false = False
this_dict = eval( my_content[:-2] + "}")
print this_dict

