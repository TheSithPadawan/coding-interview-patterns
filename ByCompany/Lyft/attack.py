"""
一道外星人打击基地的游戏题目。基地是【0，n】，外星人每次attach的范围都是1. 比如attach（1）那么【1，2】都被毁坏。如果基地全毁坏，游戏就结束了。
请实现一个class，包含下面两个functions （两个方法的时间复杂度要求是O（1））
1. void attack(double x)；
2. bool is_game_over( );
"""

store = dict()
def game_init(store, n):
    for i in range(n):
        store[i] = [i, i+1]
    return store

def attack(p, store):
    prev, next = int(p), int(p) + 1
    # if is integer, directly removing key from store 
    if p == prev:
        store.pop(p)
        return
    store[prev] = [store[prev][0], min(store[prev][1], p)]
    if next not in store:
        return
    store[next] = [p + 1, store[next][1]]

def is_game_over(store):
    return len(store) == 0

if __name__ == '__main__':
    # test case 1
    # n = 1
    # store = game_init(store, n)
    # attack(0.25, store)
    # print('is game over?', is_game_over(store))
    # attack(0, store)
    # print('is game over?', is_game_over(store))

    # test case 2
    n = 2
    store = game_init(store, n)
    attack(0, store)
    print('is game over?', is_game_over(store))
    attack(1.5, store)
    print('is game over?', is_game_over(store))
    attack(1, store)
    print('is game over?', is_game_over(store))

