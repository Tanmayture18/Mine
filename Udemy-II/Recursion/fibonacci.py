# Fibonacci series

def fibonacci(n):

    # step1 

    assert n>=0 and int(n)==n,'Invalid'

    
    # step 2
    if n in [0,1]:
        return n
    
    
    
    else:
    # step1 
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input())
print(fibonacci(n))

# finding fibonacci series upto nth term

l1=[0,1]

for i in range(2,n):
    l1.append(fibonacci(i))

print(l1)