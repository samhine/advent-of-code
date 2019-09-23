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

# 3 cases
# 1) We're continuing along our current path
# 2) We're turning onto a path along the x-axis
# 3) We're turning onto a path along the y-axis

# Conditions for cases
# 1) We haven't reached a limit for the x or y
# 2) We reach the pylim (and subsequently increment it by 1) - our xpos is then decrementing
# 3) We reach the pxlim (and subsequently increment it by 1) - our ypos is then incrementing
# 4) We reach the nylim (and subsequently decrement it by 1) - our xpos is then incrementing
# 5) We reach the nxlim (and subsequently decrement it by 1) - our ypos is then decrementing
while val<347991:

    # 4 while statements? (one for each direction)
    if direc==1 and xpos<pxlim:
        val += 1
        xpos += 1
    elif direc==1 and xpos==pxlim:
        val +=1
        ypos += 1

        direc = 2
        pxlim += 1
    elif direc==2 and ypos<pylim:
        val += 1
        ypos += 1
    elif direc==2 and ypos==pylim:
        val += 1
        xpos -= 1

        direc = 3
        pylim += 1
    elif direc==3 and xpos>nxlim:
        val += 1
        xpos -= 1
    elif direc==3 and xpos==nxlim:
        val += 1
        ypos -= 1

        direc = 4
        nxlim -= 1
    elif direc==4 and ypos>nylim:
        val +=1 
        ypos -= 1
    elif direc==4 and ypos==nylim:
        val += 1
        xpos += 1

        direc = 1
        nylim -= 1

print(xpos, ypos)




