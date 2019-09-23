import csv

with open('day2csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)

c=0
for row in mylist:
    row = [int(i) for i in row]
    c+=(max(row)-min(row))

print(c)