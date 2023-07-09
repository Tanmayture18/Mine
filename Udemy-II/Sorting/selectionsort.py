# Selection sort  O(N^^2)      (WE repeatedly find minimum element and move it to sorted part of array)

def selection(arr):
    
    for i in range(len(arr)):
        minm=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minm]:
                minm=j
        arr[i],arr[minm]=arr[minm],arr[i]
    return arr
    
print(selection([5,2,6,7,1,0]))    