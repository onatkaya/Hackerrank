k = int(input())

room_list = list(map(int, input().split()))

set_room = set(room_list) # len(set_room) = group_num + 1 (captain)

sum_room_list = sum(room_list)
set_sum_list = sum(set_room) * k  # k*(all elements' sum)

temp_sum = (sum(set_room) * k)- sum(room_list) # after this we have: (k-1)*(our_number). It is k-1, because 1 of them is actually used (captain's number).

temp_sum = temp_sum // (k-1)

print((temp_sum))

