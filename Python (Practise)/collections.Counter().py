from collections import Counter

num_shoes = int(input())
size_arr = list(map(int,input().split()))
my_dict = dict(Counter(size_arr))
money_earned = 0

num_customer = int(input())

for i in range(num_customer):
    size_requested, potential_money = map(int, input().split())

    if(size_requested in my_dict.keys()): # check whether that size is available in the first place (to avoid "key error")
        if(my_dict[size_requested] > 0): # the item is at stock, earn the money
            money_earned += potential_money
            my_dict[size_requested] -= 1 # decrease the stock by 1.
        else: # failed to buy, the item got out of stock after some time
            continue

print(money_earned)