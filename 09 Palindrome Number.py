# Given an integer x, return true if x is palindrome integer.
#
#  An integer is a palindrome when it reads the same backward as forward.
#
#
#  For example, 121 is a palindrome while 123 is not.
#
#
#
#  Example 1:
#
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
#  Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
#  Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
#
#  Constraints:
#
#
#  -2³¹ <= x <= 2³¹ - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
#
#  Related Topics Math 👍 6708 👎 2250


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False  # If negative, false

        divisor = 1
        while x >= 10 * divisor:
            divisor *= 10

        while x:
            if x % 10 != x // divisor:
                return False

            # Takes off first, last digit of x
            x = (x % divisor) // 10

            divisor = divisor / 100

        return True
# leetcode submit region end(Prohibit modification and deletion)
