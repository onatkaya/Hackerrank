len_a = int(input())

set_a = set(map(int, input().split()))

command_num = int(input()) # the number of other sets.

for a in range(command_num):
    temp_command = input().split()# Entries of the operation name and the length of the other set.
    temp_set = set(map(int, input().split()))# the other set

    if(temp_command[0] == 'intersection_update'):
        set_a.intersection_update(temp_set)
    elif(temp_command[0] == 'symmetric_difference_update'):
        set_a.symmetric_difference_update(temp_set)
    elif(temp_command[0] == 'difference_update'):
        set_a.difference_update(temp_set)
    elif(temp_command[0] == 'update'):
        set_a.update(temp_set)

print(sum(set_a))