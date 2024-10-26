"""
Question: https://leetcode.com/discuss/interview-question/882324/robinhood-phone-screen?page=1
[input] array.string house_trades

[input] array.string street_trades

[output] array.string

A list of unmatched trades both house and street, ordered alphabetically
"""

from collections import defaultdict, deque


def exact_match(house_trades, street_trades):
    """
    use house_trades as dictionary (symbol, type, quantity, id): key, count 
    for each street trade, if found identical prefix, reduce the count 
    for street trade with no match, directly add to result 
    then go through house trades dict, add to result if count is not zero
    returns the list, modify house_trades and street_trades 
    """
    house_dict = defaultdict(int)
    for ht in house_trades:
        house_dict[ht] += 1
    new_street_trades, new_house_trades = [], []
    result = []
    for st in street_trades:
        if st in house_dict:
            house_dict[st] -= 1
        else:
            # unmatched, save result
            new_street_trades.append(st)
            result.append(st)
    
    for k, v in house_dict.items():
        if v > 0:
            new_house_trades.append(k)
            result.append(k)
    return sorted(result), sorted(new_house_trades), sorted(new_street_trades)

"""
Follow-up 1 (Test 6,7,8,9): A "fuzzy" match is a house_trade+street_trade pair with identical symbol, type, and quantity ignoring ID. 
Prioritize exact matches over fuzzy matches. Prioritize matching the earliest alphabetical house trade with the earliest alphabetical street trade in case of ties.
"AAPL,B,0100,ABC123"
"""
def fuzzy_match(house_trades, street_trades):
    """
    use prefix (symbol,type,quantity) as key, ID as list of value, if found identical prefix, pop from deque
    for results, go through house trade dict add to result if list is not empty
    """
    house_dict = defaultdict(deque)
    for ht in house_trades:
        tokens = ht.split(',')
        prefix = ','.join(tokens[:-1])
        house_dict[prefix].append(tokens[-1])
    new_street_trades, new_house_trades = [], []
    result = []
    for st in street_trades:
        tokens = st.split(',')
        prefix = ','.join(tokens[:-1])
        if prefix in house_dict:
            house_dict[prefix].popleft()
        else:
            result.append(st)
            new_street_trades.append(st)
    for k, v in house_dict.items():
        if len(v) > 0:
            while v:
                curr = v.popleft()
                result.append(k+',' + curr)
                new_house_trades.append(k+',' + curr)
    return sorted(result), sorted(new_house_trades), sorted(new_street_trades)

"""
An offsetting match is a house_trade+house_trade or street_trade+street_trade pair where the symbol and quantity of both trades are the same, 
but the type is different (one is a buy and one is a sell). Prioritize exact and fuzzy matches over offsetting matches.
Prioritize matching the earliest alphabetical buy with the earliest alphabetical sell.
"""
def offset_match(house_trades, street_trades):
    """
    "AAPL,B,0100,ABC123" should match "AAPL,S,0100,ABC123"
    house_dict = {(symbol, type quantity): [Ids]}, if matched, pop from deque
    building results the same way as above 
    """
    house_dict = defaultdict(deque)
    for ht in house_trades:
        tokens = ht.split(',')
        prefix = ','.join(tokens[:-1])
        house_dict[prefix].append(tokens[-1])
    new_street_trades, new_house_trades = [], []
    result = []
    for st in street_trades:
        tokens = st.split(',')
        if tokens[1] == 'B':
            prefix = ','.join([tokens[0], 'S', tokens[2]])
        else:
            prefix = ','.join([tokens[0], 'B', tokens[2]])
        if prefix in house_dict:
            house_dict[prefix].popleft()
        else: # save result, unmatched
            result.append(st)
            new_street_trades.append(st)
    for k, v in house_dict.items():
        if len(v) > 0:
            while v:
                curr = v.popleft()
                result.append(k+',' + curr)
                new_house_trades.append(k+',' + curr)
    return sorted(result), sorted(new_house_trades), sorted(new_street_trades)


def match_orders(house_trades, street_trades):
    output, house_trades, street_trades = exact_match(house_trades, street_trades)
    print('output', output)
    print('remaining house_trades', house_trades)
    print('remaining street trades', street_trades)
    # no exact match, use fuzzy match now
    output, house_trades, street_trades = fuzzy_match(house_trades, street_trades)
    print('output', output)
    print('remaining house_trades', house_trades)
    print('remaining street trades', street_trades)
     # no fuzzy match, use offset match now
    output, house_trades, street_trades = offset_match(house_trades, street_trades)
    print('output', output)
    print('remaining house_trades', house_trades)
    print('remaining street trades', street_trades)
    return output

if __name__ == '__main__':
    house_trades = ["AAPL,B,0100,ABC123", 
 "GOOG,S,0050,CDC333", "  FB,B,0100,GBGGGX"]
    street_trades = ["  FB,B,0100,GBGGGG", 
 "AAPL,B,0100,ABC123","GOOG,B,0050,CDC333"]
    print(match_orders(house_trades, street_trades))