import csv

with open('day8csv.csv', 'r') as f:
  reader = csv.reader(f)
  mylist = list(reader)

# Holds variables and their values
vari = dict()

maxval = 0
for item in mylist:
    # Check variables exist in vari
    if item[0] not in list(vari):
        vari.update({item[0]:0})
    if item[4] not in list(vari):
        vari.update({item[4]:0})

    exp = 'vari[item[4]]'+item[5]+'int(item[6])'
    b = eval(exp)

    print(b)

    if b:
        if item[1]=='inc':
            vari[item[0]] += int(item[2])
        elif item[1]=='dec':
            vari[item[0]] -= int(item[2])

    if vari[item[0]]>maxval:
        maxval = vari[item[0]]


maxkey = 'o'
for key, val in vari.items():
    if val>vari[maxkey]:
        maxkey=key

print('Max value at end of operations:', vari[maxkey])
print('Max value over all operations:', maxval)