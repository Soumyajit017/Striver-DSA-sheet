#finding the upper bound of a number in a sorted array
#brute force appraoch: using linear search
#time complexity: O(n), space complexity: O(1)

def upper_bound(arr,target):
    for i in range(len(arr)):
        if arr[i] > target:
            return i
    return len(arr)

arr=list(map(int,input("enter the sorted array:").split()))
target=int(input("enter the target number:"))

print("upper bound of",target,"is at the index:-",upper_bound(arr,target))

#upper bound is the index of the first element that is greater than the target number
#upper bound finding using binary search

def upper_binary(arr,target,left,right):
    while left<=right:
        mid=(left+right)//2
         
        if arr[mid]<= target:
            left=mid+1  
        else:
            right=mid-1
    return left

arr=list(map(int,input("enter the sorted array:").split()))
target=int(input("enter the target number:"))
print("upper bound of",target,"is at the index:-",upper_binary(arr,target,0,len(arr)-1))