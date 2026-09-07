LEVEL = 8
star = 1
blank = 0
full_fill = 1+2*(LEVEL-1)
for i in range(LEVEL):
    blank = (full_fill - star)/2
    for j in range(int(blank)):
        print(" ", end="")
    for j in range(star):
        print("*", end="")
    print("\n")    
    star += 2