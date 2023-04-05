
# Bubble Sort   (We repeatdly compare each pairs in array and swap them if they are in wrong order)

def bubble(arr):   #O(N^^2)
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubble([5,1,2,4,0,6]))    