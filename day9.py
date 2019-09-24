import copy

with open('day9txt.txt', 'r') as file:
    data = file.read()

print(len(data))

# Number of elements defines level of nest we are inside of groups
grp_stack = []

# Same as above. If this stack is not empty, we are currently looking at garbage
gar_stack = []

scores = []

gc = 0
cancels = 0
lastchar = ''
for char in data:
    if lastchar=='!':
        lastchar=''
        continue
    if char=='{' and not gar_stack:
        grp_stack.append('.')
    elif char=='}' and not gar_stack:
        scores.append(len(grp_stack))
        grp_stack.pop()
    elif char=='<' and not gar_stack:
        gar_stack.append('.')
    elif char=='>':
        gar_stack.pop()
        gc += 1
    elif gar_stack and char!='!':
        cancels += 1

    lastchar = copy.copy(char)

print(sum(scores))
print(cancels)