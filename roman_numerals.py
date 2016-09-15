import sys
input = sys.argv[1]

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = None
        total = 0
        for cur in s:
            if prev is not None and val[cur] > val[prev]:
                total -= val[prev] * 2
            total += val[cur]
            prev = cur
        return total

s = Solution()
print(s.romanToInt(input))