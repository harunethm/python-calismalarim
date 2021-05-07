def nearestPolindrom(num):
    for i in range(num):
        if(str(num - i) == ''.join(reversed(str(num - i)))):
            return num - i
        elif(str(num + i) == ''.join(reversed(str(num + i)))):
            return num + i

testNumber = 1228
print(nearestPolindrom(testNumber))