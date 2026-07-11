#  Writing Fibonacci Series

fib =[0,1]

n= int(input("Enter the range to get fibnoacci series:"))

for i in range(n):
    fib.append(fib[-1] + fib[-2])
    
print(','.join(str(e) for e in fib))