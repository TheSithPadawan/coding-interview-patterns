# lc 282. expression add operator
# lc link: https://leetcode.com/problems/expression-add-operators/
# The issue with this problem is * operator
"""
For example:
1+2*3, if the next operation is (*4)
current evaluation result = 7
to get the next correct result, we need to back track the entire expression 2*3
new result = curr result - prev result + prev result * current number < this is the formula that we should use >
Thus keep track of state: current result, previous result, current index at num, current expression
"""
def addOperators(num, target):
    result = list()
    def dfs(target, index, exp, num, curres, prevres):

        if curres == target and index == len(num):
            result.append(exp)
            return

        for i in range(index + 1, len(num) + 1):
            curnum = num[index: i]
            if len(curnum) > 1 and curnum.startswith('0'):
                break
            curnum = int(curnum)
            # dfs for + / - / *
            if exp:
                # dfs for + 
                dfs(target, i, exp + '+' + str(curnum), num, curres + curnum, curnum)
                # dfs for - 
                dfs(target, i, exp + '-' + str(curnum), num, curres - curnum, -curnum)
                # dfs for * 2 * 
                dfs(target, i, exp + '*' + str(curnum), num, curres - prevres + prevres * curnum, prevres * curnum)
            else: # initial configuration
                dfs(target, i, str(curnum), num, curnum, curnum)


    dfs(target, 0, "", num, 0, 0)
    return result