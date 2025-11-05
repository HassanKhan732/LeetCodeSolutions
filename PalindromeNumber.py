class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        converted_num1 = str(x)
        reversed_num = converted_num1[::-1]
        return converted_num1 == reversed_num
