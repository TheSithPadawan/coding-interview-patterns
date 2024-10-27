"""
Question: https://leetcode.com/playground/RQBPRVsn
"""

from collections import defaultdict
from math import ceil
from sortedcontainers import SortedDict

import heapq

class Task:
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol

    # Define the custom comparator
    def __lt__(self, other):
        # Custom comparison: lower priority values come first
        if self.price == other.price:
            return self.symbol > other.symbol
        return self.price < other.price
    
    def __eq__(self, value: object) -> bool:
        return self.price == value.price and self.symbol == value.symbol
    
    def __hash__(self) -> int:
        return hash('.'.join([str(self.price), str(self.symbol)]))
    
    def __str__(self) -> str:
        return f'({self.price},{self.symbol})'

def trade_stocks(stocks):
    money = 1000
    portfolio = defaultdict(int)
    for tx in stocks:
        time, symbol, t, quantity, amount = tx
        if t == 'B':
            portfolio[symbol] += int(quantity)
            money -= int(amount) * int(quantity)
        else:
            portfolio[symbol] -= int(quantity)
            money += int(amount) * int(quantity)
    output = [['CASH', money]]
    for symbol, quantity in portfolio.items():
        output.append([symbol, str(quantity)])
    return output

def margin_call(portfolio, stocks):
    print('margincall begin portfolio', portfolio)
    deficit = int(portfolio[0][1])
    if deficit >= 0:
        return portfolio
    deficit = abs(deficit)
    sd = SortedDict()
    last_prices = defaultdict(int)
    for stock in stocks:
        time, symbol, t, quantity, price = stock
        last_prices[symbol] = int(price)

    for i in range(1, len(portfolio)):
        symbol, shares = portfolio[i]
        sd[Task(last_prices[symbol], symbol)] = int(shares)

    # start margin call
    while deficit > 0:
        if len(sd) == 0:
            print('not possible for margin call')
            return [['CASH', str(-deficit)]]
        task = list(sd.keys())[-1]
        count = sd[task]
        if deficit % task.price != 0:
            needed = ceil(deficit / task.price)
        else:
            needed = deficit // task.price
        if needed >= count:
            # sell all for this symbol
            deficit -= count * task.price 
            sd.pop(task)
        else:
            deficit -= needed * task.price  
            sd[task] -= needed
    print('deficit at the end', deficit) 
    output = [['CASH', str(-deficit)]]
    for k, v in sd.items():
        output.append([k.symbol, str(v)])
    return output

def get_user_portfolio(stocks):
    # Q1: trade stocks 
    output = trade_stocks(stocks)
    # Q2: margin call
    output = margin_call(output, stocks)
    return output

def margin_call_with_collateral(portfolio, stocks):
    print('margincall begin portfolio', portfolio)
    deficit = int(portfolio[0][1])
    if deficit >= 0:
        return portfolio
    deficit = abs(deficit)
    sd = SortedDict()
    last_prices = defaultdict(int)
    for stock in stocks:
        time, symbol, t, quantity, price = stock
        last_prices[symbol] = int(price)

    reserved_stocks_symbol = []
    for i in range(1, len(portfolio)):
        symbol, shares = portfolio[i]
        # print(symbol, symbol[-1], symbol[-1] == 'O')
        sd[Task(last_prices[symbol], symbol)] = int(shares)
        if symbol[-1] == 'O':
            reserved_stocks_symbol.append((symbol[:-1], int(shares)))
    print('reserved_stocks_symbol', reserved_stocks_symbol)
    remains = dict()
    # updated possible margin call collaterals
    for reserved in reserved_stocks_symbol:
        symbol = reserved[0]
        withheld = reserved[1]
        sd[Task(last_prices[symbol], symbol)] = sd[Task(last_prices[symbol], symbol)] - withheld
        remains[Task(last_prices[symbol], symbol)] = withheld
        if sd[Task(last_prices[symbol], symbol)] == 0:
            sd.pop(Task(last_prices[symbol], symbol))
     # start margin call
    while deficit > 0:
        if len(sd) == 0:
            print('not possible for margin call')
            return [['CASH', str(-deficit)]]
        task = list(sd.keys())[-1]
        sell_special = False
        if task.symbol[-1] == 'O':
            sell_special = True
        count = sd[task]
        if deficit % task.price != 0:
            needed = ceil(deficit / task.price)
        else:
            needed = deficit // task.price
        if needed >= count:
            # sell all for this symbol
            deficit -= count * task.price 
            sd.pop(task)
            # free up collateral for sale
            if sell_special:
                collateral = task.symbol[:-1]
                sd[Task(last_prices[collateral], collateral)] += count
                remains[Task(last_prices[collateral], collateral)] -= count
                if remains[Task(last_prices[collateral], collateral)] == 0:
                    remains.pop(Task(last_prices[collateral], collateral))
        else:
            deficit -= needed * task.price  
            sd[task] -= needed
            if sell_special:
                collateral = task.symbol[:-1]
                sd[Task(last_prices[collateral], collateral)] += needed
                remains[Task(last_prices[collateral], collateral)] -= needed
                if remains[Task(last_prices[collateral], collateral)] == 0:
                    remains.pop(Task(last_prices[collateral], collateral))
    print('deficit at the end', deficit) 
    output = [['CASH', str(-deficit)]]
    for k, v in sd.items():
        output.append([k.symbol, str(v)])
    # adding back those collaterals 
    for k, v in remains.items():
        output.append([k.symbol, str(v)])
    return output


def get_user_portfolio_with_collateral(stocks):
    portfolio = trade_stocks(stocks)
    return margin_call_with_collateral(portfolio, stocks)


if __name__ == '__main__':
    """
    # Q1
    stocks = [["1", "AAPL", "B", "10", "10"], ["3", "GOOG", "B", "20", "5"], ["10", "AAPL", "S", "5", "15"]]
    print(trade_stocks(stocks))

    # Q2
    stocks = [
    ["1", "AAPL", "B", "5", "100"],
    ["2", "ABPL", "B", "5", "100"],
    ["3", "AAPL", "S", "2", "80"],
    ["4", "ABPL", "S", "2", "80"],
    ["5", "GOOG", "B", "15", "30"]
]   
    # print(trade_stocks(stocks))
    output = get_user_portfolio(stocks)
    print (output)

    # Q2 Test case 2
    stocks = [
    ["1", "AAPL", "B", "10", "100"],
    ["2", "AAPL", "S", "2", "80"],
    ["3", "GOOG", "B", "15", "20"]
]
    output = get_user_portfolio(stocks)
    print (output)

    # Q2 Test case 3
    stocks = [
    ["1", "AAPL", "B", "5", "100"],
    ["2", "ABPL", "B", "5", "100"],
    ["3", "AAPL", "S", "2", "80"],
    ["4", "ABPL", "S", "2", "120"],
    ["5", "GOOG", "B", "15", "30"]
]
    output = get_user_portfolio(stocks)
    print (output)

    # Q2 Test case 4
    stocks = [
        ["1", "AAPL", "B", "5", "100"],
        ["2", "ABPL", "B", "5", "100"],
        ["3", "AAPL", "S", "2", "80"],
        ["4", "ABPL", "S", "2", "120"],
        ["5", "GOOG", "B", "10", "80"]
    ]
    output = get_user_portfolio(stocks)
    print (output)
    """

    # Q3 Test case 1
    stocks = [
    ["1", "AAPL", "B", "5", "100"],
    ["2", "GOOG", "B", "5", "75"],
    ["3", "AAPLO", "B", "5", "50"]
    ]
    output = get_user_portfolio_with_collateral(stocks)
    print(output)

    # Q3 Test case 2
    stocks = [
    ["1", "AAPL", "B", "6", "50"],
    ["2", "GOOG", "B", "6", "50"],
    ["3", "AAPLO", "B", "5", "25"],
    ["4", "GOOG0", "B", "5", "25"],
    ["5", "TEST", "B", "250", "1"]
    ]
    output = get_user_portfolio_with_collateral(stocks)
    print(output)


