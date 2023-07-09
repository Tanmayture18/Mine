# Python program to find power of the using recursion

def power(base,exp):
    
    # Unintentional case
    
    assert exp>=0 and int(exp)==exp,'Error'
    
    
    
    # Base case
    if exp==0:
        return 1
    elif exp==1:
        return base
    
    
    
    else:
        
    # Recursive case
        return base*power(base,exp-1)
        
print(power(2,2))        