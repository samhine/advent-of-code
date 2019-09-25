with open('day1txt.txt', 'r') as file:
    data = file.read()

data_split = data.split('\n')

v = 0
for i in data_split:
    v += int(i)

print(v)

# Part 2
hist = set() # The difference a set makes is massive <3 

i=0
v=0
while v not in hist:
    hist.add(v)
    v += int(data_split[i%len(data_split)])
    i += 1
    
print(v)