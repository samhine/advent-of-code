import csv

with open('day4csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)


c=0
for row in mylist:
    newrow = [i for i in row if len(i)!=0]

    if len(set(newrow))==len(newrow):
        c+=1

print(c)