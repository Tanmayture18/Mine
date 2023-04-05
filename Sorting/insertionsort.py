# Insertion sort  (Divide array into two parts ,Take first element from unsroted array and find its correct position in sorted array ,repeat untill array is empty)

def insertion(arr):    #O(N^^2)

    for i in range(len(arr)):
        curr=arr[i]

        j=i-1
        while j>=0 and curr<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=curr

    return arr

print(insertion([5,2,1,4,3]))       
