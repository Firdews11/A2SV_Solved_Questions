t = int(input())
for _ in range(t):
    n, coins = map(int, input().split())

    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))

    casinos.sort()

    for l, r, real in casinos:
        if l <= coins <= r:
            coins = max(coins, real)

    print(coins)
