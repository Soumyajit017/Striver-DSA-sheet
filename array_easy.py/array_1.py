# finding out the largest element of an array
# brute force approach: using linear search
# time complexity: O(n), space complexity: O(1)

def largest_element(arr):
    max_element = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element

arr=list(map(int,input("enter the array elements separated by space:").split()))
print("the largest element in the array is:", largest_element(arr))

# better approach: using built-in max function
# time complexity: O(n), space complexity: O(1)
def largest(arr):
    return max(arr)

arr= list(map(int,input("enter the array elements separated by space:").split()))
print("the largest element in the array is:", largest(arr))


# #most optimal approach: sorting the array and returning the last element
# #time complexity: O(n log n), space complexity: O(1)

def largest_sorted(arr):
    arr.sort()
    return arr[-1]
#or apply any other sorting algorithm like quicksort, mergesort, etc.

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
print("The largest element in the array is:", largest_sorted(arr))

#using recursion to find the largest element
#time complexity: O(n), space complexity: O(n)

def recursive_largest(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1], recursive_largest(arr, n-1))

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
n = len(arr)
print("The largest element in the array is:", recursive_largest(arr, n))