# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:48:38 2016

@author: cferko
"""

import soundfile as sf
import requests, pickle, os, numpy as np
LOOKUP_DICT = pickle.load(open("file_lookup.pkl", "r"))

import IPython

def standardize(old_rate, audio):
    if audio.ndim == 2:
        audio = audio.mean(axis=1)
    
    if old_rate == 44100:
        return audio

    n = len(audio)
    upsample_factor = float(old_rate)/44100
    new_audio = np.interp(np.arange(0, n, upsample_factor),
                          np.arange(0, n, 1), audio)

    return new_audio

def listen(audio):
    return IPython.display.Audio(audio, rate = 44100)

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

def format_song_name(genre, number):
    """Helper function to get a filename
    
    Args:
        genre: a string, one of "blues", "classical", etc.
        number: an integer between 1 and 1000 (NOT zero-indexed)
        
    Returns:
        a string giving the filename for the specified song
    """
    zero_indexed_number = int(number) - 1
    padded_number = '{:05d}'.format(zero_indexed_number)
    
    name = genre + "." + padded_number + ".au"
    
    return name

def download_song(genre, number):
    """Fetches one of the 1000 songs
    
    Args:
        genre: a string, one of "blues", "classical", etc.
        number: an integer between 1 and 1000 (NOT zero-indexed)
        
    Returns:
        None (downloads the file to current directory)
    """
    name = format_song_name(genre, number)
    url = LOOKUP_DICT[name]
    download_file(url)
    
    return

def get_song(genre, number):
    """Student-facing convenience function to fetch a numpy array
    
    Args:
        genre: a string, one of "blues", "classical", etc.
        number: an integer between 1 and 1000 (NOT zero-indexed)
        
    Returns:
        None (downloads the file to current directory)
    """
    name = format_song_name(genre, number)
    if not os.path.isfile(name):
        download_song(genre, number)
        
    data, samplerate = sf.read(name)
    
    return standardize(samplerate, data)

def get_sample():
    closer = "https://www.dropbox.com/s/b7lcd4s7pvcroie/closer.wav?dl=1"
    
    if not os.path.isfile("closer.wav"):
        download_file(closer)
    d1, s1 = sf.read("closer.wav")

    return standardize(s1, d1)
    
if __name__ == "__main__":
    closer, rate = get_sample()