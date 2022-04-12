"""
top amazon question
lc link: https://leetcode.com/problems/analyze-user-website-visit-pattern/
"""

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # step 1: find out about the website that a person visited 
        # <user: [sites]>
        # step 2: process user's visit list, update frequency map <pattern, count>
        # step 3: sort pattern by count and output
        users = defaultdict(list)
        n = len(username)
        for i in range(n):
            users[username[i]].append((timestamp[i], website[i]))
        
        self.counter = defaultdict(int)
        self.strset = set()
        for _, v in users.items():
            self.process_user(v)
        maxscore = max(self.counter.values())
        ans = ''
        for k, v in self.counter.items():
            if v == maxscore:
                if ans == '':
                    ans = k
                elif k < ans:
                    ans = k
        return ans.split(' ')

    
    def process_user(self, sites):
        sites.sort(key=lambda x: x[0])
        n = len(sites)
        strs = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    pattern = ' '.join([sites[i][1], sites[j][1], sites[k][1]])
                    strs.add(pattern)
        for s in strs:
            self.counter[s] += 1