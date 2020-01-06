counter = 0

for i in range(197487, 673251):
    hasDup = False
    increasing = True

    tempI = i
    prev = int(i / 10**5)
    for j in range(1, 6):
        var = 10**(5-j)
        temp = int(i / var) % 10

        if temp < prev:
            increasing = False
            break

        if temp == prev:
            hasDup = True

        prev = temp

    if hasDup and increasing:
        counter += 1
        print(i)
        

print(counter)
