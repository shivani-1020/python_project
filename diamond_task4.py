from os import system
system('cls')
print('Enter a number of  row:\n')
n = input() #5
n = int(n)

for i in range(1,n):
    print(' '*(n-i), end='')
    print('*'*i+'*'*(i-1))

for i in range(n,0, -1):
    print(' '*(n-i), end='')
    print('*'*i+'*'*(i-1))
