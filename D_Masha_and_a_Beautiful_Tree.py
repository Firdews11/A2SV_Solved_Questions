def solve(l, r):
    if l == r:
        return (p[l], p[l], 0)

    mid = (l + r) // 2

    l_min, l_max, l_ops = solve(l, mid)
    r_min, r_max, r_ops = solve(mid + 1, r)

    if l_ops == -1 or r_ops == -1:
        return (0, 0, -1)

    if l_max < r_min:
        return (l_min, r_max, l_ops + r_ops)

    if r_max < l_min:
        return (r_min, l_max, l_ops + r_ops + 1)

    return (0, 0, -1)

t = int(input())
for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))

    a, b, ans = solve(0, m - 1)
    print(ans)
