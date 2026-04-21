#Q 1197C
n, k = map(int, input().split())
a = list(map(int, input().split()))

diffs = [a[i+1] - a[i] for i in range(n-1)]

diffs.sort()

if k <n :
    print(sum(diffs[:n-k]) )
else:
    print(0)
