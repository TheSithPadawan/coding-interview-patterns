
from collections import deque


def get_candlestick_chart(input_string):
    pairs = input_string.split(',')

    dps = []
    for pair in pairs:
        pair_list = pair.split(':')
        price, time = int(pair_list[0]), int(pair_list[1])
        dps.append((time, price))
    dps.sort()
    print('time, price combination', dps)
    dps = deque(dps)
    start, end = 0, 10
    first, last, max_price, min_price = -1, 0, 0, 2**31 - 1
    result = []
    while dps:
        # handle one interval here
        while dps and dps[0][0] < end:
            time, price = dps.popleft()
            if first == -1:
                first = price
            last = price
            max_price = max(max_price, price)
            min_price = min(min_price, price)
        if first == -1:
            # no data point in current interval
            last_price = result[-1][2]
            result.append([start, last_price, last_price, last_price, last_price])
        else:
            result.append([start, first, last, max_price, min_price])
        # update interval
        start += 10
        end += 10
        # reset cycle
        first, last, max_price, min_price = -1, 0, 0, 2**31 - 1
    return result




if __name__ == '__main__':
    # test case 1
    input_string = '1:0,3:10,2:12,4:19,5:35'
    print(get_candlestick_chart(input_string))
    # test case 2
    input_string = "1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,11:10,12:11,13:12,14:13,15:14,16:15,17:16,18:17,19:18,20:19"
    print(get_candlestick_chart(input_string))