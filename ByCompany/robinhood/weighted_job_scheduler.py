# https://www.geeksforgeeks.org/weighted-job-scheduling/

"""
DP subproblem: maximum profit considering i jobs
Decision Tree: consider current job, do not take current job
profit(i) = max(profit(i-1), profit(j) + current profit) where j < i and j is the largest
index that does not conflict with job i
"""
def get_max_profits(jobs):
    jobs.sort(key=lambda x: x[1])
    dp = dict()

    def memo(job_num):
        # base case
        if job_num == 1:
            return jobs[0][-1]
        if job_num < 1:
            return 0
        if job_num in dp:
            return dp[job_num]
        dp[job_num] = 0
        # get last non conflicted jobs in linear scan O(n) time, can be optimized to O(log n) using binary search
        last_job_num = -1
        for j in range(job_num, 0, -1):
            if not is_conflict(jobs[j-1], jobs[job_num-1]):
                last_job_num = j
                break
        if last_job_num != -1:
            dp[job_num] = max(memo(job_num-1), memo(last_job_num) + jobs[job_num-1][-1])
        else:
            dp[job_num] = max(memo(job_num -1), jobs[job_num-1][-1])
        print('max profit considering job_num:', job_num, 'is', dp[job_num])
        return dp[job_num]        

    return memo(len(jobs))

def is_conflict(j1, j2):
    return False if j1[1] <= j2[0] else True

if __name__ == '__main__':
    jobs = [[1, 2, 50], [3, 5, 20], [6, 19, 100], [2, 100, 200]]
    # returns 250
    print(get_max_profits(jobs))