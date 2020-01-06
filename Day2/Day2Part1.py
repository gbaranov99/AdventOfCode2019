file = open('Day2File.txt', 'r')
data = file.read()
data = data.strip('\n')
data = data.split(',')

data[1] = 12
data[2] = 2

print(data)
location = 0
length = len(data)

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

    location += 4 

print(data)
