n = int(input())
s = set(map(int, input().split()))

command_num = int(input())

for a in range(command_num):
    temp_input = input().split()
    if(temp_input[0] == 'discard'):
        s.discard(int(temp_input[1]))
    elif(temp_input[0] == 'remove'):
        s.remove(int(temp_input[1]))
    elif(temp_input[0] == 'pop'):
        s.pop()

print(sum(s))
