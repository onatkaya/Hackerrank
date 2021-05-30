n = int(input())

set_english = set(map(int, input().split()))

b = int(input())

set_french = set(map(int, input().split()))

set_union = set_english.union(set_french)

print(len(set_union))