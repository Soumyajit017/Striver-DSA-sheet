#Method name: palindrome
#Description: This function checks if a given string is a palindrome using recursion.
# Time complexity: O(n)
# Space complexity: O(n): due to the recursive stack space

def palindrome(s):
    n = len(s)
    if n <= 1:
        return True
    if s[0] != s[n - 1]:
        return False
    return palindrome(s[1:n - 1])

print(palindrome("madam"))  # True
print(palindrome("hello"))  # False

#another way to do it: using two pointers

def palindrome(s,left,right):
    if left==right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s,left+1,right-1)

print(palindrome("madam",0,4)) # True
print(palindrome("hello", 0, 4))  # False