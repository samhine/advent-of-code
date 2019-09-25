import csv

with open('day7csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)

mydict = {}

for item in mylist:
    mydict.update({ item[0] : item[2:]})

disc = list(mydict)[0]
flag = True
while flag:
    flag = False
    for key, val in mydict.items():
        if disc in val:
            disc = key
            flag = True
            break
            
print(disc)
