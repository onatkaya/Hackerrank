from itertools import product

a_list = list(map(int,input().split()))

b_list = list(map(int,input().split()))

result_list = map(str,(list(product(a_list, b_list))))

print(' '.join(result_list))
