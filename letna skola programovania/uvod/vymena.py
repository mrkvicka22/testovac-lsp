y,x = map(int, input().split())
a = []
for i in range(y):
    a.append(list(map(int, input().split())))

for j in range(x):
    c = []
    for i in a:
        c.append(i[j])
    print(*c)
