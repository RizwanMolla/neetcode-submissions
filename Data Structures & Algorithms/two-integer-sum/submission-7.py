class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNum = {}

        for i, n in enumerate(nums):

            requiredNum = target-n

            if requiredNum in seenNum:
                return [seenNum[requiredNum], i]

            seenNum[n]= i 