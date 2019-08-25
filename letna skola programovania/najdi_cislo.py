def binary_search(arr, x, l, r):
    # Check base case

    mid = l + (r - l) // 2

    # If element is present at the middle itself
    if arr[mid] == x:
        return mid+1

        # If element is smaller than mid, then it can only
    # be present in left subarray
    elif arr[mid] > x:
        return binary_search(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
    else:
        return binary_search(arr, mid + 1, r, x)

n = int(input())
a = list(map(int, input().split()))
print(a)
q = int(input())
s = []
for i in range(q):
    s.append(int(input()))
for i in s:
    print(binary_search(a,i,0,len(a)-1))
