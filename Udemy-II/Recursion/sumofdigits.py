# Write a program to find sum of its all digits using recursion

def sumpositive(n):
    # Unintentional case
    assert n>=0 and int(n)==n,'Error'

    # base case
    if n==0:
        return 0
    else:
        
        # Recursive case
        return int(n%10) + int(sumpositive(n/10))
        
print(sumpositive(int(input())))        
    
    