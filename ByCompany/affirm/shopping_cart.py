"""
[item1, item2, item2, item3]
[item2, item3, item4]
[item3, item4, item5]

output: 
item1: [item2, item3],
item2: [item3],
item3: [item2, item4],
item4: [item3],
item5: [item3, item4]
"""

from collections import Counter, defaultdict


def solve_1(carts):
    """
    O(N*M^2) solution brute force
    """
    result = defaultdict(lambda: defaultdict(int))
    for cart in carts:
        for i in range(len(cart)):
            for j in range(len(cart)):
                if i == j:
                    continue
                result[cart[i]][cart[j]] += 1
    max_result = dict()
    for item, values in result.items():
        max_cnt = 0
        max_result[item] = []
        # find out about the max cnt first
        # for other, cnt in values.items():
        #     max_cnt = max(max_cnt, cnt)
        # for other, cnt in values.items():
        #     if cnt == max_cnt:
        #         max_result[item].append(other)
        # a little optimization here, build max_cnt on the fly
        for other, cnt in values.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_result[item] = [other]
            elif cnt == max_cnt:
                max_result[item].append(other)
    return max_result



def solve_2_optimized(carts):
    """
    if we know the item count ahead of time
    can just update counts then aggregate the results
    O(N * max(N, M))
    """
    counts = defaultdict(Counter)
    for cart in carts: # O(N)
        item_count = Counter(cart) # O(N)
        for item in cart: # O(M)
            counts[item] += item_count
    result = defaultdict(list)
    for item, cnt in counts.items():
        max_cnt = 0
        for k, v in cnt.items():
            if k == item:
                continue
            if v == max_cnt:
                result[item].append(k)
            elif v > max_cnt:
                result[item] = [k]
                max_cnt = max(max_cnt, v)
    return result


if __name__ == '__main__':
    carts = [['item1', 'item2', 'item3'],
['item2', 'item3', 'item4'],
['item3', 'item4', 'item5']]
    print(solve_1(carts))
    print(solve_2_optimized(carts))