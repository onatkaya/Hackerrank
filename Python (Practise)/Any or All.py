n = int(input())
my_list = list(map(int, input().split()))
print(all(list(map(lambda x: x>0, my_list))) and    any(list(map( lambda x: x == x[::-1] ,list(map(str, my_list))))))