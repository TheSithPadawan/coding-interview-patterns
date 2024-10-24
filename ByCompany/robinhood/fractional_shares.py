"""
Question: https://leetcode.com/playground/4oRujNmW

algo
if hood doesn not have enough inventory to fill order, buy whole share from stock exchange
number of shares needed = ceil(demand - current)

after tx, ensure we have less than 1, only keep the decimal part of a floating point number
E.g. 3.25 -> 0.25
"""

# returns list of list 
# input: orders [symbol, order type, quantity, price]
from collections import defaultdict
from math import ceil


def handle(orders, existing):
    inventory = defaultdict(float)
    # first update inventory fom existing
    for symbol, num in existing:
        inventory[symbol] += int(num) / 100

    for order in orders:
        symbol, order_type = order[0], order[1]
        quantity = 0
        current_price = int(order[3]) / 100
        if order[2].startswith('$'):
            quantity = int(order[2][1:]) / (int(order[3])/100)
        else:
            quantity = int(order[2]) / 100
        if order_type == 'B':
            if inventory[symbol] < quantity:
                # this is the amount we bought from market
                need = ceil(quantity - inventory[symbol])
                remt = need + inventory[symbol] - quantity
            else:
                remt = inventory[symbol] - quantity
            if remt > 1:
                digit = str(remt).split('.')[1:][0]
                digit_string = f"0.{digit}"
                inventory[symbol] = float(digit_string)
            else:
                inventory[symbol] = remt
        elif order_type == 'S':
            remt = inventory[symbol] + quantity
            # update inventory 
            if remt > 1:
                digit = str(remt).split('.')[1:][0]
                digit_string = f"0.{digit}"
                inventory[symbol] = float(digit_string)
            else:
                inventory[symbol] = remt

    
    # output inventory
    result = []
    for symbol, remt in inventory.items():
        amount = "{:.2f}".format(remt)
        result.append([symbol, amount.split('.')[1:][0]])
    return result
        
        

if __name__ == "__main__":
    current = [["AAPL","99"]]
    orders = [["AAPL","B","42","100"]]
    print(handle(orders, current))

    current = [["AAPL","50"]]
    orders = [["AAPL","B","$42","100"]]

    print(handle(orders, current))

    # scenario 3
    current = []
    orders = [["AAPL","B","150","100"], ["AAPL","B","40","100"],["AAPL","B","50","100"]]
    print(handle(orders, current))
