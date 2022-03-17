"""
lc link: https://leetcode.com/problems/interval-list-intersections
Solution using merge 2 array template
whoever's end time is earlier, advances that pointer.
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            # has overlap, first list start < second list start
            if firstList[i][0] <= secondList[j][0] and firstList[i][1] >= secondList[j][0]:
                result.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            # has overlap, second list start < first list start
            elif secondList[j][0] <= firstList[i][0] and secondList[j][1] >= firstList[i][0]:
                result.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result