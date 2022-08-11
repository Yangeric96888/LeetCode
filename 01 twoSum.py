# twoSum - https://leetcode.com/problems/two-sum/submissions/


class Solution:
    def twoSum(self, nums, target: list[int]) -> list[int]:
        prevNum = {}
        for count, value in enumerate(nums):
            if (target - value) in prevNum:
                return [prevNum[target - value], count]

            prevNum[value] = count

        return
# leetcode submit region end(Prohibit modification and deletion)
