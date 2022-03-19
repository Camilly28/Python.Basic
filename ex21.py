
#Truco
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a>b)and(a>c)and(a>d):
  print(a)
elif(b>a)and(b>c)and(b>d):
  print(b)
elif(c>a)and(c>b)and(c>d):
  print(c)
elif(d>a)and(d>b)and(d>c):
  print(d)
else:
  print('empate')

