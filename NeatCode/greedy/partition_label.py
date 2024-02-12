class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        for i, char in enumerate(s):
            if char not in last:
                last[char] = i
            else:
                last[char] = max(i, last[char])
        result = []
        l = 0
        while l < len(s):
            r = last[s[l]]
            # print('checking s[l] = ', s[l])
            i = l
            while i < r:
                r = max(last[s[i]], r)
                i += 1
            result.append(r - l + 1)
            l = r + 1
        return result
# O(n) solution, the idea is to check if current char in the window can extend
# the right edge of the window or not. record answer when it cannot

# NC solution. A better one. The idea is to update the end when possible
# record answer when j == r meaning all elements in the current window cannot surpass the end
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        for i, char in enumerate(s):
            last[char] = i

        result = []
        r, size = 0, 0
        j = 0
        while j < len(s):
            r = max(last[s[j]], r)
            size += 1

            if j == r:
                result.append(size)
                size = 0
            j += 1
        return result

# lc link: https://leetcode.com/problems/partition-labels/ 
