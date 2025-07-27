#binary search algorithm using iterative approach
#time complexity is O(log n) and space complexity is O(1)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(map(int, input("Enter the sorted array elements separated by space: ").split()))
target = int(input("Enter the target element to search: "))

print("The element is found at index:", binary_search(arr, target))

#binary seach algorithum using recursive approach only 
#time complexity is O(log n) and space complexity is O(n)

def binary (arr, target,left,right):
    if left <= right:
        mid= (left + right) //2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary(arr,target,mid+1,right)
        else:
            return binary(arr,target,left,mid-1)
    return -1

arr= list(map(int,input("enter the sorted array elements separated by space:").split()))

target=int(input("enter the target element to search:"))

print("the element is found at the index:", binary(arr,target,0,len(arr)-1))


    