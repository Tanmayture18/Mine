# Python program to conert decimal to binary using recursion

def detobi(n):
     # unintentional case
    assert int(n)==n,'Error'
   
   
   # base case 
    if n==0:
        return 0
    
    else:
        # Recursive base
        return n%2 +10 * detobi(int(n/2))
        
print(detobi(13))        
    
    
   