# #reversing an array: brute force approach:time complexity: O(n)
# Space complexity: O(n)

def reverse_array(arr):
    n=len(arr)
    ans= [0]*n
    for i in range(n):
        ans[i]=arr[n-1-i]
    return ans

print(reverse_array([1,2,3,4,5]))

#brute force approach: space optimized
#using the same array to store the reversed array using two pointers
## Time complexity: O(n)
# Space complexity: O(1)
def reverse_array(arr,n):
    left,right=0,n-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

print(reverse_array([1,2,3,4,5],5))

#recursive approach to reverse an array 
# Time complexity: O(n)
# Space complexity: O(n): # because of the recursive stack space

def reverse_array(arr,left,right):
    if left>=right:
        return arr
    arr[left],arr[right]=arr[right],arr[left]

    return reverse_array(arr,left+1,right-1)

print(reverse_array([1,2,3,4,5],0,4))

#slicing approach to reverse an array
# Time complexity: O(n)
# Space complexity: O(n): # because a new array is created
# This approach is simple and elegant, but it creates a new array, which may not be ideal for large arrays or memory-constrained environments.

def reverse_array(arr):
    return arr[::-1]

print(reverse_array([1,2,3,4,5]))