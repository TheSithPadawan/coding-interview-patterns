"""
lc link: https://leetcode.com/problems/accounts-merge/

union find solution
time complexity: O(nk log nk) n = # of accounts; k = avg # of emails
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = py
        
        # assign emails to ids
        email_to_ids = defaultdict(list)
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                email_to_ids[email].append(i)
        
        # perform merge of emails
        for ids in email_to_ids.values():
            for id in ids[1:]:
                union(ids[0], id)
        
        # merged acct 
        merged_acct = defaultdict(set)
        for i in range(len(accounts)):
            merged_acct[find(i)].update(accounts[i][1:])
        
        # output
        results = []
        for k, v in merged_acct.items():
            name = accounts[k][0]
            sorted_emails = sorted(v)
            results.append([name] + sorted_emails)
        return results