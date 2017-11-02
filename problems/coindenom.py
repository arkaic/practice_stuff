#!/usr/bin/env python3
import time
""" Given US denomination coins, what is the algorithm to make change for any amount? 
Also, do it iteratively.
"""

WHATS_IN_YOUR_WALLET = [67, 23, 43, 37, 49] #cents
# WHATS_IN_YOUR_WALLET = range(100)

class Traveler():
    """ Wanderer of trees and purse of coins, USD """
    def __init__(self):
        self.l = []
        self.purse = {25:0, 10:0, 5:0, 1:0}
    def pop(self):
        coin = self.l.pop()
        self.purse[coin] -= 1
        return coin
    def append(self, coin):
        self.purse[coin] += 1
        self.l.append(coin)
    def peek(self):
        return self.l[-1]
    def len(self):
        return len(self.l)


def make_change(amount):
    """ Fewest coins
    Leftmost depth first search to first leaf, where each node is a US coin,
    descending ordered
    """
    if amount > 100:
        return

    coins = [25,10,5,1]
    traveler = Traveler()
    running_amt = amount
    while running_amt > 0:
        coins_to_remove = []

        for coin in coins:
            if running_amt < coin:
                coins_to_remove.append(coin)
                continue
            traveler.append(coin)
            running_amt -= coin
            break

        for coin in coins_to_remove:
            coins.remove(coin)

    assert_combos([traveler.purse], amount)
    print('fewest coins for {} cents: {}'.format(amount, result_to_print([traveler.purse])))


def make_all_change(amount):
    """ All combinations 
    Depth first search of every leaf

    stack is running collection of possible coins
    traveler carries coins
    combos tracks valid combinations
    Valid combos found in leafs
    When found, push copy of what traveler has into combo, and pop from traveler
    """
    if amount > 100:
        return
    coins = [25,10,5,1]

    stack = []  # (coin, level)
    for coin in reversed(coins):
        if coin <= amount:
            stack.append((coin, 1))

    combos = []
    traveler = Traveler()
    running_amt = 0
    while stack:
        # take next node, going down
        traveler.append(stack.pop()[0])
        running_amt += traveler.peek()

        # eval leaf
        if running_amt == amount:
            combos.append(traveler.purse.copy())
            running_amt -= traveler.pop()
            # trim stack of coins not in next level relative to traveler
            while stack and stack[-1][1] <= traveler.len():
                running_amt -= traveler.pop()
        else:
            # added unvisited
            for coin in reversed(coins):
                if coin <= amount - running_amt and coin <= traveler.peek():
                    # second conditional filters out already tried combos
                    stack.append((coin, traveler.len() + 1))
    
    print('all denominations for {} cents:'.format(amount))
    assert_combos(combos, amount)
    print(result_to_print(combos))

# #
# #  HELPER FUNCTIONS
# #
def result_to_print(combos):
    d = {25:'quarters', 10:'dimes', 5:'nickels', 1:'pennies'}
    s = ''
    for combo in combos:
        for coin, no in combo.items():
            if no > 0:
                s += '{} {}, '.format(no, d[coin])
        s = s[:-2] + '\n'
    return s

def assert_combos(combos, amt):
    """ they should all add up to amt """
    for combo in combos:
        total = 0
        for coin, no in combo.items():
            total += coin * no
        assert total == amt
    
if __name__ == '__main__':
    for amount in WHATS_IN_YOUR_WALLET:
        # make_change(amount)
        make_all_change(amount)

