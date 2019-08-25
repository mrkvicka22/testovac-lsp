n = int(input())
lst = list(map(int, input().split()))
q = int(input())


def binary_search(a, x, l,r):
    if a == []:
        return -1
    if a[0] == x:
        return 0
    if r == l + 1:
        return -1
    mid = (l + r) // 2
    if mid >= len(a):
        return -1
    if a[mid] > x:
        return binary_search(a, x, l, mid)
    elif a[mid] < x:
        return binary_search(a, x, mid, r)
    else:
        return mid


for i in range(q):
    print(binary_search(lst, int(input()),0, len(lst)))

