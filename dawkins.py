import random, copy
from fuzzywuzzy import fuzz

alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ']
match_string = "METHINKS IT IS LIKE A WEASEL"

leven = True

def scorer(s, target):
    # Assumes same length 
    score = 0
    for idx, letter in enumerate(s):
        if letter==target[idx]:
            score += 1

    return score

# Generate 28 random chars
phr = [alph[random.randint(0,len(alph)-1)] for i in range(len(match_string))]
if leven: phr = [' ']
print(''.join(phr), 0)

score = 0
while score<100:
    # Repeat this 100 times
    phr_book = [copy.copy(phr) for i in range(100)]

    # Apply mutation
    scores = []
    # Iterate over phrases in the book
    for i, p in enumerate(phr_book):
        # Iterate over the characters in this phrase
        for j, s in enumerate(p):
            if leven:
                if random.random()<0.05:
                    phr_book[i][j] = alph[random.randint(0,len(alph)-1)]
                elif random.random()<0.05:
                    phr_book[i].pop(j)
                elif random.random()<0.05:
                    phr_book[i].insert(j, alph[random.randint(0,len(alph)-1)])
            else:
                if random.random()<0.05:
                    phr_book[i][j] = alph[random.randint(0,len(alph)-1)]
        if leven:
            scores.append(fuzz.ratio(''.join(p), match_string))
        else:
            scores.append(scorer(p, match_string))

    # Pick best score
    score = max(scores)
    phr_idx = scores.index(score)
    phr = phr_book[phr_idx]
    print(''.join(phr), score)

print(''.join(phr), score)