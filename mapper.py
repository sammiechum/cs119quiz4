#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:38:03 2023

@author: sammiechum
"""
import sys, re
import gzip
import tarfile
import os
import string
library = []

def clean_text(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return text


def determineValence(content):
    cleaned = clean_text(content)
    words = cleaned.split()
    for word in words:
        for i in range (len(library)):
            if (library[i]["word"] == word):
                key = os.environ['mapreduce_map_input_file']
                value = library[i]["value"]
                print(key,"\t",value)


def main(argv):
    # line = sys.stdin.readline()
    with open(argv[2], 'r') as file:
        for line in file:
            words = line.split()
            dict = {
                "word": words[0],
                "value": words[1] }
            library.append(dict)
        # print(library)
            
    for gz_file in os.listdir(argv[1]):
        pathtofile = os.path.join(argv[1],gz_file)
        
        # print(pathtofile)
        with gzip.open(pathtofile, 'rb') as gz_file:
        # Read the contents of the compressed file
            # print(gz_file)
            with tarfile.open(fileobj= gz_file, mode='r') as tar:
            # List the contents of the tar archive (optional)
                # print(tar.list())
                for txt in tar.getmembers():
                    speech = tar.extractfile(txt)
                    if speech:
                        content = speech.read()
                        determineValence(content)
                        # print(content.decode('utf-8'))

if __name__ == "__main__":
    main(sys.argv)
