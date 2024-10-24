# Link to question: https://leetcode.com/playground/D8HmPNdG
# https://leetcode.com/discuss/interview-question/625536/Robinhood-or-Phone-or-Portfolio-Value-Optimization

# returns maximum achievable value
# version 1: allows fractional shares, for this question we can solve using greedy algs
def solve(portfolio, M, N): 
    arr = []
    for i in range(N):
        base, expected, amount = portfolio[i]
        arr.append((expected/base, base, expected, amount))
    arr.sort(reverse=True)
    money = 0
    i = 0
    while M and i < len(arr):
        num_shares = min(M / arr[i][1], arr[i][-1])
        M -= num_shares * arr[i][1]
        money += num_shares * arr[i][2]
        i += 1
    return money

# version 2: do not allow fractional shares use memoization
# max_revenue(i, amount) = amount when i == n
# max(max_revenue(i - 1, amount - count * b_val) + count * (s_val - b_val) for count in range(A[i]) such that amount - count * b_val >= 0)
def solve2(portfolio, M, N):
    cache = dict()

    def memo(i, amount):
        # base case: cash at hand
        if i == 0:
            return amount
        if (i, amount) in cache:
            return cache[(i, amount)]
        base, expected, count = portfolio[i-1]
        best = 0
        for j in range(count):
            if base * j > amount:
                break
            best = max(memo(i-1, amount - base * j) + j * expected, best)
        cache[(i, amount)] = best
        return best
    
    return memo(N, M)

if __name__ == '__main__':
    portfolio = [[15, 45, 3], [40, 50, 3], [25, 35, 3], [30, 25, 4]]
    M, N = 140, 4
    print(solve(portfolio, M, N))

    portfolio = [[15, 30, 3], [20, 45, 3]]
    M, N = 30, 1
    print(solve2(portfolio, M, N))
