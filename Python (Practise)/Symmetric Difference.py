n = int(input())

set_1 = set(map(int, input().split()))

m = int(input())

set_2 = set(map(int, input().split()))

diff_1 = set_1.difference(set_2)

diff_2 = set_2.difference(set_1)

diff_1 = diff_1.union(diff_2)

result_set = sorted(diff_1)

for a in result_set:
    print(a)