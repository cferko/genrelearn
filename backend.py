# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:48:38 2016

@author: cferko
"""

import requests, pickle
LOOKUP_DICT = pickle.load(open("file_lookup.pkl", "r"))

def download_file(url):
    """Helper function to download a file with requests
    
    Args:
        url: a string pointing at a url with a downloadable resource
        
    Returns:
        the filename of the resource, on a successful return
    """
    local_filename = url.split('/')[-1].split("?")[0]
    # Hack to strip off the filename
    
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    
    return local_filename

def get_song(genre, number):
    """Fetches one of the 1000 songs
    
    Args:
        genre: a string, one of "blues", "classical", etc.
        number: an integer between 1 and 1000 (NOT zero-indexed)
        
    Returns:
        None (downloads the file to current directory)
    """
    zero_indexed_number = int(number) - 1
    padded_number = '{:05d}'.format(zero_indexed_number)
    
    name = genre + "." + padded_number + ".au"
    url = LOOKUP_DICT[name]
    download_file(url)
    
    return

get_song("blues", 5)