#import math

file = open('Day3File.txt', 'r')
#file = open('Day3File.txt', 'r')
path1 = file.readline()
path2 = file.readline()

path1 = path1.strip('\n')
path1 = path1.split(',')

path2 = path2.strip('\n')
path2 = path2.split(',')

# Better way
# Create ranges for each step of path1 and path2
# Go through path2 ranges, for each one comparing the range to any 

curX = 0
curY = 0

range_path1 = []
range_path2 = []

distance1 = 0
for elem in path1:
    distance = int(elem[1:])
    newX = curX
    newY = curY

    if elem[0] == 'R':
        newX += distance
    if elem[0] == 'L':
        newX -= distance
    if elem[0] == 'D':
        newY -= distance
    if elem[0] == 'U':
        newY += distance
    
    range_path1.append([[curX, curY], [newX, newY], distance1])

    distance1 += distance
    curX = newX
    curY = newY


curX = 0
curY = 0

distance2 = 0
for elem in path2:
    distance = int(elem[1:])
    newX = curX
    newY = curY

    if elem[0] == 'R':
        newX += distance
    if elem[0] == 'L':
        newX -= distance
    if elem[0] == 'D':
        newY -= distance
    if elem[0] == 'U':
        newY += distance
    
    range_path2.append([[curX, curY], [newX, newY], distance2])

    distance2 += distance
    curX = newX
    curY = newY

#print(range_path1)
#print(range_path2)

intersections = []
for i in range_path2:
    for j in range_path1:
        if i[0][0] == i[1][0]:
            if j[0][1] == j[1][1]:
                if (j[0][0] <= i[0][0] <= j[1][0]) or (j[0][0] >= i[0][0] >= j[1][0]):
                    if (i[0][1] <= j[0][1] <= i[1][1]) or (i[0][1] >= j[0][1] >= i[1][1]):
                        y = i[0][0]
                        x = j[0][1]
                        #temp = i[2] + abs(i[1][1] - j[0][1])
                        #temp1 = j[2] + abs(j[1][0] - i[0][0])
                        temp = abs(j[0][1] - i[0][1])
                        print(i, j)
                        i[2] += temp
                        intersections.append(i[2])
                        #intersections.append([i[2], temp])
        else:
            if j[0][0] == j[1][0]:
                if (j[0][1] <= i[0][1] <= j[1][1]) or (j[0][1] >= i[0][1] >= j[1][1]):
                    if (i[0][0] <= j[0][0] <= i[1][0]) or (i[0][0] >= j[0][0] >= i[1][0]):
                        y = j[0][0]
                        x = i[0][1]
                        #temp = i[2] + abs(i[1][0] - j[0][0])
                        #temp1 = j[2] + abs(j[1][1] - i[0][1])
                        temp = abs(j[1][0] - i[0][0])
                        print(i, j)
                        i[2] += temp
                        intersections.append(i[2])
                        #intersections.append([i[2], j[2]])


intersections1 = []
for i in range_path1:
    for j in range_path2:
        if i[0][0] == i[1][0]:
            if j[0][1] == j[1][1]:
                if (j[0][0] <= i[0][0] <= j[1][0]) or (j[0][0] >= i[0][0] >= j[1][0]):
                    if (i[0][1] <= j[0][1] <= i[1][1]) or (i[0][1] >= j[0][1] >= i[1][1]):
                        y = i[0][0]
                        x = j[0][1]
                        #temp = i[2] + abs(i[1][1] - j[0][1])
                        #temp1 = j[2] + abs(j[1][0] - i[0][0])
                        temp = abs(j[0][1] - i[0][1])
                        print(i, j)
                        i[2] += temp
                        intersections1.append(i[2])
                        #intersections.append([i[2], temp])
        else:
            if j[0][0] == j[1][0]:
                if (j[0][1] <= i[0][1] <= j[1][1]) or (j[0][1] >= i[0][1] >= j[1][1]):
                    if (i[0][0] <= j[0][0] <= i[1][0]) or (i[0][0] >= j[0][0] >= i[1][0]):
                        y = j[0][0]
                        x = i[0][1]
                        #temp = i[2] + abs(i[1][0] - j[0][0])
                        #temp1 = j[2] + abs(j[1][1] - i[0][1])
                        temp = abs(j[1][0] - i[0][0])
                        print(i, j)
                        i[2] += temp
                        intersections1.append(i[2])
                        #intersections.append([i[2], j[2]])
print(intersections)
print(intersections1)

#newIntersections = []
#for i in intersections:
#    newIntersections.append(abs(i[0]) + abs(i[1]))
#
#newIntersections.sort()
#print(newIntersections)
