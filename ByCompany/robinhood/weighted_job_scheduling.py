"""
https://www.geeksforgeeks.org/weighted-job-scheduling/
"""

def get_max_profit(jobs):
    """
    subset组合问题 dfs: O(2^n)
    use memoization: subproblem: max profit when job i is included O(n^2)
    profit(i): max profit considering first i jobs
    profit (i) = max(profit(i-1), profit(j) + current profit) for j < i, and j is not in conflict with i
    """
    # sort by job end time
    jobs.sort(key=lambda x: x[1])
    dp = dict()

    def memo(jobIndex):
        # base case 
        if jobIndex == 1:
            return jobs[0][-1]
        
        if jobIndex in dp:
            return dp[jobIndex]
        curr = jobs[jobIndex-1][-1]
        for i in range(jobIndex-1, -1, -1):
            # if has no conflict:
                result = memo()
                break
        dp[jobIndex] = max(curr + result, memo(jobIndex-1))
        return dp[jobIndex]

if __name__ == '__main__':
    # (start, end, profit)
    jobs = [[1, 2, 50], [3, 5, 20], [6, 19, 100], [2, 100, 200]]
    print(get_max_profit(jobs))