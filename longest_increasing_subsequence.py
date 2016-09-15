class Solution(object):


    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        bestFollowing = [1 for _ in range(len(nums))]

        for i in reversed(range(len(nums))):
            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
                    best = max(best, bestFollowing[j] + 1)
            bestFollowing[i] = best
            longest = max(longest, best)

        print(bestFollowing)
        return longest


s = Solution()

test = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(test))


