english_num = int(input())

english_set = set(map(int, input().split()))

french_num = int(input())

french_set = set(map(int, input().split()))

print(len(english_set.difference(french_set)))