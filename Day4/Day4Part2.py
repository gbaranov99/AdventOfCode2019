counter = 0

for i in range(197487, 673251):
    increasing = True

    tempI = i
    prev = int(i / 10**5)
    
    twovalid = False
    exactly2 = False
    continuingDup = False
    twoInRow = False

    for j in range(1, 6):
        var = 10**(5-j)
        temp = int(i / var) % 10

        if temp < prev:
            increasing = False
            break

        if temp == prev:
            if not continuingDup:
                if twoInRow:
                    continuingDup = True
                    exactly2 = False
                else:
                    exactly2 = True
                twoInRow = True
        else:
            if exactly2:
                twovalid = True
            continuingDup = False
            twoInRow = False

        if j == 5 and exactly2 and not continuingDup and twoInRow:
            twovalid = True


        prev = temp

    if increasing and twovalid:
        counter += 1
        print(i)
        

print(counter)
