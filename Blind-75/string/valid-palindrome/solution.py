# https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s: str) -> bool:
    # left, right = 0, len(s) - 1

    # while left < right:
    #     while(left<right and not s[left].isalnum()):
    #         left +=1
    #     while(left<right and not s[right].isalnum()):
    #         right -= 1
        
    #     if s[left].lower() != s[right].lower():
    #         return False

    #     left += 1
    #     right -= 1

    # return True
    clean_string = ''.join([char for char in s if char.isalnum()]).lower()

    reversed_string = clean_string[::-1]

    return True if clean_string == reversed_string else False

# Test Case:

s = "A man, a plan, a canal: Panama"
output = True

print(isPalindrome(s) == output)