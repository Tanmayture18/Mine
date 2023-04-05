# Bucket Sort   Time complexity depends which sorting algorithm you are using
import math

def bucket(arr):
    n=len(arr)
    
    #1) Calculate number of buckets
    num_buckets=round(math.sqrt(n))
    
    #2)Create Buckets
    l1=[]
    for i in range(num_buckets):
        l1.append([])
    
    #3) Assign every element of array to correct bucket
    maxm=max(arr)
    for i in arr:
        index=math.ceil(i*num_buckets/maxm)
        l1[index-1].append(i)
    
    #4) Using alternate sorting algorithm
    for i in l1:
        i.sort()
    
    #5) Combining all buckets
    l3=[]
    for i in l1:
        for j in i:
            l3.append(j)
    return l3

print(bucket([9,8,7,6,5,4,3,2,1]))    
    
    
    