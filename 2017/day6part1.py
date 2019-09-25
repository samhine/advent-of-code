
import copy

curr = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
# part 2
curr = [1, 0, 14, 14, 12, 11, 10, 9, 9, 7, 5, 5, 4, 3, 7, 1]

list_len = len(curr)

histories = []

c=0

# part 1
while curr not in histories:
    histories.append(copy.copy(curr))

    max_val = max(curr)
    max_ind = curr.index(max_val)

    rem = max_val%list_len
    quo = max_val//list_len

    curr[max_ind] = 0

    # Dealing with quotient
    curr = [n+quo for n in curr]

    # Dealing with remainder
    p = 1
    for i in range(rem):
        try:
            curr[max_ind+p] += 1
        except IndexError:
            curr[max_ind+p-list_len] += 1
        p += 1

    c+=1

    # print(curr)
print(c)
print(curr)