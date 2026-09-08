class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        distinct = 0
        charSet = {}
        for r in range(len(s)):
            charSet[s[r]] = charSet.get(s[r], 0) + 1
            ## agar charSet mein value hai toh fetch that otherwise 0 then add 1 to it
            while len(charSet) > k:
                charSet[s[l]] -= 1
                if charSet[s[l]] == 0:
                    del charSet[s[l]]
                l += 1
            distinct = max(distinct, r - l + 1)
        return distinct