# -----------------------------------------
# METHOD 1: RECURSION
# -----------------------------------------

def fibonacci_recursion(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


# -----------------------------------------
# METHOD 2: MEMOIZATION
# -----------------------------------------

def fibonacci_memoization(n, memo=None):

    if memo is None:
        memo = {}

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = (
        fibonacci_memoization(n - 1, memo)
        + fibonacci_memoization(n - 2, memo)
    )

    return memo[n]


# -----------------------------------------
# METHOD 3: TABULATION
# -----------------------------------------

def fibonacci_tabulation(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

try:
    n = int(input("Enter the value of n: "))

    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print("Fibonacci using Recursion:", fibonacci_recursion(n))
        print("Fibonacci using Memoization:", fibonacci_memoization(n))
        print("Fibonacci using Tabulation:", fibonacci_tabulation(n))

except ValueError:
    print("Please enter a valid integer.")
