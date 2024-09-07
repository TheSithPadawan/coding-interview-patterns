# lc link: https://leetcode.com/problems/stickers-to-spell-word/

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        counters = []
        for sticker in stickers:
            counters.append(Counter(sticker))
        
        dp = dict()
        def memo(t, sticker):
            if t in dp:
                return dp[t]
            if not t:
                return 0

            res = 1 if sticker else 0
            remt = ''
            for ch in t:
                if ch in sticker and sticker[ch] > 0:
                    sticker[ch] -= 1
                else:
                    remt += ch
            # continue with dfs
            if remt:
                used = float("inf")
                for s in counters:
                    if remt[0] not in s:
                        continue
                    used = min(memo(remt, s.copy()), used)
                dp[remt] = used
                res += used
            return res
        
        result = memo(target, {})
        return -1 if result == float("inf") else result
