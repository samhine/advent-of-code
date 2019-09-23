import csv

with open('day4csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)

def noanagrams(l):
    sl = []
    for item in l:
        sl.append(set(item))

    # Check if any two values of sl are equal
    while len(sl)>0:
        if sl.pop() in sl:
            return False
    
    return True

    

c=0
for row in mylist:
    newrow = [i for i in row if len(i)!=0]

    if len(set(newrow))==len(newrow) and noanagrams(newrow):
        c+=1

print(c)