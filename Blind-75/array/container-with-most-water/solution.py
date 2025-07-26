# https://leetcode.com/problems/container-with-most-water/

def maxArea(height: list) -> int:
#     # BRUTE FORCE

#     result = 0

#     for left in range(len(height)):
#         for right in range(left+1, len(height)):
#             area = (right-left) * min(height[left], height[right])
#             result = max(result, area)

#     return result


# # Time Complexity: O(n2)
# # Space Complexity: O(1)

    # Two Pointer Method

    result = 0

    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(result, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result

# Time Complexity: O(n)
# Space Complexity: O(1)

height =  [1,8,6,2,5,4,8,3,7]
Output = 49

print(maxArea(height) == Output)