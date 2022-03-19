
a=int(input())
b=input()
c=int(input())
if(b)=='%':
    print(a%c)
elif(b)=='/':
    print('{:.1f}'.format(a/c))
else:
    print(a//c)
