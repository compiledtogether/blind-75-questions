# https://leetcode.com/problems/sqrtx

def mySqrt(x: int) -> int:
        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left+right)//2

            midSquared = mid * mid

            if midSquared > x:
                right = mid - 1
            elif midSquared < x: 
                left = mid + 1
                result = mid
            else:
                return mid
        return result

# Test Case

x = 8
output = 2

print(mySqrt(x) == output)