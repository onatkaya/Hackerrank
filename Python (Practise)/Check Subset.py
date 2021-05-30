num_of_cases = int(input())

for a in range(num_of_cases):
    length_a = int(input())
    set_a = set(map(int, input().split()))

    length_b = int(input())
    set_b = set(map(int, input().split()))

    if(set_a.intersection(set_b) == set_a):
        print("True")
    else:
        print("False")