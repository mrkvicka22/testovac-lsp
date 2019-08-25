leng = int(input())
a = list(map(int, input().split()))
def sums_a(a):
    newa = []
    for i in range(len(a)-1):
        newa.append(a[i] + a[i+1])
    return newa

for i in range(leng-1):
    a = sums_a(a)
    print(*a)