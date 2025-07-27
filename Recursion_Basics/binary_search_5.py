# Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
# The floor of x is the largest element in the array which is smaller than or equal to x.
# The ceiling of x is the smallest element in the array greater than or equal to x.

def floor_and_ceiling(arr,x):
    left,right =0,len(arr)-1
    
    floor,ceiling= None,None

    while left<=right:

        mid=(left+right)//2

        if arr[mid]==x:
            return mid,mid
        elif arr[mid]<x:
            floor=mid
            left=mid+1
        else:
            ceiling=mid
            right=mid-1
    return floor,ceiling

__name__="__main__"

arr=[2,3,4,5,6,7,8,9,10]
x=4

print(floor_and_ceiling(arr,x))