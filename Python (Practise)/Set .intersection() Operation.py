n = int(input())

set_english = set(map(int, input().split()))

b = int(input())

set_french = set(map(int, input().split()))

set_intersection = set_english.intersection(set_french)

print(len(set_intersection))