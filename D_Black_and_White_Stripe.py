#1690D
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    w = input()
    if k == 1 and "B" in w:
        print(0)
        continue
    count_w = w[:k].count('W')

    ans = count_w

    for i in range(k,n):
        if w[i- k] == 'W':
            count_w -=1
        if w[i] == 'W':
            count_w +=1
        ans = min(ans,count_w)
    print(ans)
