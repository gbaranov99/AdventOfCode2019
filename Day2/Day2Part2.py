import copy

file = open('Day2File.txt', 'r')
data = file.read()
data = data.strip('\n')
data = data.split(',')


#print(data)
location = 0
length = len(data)

num1 = 0
num2 = 0
num3 = 0
num4 = 0


first = 1
second = 1

curData = copy.deepcopy(data)

while True:
    data[1] = first
    data[2] = second

    while location < length:
        num1 = int(data[location])
        if num1 == 99:
            break

        num2 = int(data[location + 1])
        num3 = int(data[location + 2])
        num4 = int(data[location + 3])

        if num1 == 1:
            data[num4] = int(data[num2]) + int(data[num3])

        elif num1 == 2:
            data[num4] = int(data[num2]) * int(data[num3])

        else:
            print('not a valid opcode')
            break

    #    if int(data[num2]) + int(data[num3]) == 19690720:
    #        print(100*num2 + num3)
    #
    #    if int(data[num2]) * int(data[num3]) == 19690720:
    #        print(100*num2 + num3)
    #
        location += 4 

    #print(data)

    print('data[0]: ')
    print(data[0])
    print('first:')
    print(first)
    print('second:')
    print(second)

    
    if data[0] == 19690720:
        print('valid\n')
        print(100* first + second)
        break
    elif first == 100:
        first = 0
        second += 1
    else:
        first += 1

    location = 0
    data = copy.deepcopy(curData)
    #print(data)
    #print(first)
    #print(second)


print(data)
