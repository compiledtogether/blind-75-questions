# https://leetcode.com/problems/powx-n

def myPow(x: float, n: int) -> float:
    # Brute Force
    # result = 1
    # for i in range(n):
    #     result *= x

    # return result

    # Recursion
    def helper(x: float, n: int):

        if x == 0: return 0
        if n == 0: return 1

        res = helper(x, n//2)
        res = res * res

        return res * x if n % 2 else res
     
    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res

# Test Case

x = 2.000
n = 10

output = 1024.000

print(myPow(x,n) == output)