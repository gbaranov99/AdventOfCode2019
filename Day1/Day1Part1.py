file = open('Day1File.txt', 'r')

output = 0;

for line in file:
    temp = int(line)
    temp = int((temp/3)) -2
    output += temp

print(output)
