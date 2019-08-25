x = int(input())
a = []
for i in range(x):
    a.append(list(map(int, input().split())))

for j in range(x):
    c = []
    for i in a:
        c.append(i[x-j-1])
    print(*c)