class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        streak = 0
        maxStreak = 0
        for i, n in enumerate(nums):
            if n == 1:
                streak += 1

            if streak > maxStreak:
                maxStreak = streak

            if n==0:
                streak = 0

        return maxStreak