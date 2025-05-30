n = int(input('tell the number upto which you want to find the sum: '))
a=0

for i in range(1,n+1):
    a+=i

print(f'The sum of numbers from 1 to {n} is {a}')
