from itertools import permutations

my_str, num = input().split()

num = int(num)

my_str_arr = list(my_str)
my_str_arr.sort()
my_str = ''.join(my_str_arr)

result_list = (list(permutations(my_str,num)))

for a in result_list:
    temp_str = str(a)
    
    result_str = ""

    for b in range(0, num):
        if(b != 0 and ((5*b)+2) < len(temp_str)):
            result_str = result_str + temp_str[2 + (5*b)]
        elif(b == 0):
            result_str = temp_str[2]
    
    print(result_str)