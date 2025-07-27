#Functional way:

def sum(n):
    if n<=0:
        return 0
    else:
        return n + sum(n-1)
    
print(sum(5))    

#parametric way:
def sum_parametric(n, acc=0):
    if n <= 0:
        return acc
    else:
        return sum_parametric(n - 1, acc + n)
    
print(sum_parametric(5))  # Example usage, prints sum of first 5 natural numbers (15)