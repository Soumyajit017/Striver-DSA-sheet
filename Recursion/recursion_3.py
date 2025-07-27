# #print 1 to N # using recursion(backtracking)
# # This code prints numbers from 1 to N using recursion.

# def print_numbers(n):
#     if n <=0:
#         return # Base case: if n is less than or equal to 0, do nothing
#     print_numbers(n-1) # Recursive call with n-1
#     print(n) # Print the current number after the recursive call

# print_numbers(5) # Example usage, prints numbers from 1 to 5  

# #for forward recursion or tail recursion

def print_numbers_forward(n):
    if n<=0:
        return
    print(n)
    print_numbers_forward(n-1)

print_numbers_forward(5)
        