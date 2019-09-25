import csv

with open('day2csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)

c=0
for row in mylist:
    row = [int(i) for i in row]

    for divisor in row:
        for dividend in row:
            if dividend%divisor==0 and dividend!=divisor:
                c+=dividend//divisor
                break

print(c)