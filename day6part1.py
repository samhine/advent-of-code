
# UNFINISHED
curr = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
curr = [0, 2, 7, 0]
list_len = len(curr)
histories = []

c=0

while c<6:
    if curr not in histories:
        histories.append(curr)
    else:
        break
    max_val = max(curr)
    max_ind = curr.index(max_val)

    rem = max_val%list_len
    quo = max_val//list_len

    curr[max_ind] = 0

    # Dealing with quotient
    curr = [n+quo for n in curr]

    # Dealing with remainder
    if max_ind+1+rem>len(curr)-1:
        overhang = rem-(len(curr)-max_ind+1)
        curr[max_ind+1:] = [n+1 for n in curr[max_ind+1:]]
        curr[:overhang] = [n+1 for n in curr[:overhang]]
    else:
        curr[max_ind+1:max_ind+1+rem] = [n+1 for n in curr[max_ind+1:max_ind+1+rem]]
    
    print(curr)

    c+=1

print(c)
print(len(histories))