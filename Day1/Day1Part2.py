file = open('Day1File.txt', 'r')

output = 0;

for line in file:
    temp = int(line)
    temp = int((temp/3)) -2

    while temp > 0:
        output += temp
        temp = int((temp/3)) -2

print(output)
