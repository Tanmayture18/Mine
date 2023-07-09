# Program to find factorial

def factorial(n):


    # step 3 un intentional case
    assert n>=0 and int(n)==n,'Number must be postive integer only'

    # step 2 base case
    if n==0 or n==1:
        return 1


    
    else:
    # Step 1:recursive case
        return n*factorial(n-1)

print(factorial(int(input())))        