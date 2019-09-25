pxlim=1
nxlim=-1
pylim=1
nylim=-1

# 4 directions
# 1 = right, 2 = up, 3 = left, 4 = down
direc = 1

xpos=0
ypos=0

val=0

# Holding position values in dictionary (could get messy)
foundpositions = {
    "0,0" : 1,
}

# Find the value of a position based on the values of positions we already have
def get_val_on_position(xpos, ypos):
    val = 0

    # The 8 positions surrounding the current coordinate
    coords = [
        str(xpos+1)+","+str(ypos),
        str(xpos+1)+","+str(ypos+1),
        str(xpos)+","+str(ypos+1),
        str(xpos-1)+","+str(ypos+1),
        str(xpos-1)+","+str(ypos),
        str(xpos-1)+","+str(ypos-1),
        str(xpos)+","+str(ypos-1),
        str(xpos+1)+","+str(ypos-1)
    ]

    for pos in coords:
        try: 
            val += foundpositions[pos]
        except KeyError:
            continue
    
    return val

# 3 cases
# 1) We're continuing along our current path
# 2) We're turning onto a path along the x-axis
# 3) We're turning onto a path along the y-axis

# Conditions for cases
# 1) We haven't reached a limit for the x or y
# 2) We reach the pylim (and subsequently increment it by 1) - our xpos is then decrementing
# 3) We reach the pxlim (and subsequently increment it by 1) - our ypos is then incrementing
# 2) We reach the nylim (and subsequently decrement it by 1) - our xpos is then incrementing
# 3) We reach the nxlim (and subsequently decrement it by 1) - our ypos is then decrementing
while val<347991:

    # 4 while statements? (one for each direction)
    if direc==1 and xpos<pxlim:
        xpos += 1
    elif direc==1 and xpos==pxlim:
        ypos += 1

        direc = 2
        pxlim += 1
    elif direc==2 and ypos<pylim:
        ypos += 1
    elif direc==2 and ypos==pylim:
        xpos -= 1

        direc = 3
        pylim += 1
    elif direc==3 and xpos>nxlim:
        xpos -= 1
    elif direc==3 and xpos==nxlim:
        ypos -= 1

        direc = 4
        nxlim -= 1
    elif direc==4 and ypos>nylim:
        ypos -= 1
    elif direc==4 and ypos==nylim:
        xpos += 1

        direc = 1
        nylim -= 1
    else:
        continue

    val = get_val_on_position(xpos, ypos)
    foundpositions.update({str(xpos)+","+str(ypos) : val})

print(foundpositions[str(xpos)+","+str(ypos)])