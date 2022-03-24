"""
lc 243, with exception that two words can be the same
"""
from typing import List

def shortestDistance(wordsDict: List[str], word1: str, word2: str) -> int:
        mindist = 2**31 - 1
        word1_last_seen, word2_last_seen = -1, -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                if word2_last_seen != -1:
                    mindist = min(mindist, i - word2_last_seen)
                word1_last_seen = i
            if word == word2:
                if word1_last_seen != -1 and word1_last_seen != i:
                    mindist = min(mindist, i - word1_last_seen)
                word2_last_seen = i
        return mindist


# output 3, not 0
print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes'))