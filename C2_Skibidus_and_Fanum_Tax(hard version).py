t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    flag = True
    change = b[0] - a[0]
    prev = min(a[0], change)
    for i in range(1,n):
        if prev <= a[i]:
            keep = a[i]
        else:
            keep = float('inf')
        l = 0
        r = m-1
        ans = -1
        while l <= r:
            mid = l +(r-l) //2
            if b[mid] >= prev + a[i]:
                ans = mid
                r = mid -1
            else:
                l = mid +1
        if ans != -1:
            change = b[ans] - a[i]
        else:
            change = float('inf')
        best = min(keep,change)
        if best == float('inf'):
            flag = False
            break
        prev = best
    print("YES" if flag else "NO")
