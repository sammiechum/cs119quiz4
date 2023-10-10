#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_totalValence = 0
word = None
count = 0
totalvalence = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, valence = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        valence = float(valence)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_totalValence += valence
        count += 1.0
        # print("Valence is", valence, "count is", count)
    else:
        if current_word:
            # write result to STDOUT
            average = float(current_totalValence/count)
            print ('%s\t%s' % (current_word, average))
            print("Total sum is", current_totalValence, "number of words is", count)
            # print ('%s\t%s' % (current_totalValence, count))
        # print("Reset for next word")
        count = 1
        current_word = word
        current_totalValence = valence
        # print(current_word, current_totalValence)
    
    
# # do not forget to output the last word if needed!
if current_word == word:
    average = current_totalValence/count
    print ('%s\t%s' % (current_word, average))
