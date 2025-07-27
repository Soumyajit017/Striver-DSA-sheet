#fibonacci series: naive approach

def fibonacci(n):
    fib = [0] * (n + 1) #creaye an array to store fibonacci numbers

    if n >= 1:
        fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i - 1] + fib[i - 2]   
    return fib[i]
print(fibonacci(8))


#time complexity: O(n)
#space complexity: O(n) due to the array used to store the Fibonacci numbers

#now space optimized approach
#using two variables to store the last two Fibonacci numbers

def fibonacci_space_optimized(n):
    if n<=1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
print(fibonacci_space_optimized(8)) 

#time complexity: O(n)
#space complexity: O(1) due to the use of only two variables

#recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(8))
#time complexity: O(2^n) due to the exponential growth of recursive calls
#space complexity: O(n) due to the recursive stack space