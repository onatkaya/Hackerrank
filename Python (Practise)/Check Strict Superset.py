set_a = set(map(int, input().split()))

num_of_cases = int(input())

all_superset = True

for a in range(num_of_cases):
    set_b = set(map(int, input().split()))
    if(set_a.intersection(set_b) == set_b and set_a != set_b): # set A is a super-set of B. Bool remains True
        continue
    else: # There is a contradictory case. Print "False" and stop the program.
        all_superset = False
        print(all_superset)
        break

if(all_superset): # Print "True" if it is still that way
    print(all_superset)