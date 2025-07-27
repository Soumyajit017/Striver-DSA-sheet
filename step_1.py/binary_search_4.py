#Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.
#If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

##time complexity: O(log n), space complexity: O(1)

def insert_index(arr, target):
    left,right=0,len(arr)-1
    while left <=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left

arr=list(map(int,input("enter the sorted array:").split()))
target=int(input("enter the target number:"))

print("index of", target, "is at the index:",insert_index(arr,target))

