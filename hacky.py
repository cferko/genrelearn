# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:31:50 2016

@author: cferko
"""

"""
This is a hacky file to get individual Dropbox links from folders
"""

import requests

blues = "https://www.dropbox.com/sh/afegxsw8f41vfbm/AABgihmIL0wui7WpNqD2JyWLa"
classical = "https://www.dropbox.com/sh/1cctr3dfrjccpdy/AACgSm9YHi0aZ1baEcIa-5LZa"
country = "https://www.dropbox.com/sh/tyz3t14h5r5i49n/AAAKvEOTggtAEpb5aa9VCCRpa"
disco = "https://www.dropbox.com/sh/raf3ew7bvle3z2p/AADignlKtvRn6YJnUL3Gv2Nka"
hiphop = "https://www.dropbox.com/sh/rknigscckkp15et/AAD94jEQMRrEkpbCPi1KB7qMa"
jazz = "https://www.dropbox.com/sh/ceji0dmoyie2orq/AADXabt75PElJW9WNCBvBQ51a"
metal = "https://www.dropbox.com/sh/gqhgkkuvg6akab8/AADR6U9-cVwT5oBdL1_98iOya"
pop = "https://www.dropbox.com/sh/r7a0ya4679z1w1s/AAD1A7dnj0EHL20U4Iwhnp-va"
reggae = "https://www.dropbox.com/sh/6unjnco4qqplysb/AADfq-Pg-AeaKMPFuqA3v-iFa"
rock = "https://www.dropbox.com/sh/uotvtqu4g8fcu63/AADFFyOkEtfVMe4o_KHx3Yqja"

genres = ["blues",
          "classical",
          "country",
          "disco",
          "hiphop",
          "jazz",
          "metal",
          "pop",
          "reggae",
          "rock"]

genre_map = {g:eval(g) for g in genres}
## I know, evals are satan, sue me

## This part is so JSON entries don't freak Python out
null = 0
false = False

def handle_list(my_list):
    out = {}
    
    for item in my_list:
        try:
            out[item['filename']] = item['href'].replace('dl=0', 'dl=1')
        except:
            continue
        
    return out

dict_list = []
for genre, url in genre_map.items():
    r = requests.get(url)

    print "doing", genre    
    
    my_content = r.text.split('"fileSharedLinkInfos": [{"url":')[0].split('"contents": ')[1]
    
    print type(my_content)    
    
    if ".au" in my_content:
        this_list = eval( '[' + my_content[:-2] + "} ]")[0]["files"]
        parsed_dict = handle_list(this_list)
        dict_list.append(parsed_dict)

    else:
        print my_content
        raise

#print dict_list