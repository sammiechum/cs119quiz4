#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:38:03 2023

@author: sammiechum
"""
import sys, re
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
                # key = word
                value = library[i]["value"]
                print(key,"\t",value)


def main(argv):
    line = sys.stdin.readline()
    with open('AFINN.txt', 'r') as file:
        for line in file:
            words = line.split()
            dict = {
                "word": words[0],
                "value": words[1] }
            library.append(dict)
        # print(library)
    
    try:
        while line:
            determineValence(line)
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
