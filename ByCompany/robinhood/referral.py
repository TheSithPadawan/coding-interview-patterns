# referral count
# question: https://leetcode.com/discuss/interview-question/5047205/Robinhood-Phonescreen-or-L4


from collections import defaultdict
import heapq


def solve(rh_users, new_users):
    graph = defaultdict(list)
    for i in range(len(rh_users)):
        start, end = rh_users[i], new_users[i]
        # invalid due to existing users cannot be referred again
        if end in graph:
            continue
        graph[start].append(end)
    
    count = dict()
    visit = set() 
    def dfs(node):
        cnt = 0
        if node in visit:
            count[node] = cnt
            return cnt
        visit.add(node)
        for nei in graph[node]:
            cnt += dfs(nei) + 1
        count[node] = cnt
        return cnt

    for user in rh_users:
        if user in visit:
            continue
        dfs(user)
    minheap = []
    """
    heap size = 3 
    """
    for key, val in count.items():
        heapq.heappush(minheap, (val, key))
        if len(minheap) > 3:
            heapq.heappop(minheap)
    # from big to small
    result = []
    while minheap:
        result.append(heapq.heappop(minheap))
    return result[::-1]

if __name__ == '__main__':
    rh_users = ['A', 'B', 'C']
    new_users = ['B', 'C', 'D']
    print(solve(rh_users, new_users))