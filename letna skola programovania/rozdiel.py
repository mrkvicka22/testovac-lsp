n,x = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    for j in a[1:]:
        if abs(i-j) == x:
            print('Ano')
            exit()
    a.remove(i)
print('Nie')