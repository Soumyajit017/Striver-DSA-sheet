#finding the lower bound of a number in a sorted array using binary search
#time complexity is O(log n) and space complexity is O(1)

#brute force approach: using linear search

def lower_bound(arr, target):
    for i in range(len(arr)):
        if arr[i] >= target:
            return i
    return -1

arr=list(map(int,input("enter the sorted array elements separated by space:").split()))

target=int(input("enter the target element to search:"))

print("the lower bound of the target element is at index:", lower_bound(arr,target))


#now using binary search algorithm to find the lower bound
#time complexity is O(log n) and space complexity is O(1)

def binary_search(arr, target):
    left,right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) //2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return left

arr = list(map(int, input("Enter the sorted array elements separated by space: ").split()))
target = int(input("Enter the target element to search: "))
print("The lower bound of the target element is at index:", binary_search(arr, target))