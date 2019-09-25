import csv

with open('day5csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)

reflist = [int(i[0]) for i in mylist]

c=0
p=0
while True:
    try:
        val = reflist[p]
        if val>=3:
            reflist[p]-=1
        else:
            reflist[p]+=1

        p+=val
        c+=1
    except IndexError:
        break

print(c)