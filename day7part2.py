# UNFINISHED
import csv

with open('day7csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)

mydict = {}
mydict_weights = {}

for item in mylist:
    mydict_weights.update({item[0]: -int(item[1])})

for item in mylist:
    mydict.update({ item[0] : item[2:]})

# Successfully traverses tree, just don't know how to keep track of which branch we are travelling down, and what information to hold at the time.
def get_child_weights(disc):
  children = mydict[disc]
  if children[0]=='':
    return mydict_weights[disc]
  l = [get_child_weights(d) for d in children if len(d)!=0]
  # We're told only 1 disc is incorrect, so we're looking for lists with only 1 element which is incorrect
  if len(set(l))==2:
    print(disc)
    print(l)
  return sum(l)

# We know this is the root element from part 1
disc = 'gynfwly'
weight_tree = get_child_weights(disc)

