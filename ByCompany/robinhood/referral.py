# referral count
# question: https://leetcode.com/discuss/interview-question/5047205/Robinhood-Phonescreen-or-L4


from collections import defaultdict


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
    # sorting for count
    count_list = [(val, key) for key, val in count.items()]
    count_list.sort(reverse=True)
    result = []
    for i in range(3):
        result.append((count_list[i][1], count_list[i][0]))
    return result

if __name__ == '__main__':
    rh_users = ['A', 'B', 'C']
    new_users = ['B', 'C', 'D']
    print(solve(rh_users, new_users))