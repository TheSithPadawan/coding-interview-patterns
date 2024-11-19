"""
Question link: https://leetcode.com/discuss/interview-question/3158526/Offset-Ordering

Algorithm:
O(n) space, O(n) algorithm
[2, 1, 0, 5, 4]
we can only update committed offset if the processing offset is current highest commit + 1
result = [-1, -1, 2, -1, -1]
"""

def commit_offset(offsets: list[int]) -> list[int]:
    highest_offset = -1
    output = []
    uncommits = set()
    for offset in offsets:
        uncommits.add(offset)
        if offset == highest_offset + 1:
            while highest_offset + 1 in uncommits:
                uncommits.remove(highest_offset + 1)
                highest_offset += 1
            output.append(highest_offset)
        else:
            output.append(-1)
    return output


"""
Algorithm: 
O(1) space: result use tuple (-1, T/F)
"""
def commit_offset_2(offsets: list[int]) -> list[int]:
    output = []
    # to store offset when offsets[offset] = 0. otherwise it will be -offsets[offset]
    visit_num = None
    highest = -1
    # for any value >= len(output), it cannot be committed, just skip
    for i in range(len(offsets)):
        offset = abs(offsets[i])
        if offset >= len(offsets):
            output.append(-1)
            continue
        else:
            if offset == highest + 1:
                # add current one to seen
                offsets[offset] *= -1
                if offsets[offset] == 0:
                    visit_num = offset
                while highest + 1 < len(offsets) and (offsets[highest + 1] < 0 or visit_num == highest + 1):
                    highest += 1
                output.append(highest)
            else:
                offsets[offset] *= -1
                if offsets[offset] == 0:
                    visit_num = offset
                output.append(-1)
    return output

if __name__ == '__main__':
    # test case 1
    offsets = [2, 1, 0, 5, 4]
    print(commit_offset(offsets))
    print('testing for O(1) solution')
    print(commit_offset_2(offsets))
    print()
    # test case 2
    offsets = [0, 1, 2, 3]
    print(commit_offset(offsets))
    print('testing for O(1) solution')
    print(commit_offset_2(offsets))
    print()
    # # test case 3
    offsets = [3, 2, 1, 0]
    print(commit_offset(offsets))
    print('testing for O(1) solution')
    print(commit_offset_2(offsets))