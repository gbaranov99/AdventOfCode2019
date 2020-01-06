file = open('Day5Input.txt', 'r')
data = file.read()
data = data.strip('\n')
data = data.split(',')

location = 0
length = len(data)


#print(data)

while location < length: 
    code_string = str(data[location])
    code = int(code_string[-1])

    if len(code_string) == 2 and code_string == '99':
        break

    if code == 1 or code == 2 or code == 5 or code == 6 or code == 7 or code == 8:
        val1 = 0
        val2 = 0

        if len(code_string) < 3:
            val1 = int(data[int(data[location + 1])])
            val2 = int(data[int(data[location + 2])])
        elif len(code_string) == 3:
            if code_string[0] == 0:
                val1 = int(data[int(data[location + 1])])
            else:
                val1 = int(data[location + 1])
            val2 = int(data[int(data[location + 2])])
        else:
            #val1 = int(data[location + 1])
            #val2 = int(data[location + 2])
            if int(code_string[1]) == 0:
                val1 = int(data[int(data[location + 1])])
            else:
                val1 = int(data[location + 1])

            if int(code_string[0]) == 0:
                val2 = int(data[int(data[location + 2])])
            else:
                val2 = int(data[location + 2])


        if code == 1 or code == 2:
            store_to = int(data[location + 3])

            if code == 1:
                data[store_to] = val1 + val2

            if code == 2:
                data[store_to] = val1 * val2

            #print('Test: ')
            #print(data[store_to])
            #print(store_to)

            location += 4
        else:
            if code == 5:
                if val1 != 0:
                    location = val2
                else:
                    location += 3

            elif code == 6:
                if val1 == 0:
                    location = val2
                else:
                    location += 3

            elif code == 7:
                store_to = int(data[location + 3])
                if val1 < val2:
                    data[store_to] = 1
                else:
                    data[store_to] = 0
                location += 4

            elif code == 8:
                store_to = int(data[location + 3])
                if val1 == val2:
                    data[store_to] = 1
                else:
                    data[store_to] = 0
                location += 4


    elif code == 3 or code == 4:
        loc = int(data[location + 1])

        if code == 3:
            data[loc] = str(input())

        if code == 4:
            print('Code 4:')
            if len(code_string) < 3:
                print(data[loc])

            if len(code_string) == 3:
                if int(code_string[0]) == 1:
                    print(loc)
                else:
                    print(data[loc])


        location += 2

    else:
        print(location)
        print(code)
        raise ValueError('Not valid opCode')

#print(data)
