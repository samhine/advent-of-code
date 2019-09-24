# -*- coding: utf-8 -*-
import random 

with open('shaney_training.txt', 'r') as file:
    data = file.read()

# We don't really want to limit our output because of grammer
data = data.lower()

# Keys are words, value is a list of following words from that word, which are selected uniformly within the MC
# This way, more common following words are intrisically more likely to be picked from the uniform process
links = dict()
data_split = data.replace('\n', ' ').split(' ')
lim = len(data_split)
context = 2

for i, word in enumerate(data_split):
    if str(data_split[i:i+2]) not in list(links):
        links.update({str(data_split[i:i+context]):[]})

    if i<lim-context:
        links[str(data_split[i:i+context])].append(data_split[i+context])
    else:
        break

# Number of words for our new text
txt_len = 200

start_idx = random.randint(0,len(data_split)-context)
words = data_split[start_idx:start_idx+context]
txt = ' '.join(words)

for c in range(txt_len):
    next_word = random.choice(links[str(words)])
    txt+=" "+next_word

    words.pop(0)
    words.append(next_word)

print(txt)