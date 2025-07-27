#factorial of a number: iterative method

def fact_ite(n,fact=1):

    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            fact*=i
        return fact
print(fact_ite(5)) 

#factorial of a number: recursive method

def recur(n):
    if n==0:
        return 1
    else:
        return n * recur(n-1)
    
print(recur(5))