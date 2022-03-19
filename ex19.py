
timeA = int(input())
timeB = int(input())

if timeA >= 25 and timeB <= timeA - 2:
    print('S')
elif timeB >= 25 and timeA <= timeB - 2:
    print('S')
else:
    print('N')


