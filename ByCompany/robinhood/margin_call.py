# https://leetcode.com/playground/RQBPRVsn

from collections import defaultdict
from math import ceil
from sortedcontainers import SortedList

class Stock:
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol

    def __eq__(self, value: object) -> bool:
        return self.price == value.price and self.symbol == value.symbol
    
    def __lt__(self, other: object) -> bool:
        if self.price == other.price:
            return self.symbol < other.symbol
        return self.price > other.price
    
    def __hash__(self) -> int:
        return hash('.'.join([str(self.price), str(self.symbol)]))

def trade_stock(tx_type, portfolio, ticker, quantity, price, cash):
    if tx_type == 'B':
        portfolio[ticker] += quantity
        cash -= price * quantity
    else:
        portfolio[ticker] -= quantity
        cash += price * quantity
    return cash

# question 1
def get_user_portfolio(trades):
    cash = 1000
    portfolio = defaultdict(int)
    result = []
    for trade in trades:
        _, ticker, tx_type, quantity, price = trade
        quantity = int(quantity)
        price = int(price)
        cash = trade_stock(tx_type, portfolio, ticker, quantity, price, cash)
        
    result.append(['CASH', cash])
    for k, v in portfolio.items():
        result.append([k, str(v)])
    return result

# question 2: margin call
def get_user_portfolio_with_margin_call(trades):
    portfolio = defaultdict(int)
    last_traded_price = dict()
    cash = 1000
    result = []
    for trade in trades:
        _, ticker, tx_type, quantity, price = trade
        quantity = int(quantity)
        price = int(price)
        # trade stock
        cash = trade_stock(tx_type, portfolio, ticker, quantity, price, cash)
        # update last trade price
        last_traded_price[ticker] = price
        cash = margin_call(cash, tx_type, portfolio, last_traded_price)
    result.append(['CASH', cash])
    for k, v in portfolio.items():
        result.append([k, str(v)])
  
    return result 

# question 3: margin call with collateral 
def get_user_portfolio_with_margin_call_collateral(trades):
    portfolio = defaultdict(int)
    last_traded_price = dict()
    cash = 1000
    result = []
    collaterals = defaultdict(int)
    for trade in trades:
        _, ticker, tx_type, quantity, price = trade
        quantity = int(quantity)
        price = int(price)
        if ticker.endswith('O') and tx_type == 'B':
            collateral_stock = ticker[:-1]
            portfolio[collateral_stock] -= quantity
            if portfolio[collateral_stock] == 0:
                portfolio.pop(collateral_stock)
                if collateral_stock in last_traded_price:
                    last_traded_price.pop(collateral_stock)
            collaterals[collateral_stock] += quantity
        elif ticker.endswith('O') and tx_type == 'S':
            collateral_stock = ticker[:-1]
            portfolio[collateral_stock] += quantity
            collaterals[collateral_stock] -= quantity
            if collaterals[collateral_stock] == 0:
                collaterals[collateral_stock].pop(collateral_stock)
        # trade stock
        cash = trade_stock(tx_type, portfolio, ticker, quantity, price, cash)
        # update last trade price
        last_traded_price[ticker] = price
        cash = margin_call_with_collateral(cash, tx_type, portfolio, last_traded_price, collaterals)
    result.append(['CASH', cash])
    for k, v in portfolio.items():
        result.append([k, str(v)])
    
    # add back collateral stocks 
    for k, v in collaterals.items():
        result.append([k, str(v)])
    return result[0] + sorted(result[1:])

def margin_call(cash, tx_type, portfolio, last_traded_price):
    print('cash:', cash)
    print('last traded prices:', last_traded_price)
    print('portfolio', portfolio)
    if tx_type != 'B' or cash >= 0:
        return cash 
    sl = SortedList()
    for k, v in last_traded_price.items():
        current = Stock(v, k)
        sl.add(current)
    i = 0
    while cash < 0 and i < len(sl):
        p, stock = sl[i].price, sl[i].symbol
        num_stocks_to_sell = min(ceil(abs(cash) / p), portfolio[stock])
        print('selling', num_stocks_to_sell, stock, 'at', p, 'price')
        portfolio[stock] -= num_stocks_to_sell
        if portfolio[stock] == 0:
            portfolio.pop(stock)
            last_traded_price.pop(stock)
        cash += p * num_stocks_to_sell
        i += 1
    return cash 

def margin_call_with_collateral(cash, tx_type, portfolio, last_traded_price, collaterals):
    # during the margin call process, can collateral be sold as well?
    print('cash:', cash)
    print('last traded prices:', last_traded_price)
    print('portfolio', portfolio)
    if tx_type != 'B' or cash >= 0:
        return cash 
    sl = SortedList()
    for k, v in last_traded_price.items():
        current = Stock(v, k)
        sl.add(current)
    i = 0
    while cash < 0 and i < len(sl):
        p, stock = sl[i].price, sl[i].symbol
        num_stocks_to_sell = min(ceil(abs(cash) / p), portfolio[stock])
        print('selling', num_stocks_to_sell, stock, 'at', p, 'price')
        portfolio[stock] -= num_stocks_to_sell
        if portfolio[stock] == 0:
            portfolio.pop(stock)
            last_traded_price.pop(stock)
        cash += p * num_stocks_to_sell
        # if we sold a special stock, free up the collateral as well 
        if stock.endswith('O'):
            collateral = stock[:-1]
            collaterals[collateral] -= num_stocks_to_sell
            portfolio[collateral] += num_stocks_to_sell
        i += 1
    return cash 

if __name__ == '__main__':
    # Q1
    stocks = [["1", "AAPL", "B", "10", "10"], ["3", "GOOG", "B", "20", "5"], ["10", "AAPL", "S", "5", "15"]]
    print(get_user_portfolio(stocks))

    # Q2
    stocks = [
    ["1", "AAPL", "B", "5", "100"],
    ["2", "ABPL", "B", "5", "100"],
    ["3", "AAPL", "S", "2", "80"],
    ["4", "ABPL", "S", "2", "80"],
    ["5", "GOOG", "B", "15", "30"]
]   
    print(get_user_portfolio_with_margin_call(stocks))

    # Q2 test case 2
    stocks = [
    ["1", "AAPL", "B", "10", "100"],
    ["2", "AAPL", "S", "2", "80"],
    ["3", "GOOG", "B", "15", "20"]
]
    print(get_user_portfolio_with_margin_call(stocks))

    stocks = [
    ["1", "AAPL", "B", "5", "100"],
    ["2", "ABPL", "B", "5", "100"],
    ["3", "AAPL", "S", "2", "80"],
    ["4", "ABPL", "S", "2", "120"],
    ["5", "GOOG", "B", "15", "30"]
]
    print(get_user_portfolio_with_margin_call(stocks))
    
    # Q2 test case 4: need to sell multiple stocks
    stocks = [
        ["1", "AAPL", "B", "5", "100"],
        ["2", "ABPL", "B", "5", "100"],
        ["3", "AAPL", "S", "2", "80"],
        ["4", "ABPL", "S", "2", "120"],
        ["5", "GOOG", "B", "10", "80"]
    ]
    print(get_user_portfolio_with_margin_call(stocks))

    # Q3 test case 0
    stocks = [
    ["1", "AAPL", "B", "5", "100"],
    ["2", "GOOG", "B", "5", "75"],
    ["3", "AAPLO", "B", "5", "50"]
    ]
    print(get_user_portfolio_with_margin_call_collateral(stocks))

    # Q3 test case 1
    stocks = [
    ["1", "AAPL", "B", "6", "50"],
    ["2", "GOOG", "B", "6", "50"],
    ["3", "AAPLO", "B", "5", "25"],
    ["4", "GOOG0", "B", "5", "25"],
    ["5", "TEST", "B", "250", "1"]
    ]
    print(get_user_portfolio_with_margin_call_collateral(stocks))