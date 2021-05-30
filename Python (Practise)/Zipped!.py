# n: number of students, s: number of subjects

n,s = map(int,input().split())

list_1 = []

for a in range(s):
    temp = list(map(float, input().split()))
    list_1.append(temp)

list_2 = list(zip(*list_1))

for a in list_2:
    print(sum(a) / len(a))