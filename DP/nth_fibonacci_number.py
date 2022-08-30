
# n =	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15    ...
# xn =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610   ...
def nthFibonacci_recursive(n):
    # Base condition
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    # Recursive logic
    result1 = nthFibonacci_recursive(n-1)
    result2 = nthFibonacci_recursive(n-2)
    
    return result1 + result2

def nthFibonacci_memorization(n, dp):
    # Base condition
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    if dp[n] != False:
        return dp[n]
    
    # Recursive logic
    if dp[n-1] == False:
        dp[n-1] = nthFibonacci_memorization(n-1, dp)
        
    if dp[n-2] == False:
        dp[n-2] = nthFibonacci_memorization(n-2, dp)
    
    dp[n] = dp[n-1] + dp[n-2]
    
    return dp[n]

def nthFibonacci_tabulation(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    dp = [False] * (n + 1)
    
    # Base conditions
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    start = 3
    # Iterative logic
    for current in range(start, n+1):
        dp[current] = dp[current-1] + dp[current-2]
    
    return dp[n]

n = 15
dp = [False] * (n + 1)
result = nthFibonacci_tabulation(n)
print(result)
    