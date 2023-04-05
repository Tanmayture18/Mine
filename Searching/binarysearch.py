# Binary search    O(logN)

def binarysearch(arr,target):

    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if target<arr[mid]:
            high=mid-1 
        
        elif target>arr[mid]:
            low=mid+1
         
        else:
            return mid
    return -1    

print(binarysearch([10,20,30,40,50],40))
print(binarysearch([10,20,30,40,50],100))


