t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()

    pos = x
    first = -1

    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1

        if pos == 0:
            first = i + 1
            break

    if first == -1 or first > k:
        print(0)
        continue

    pos = 0
    cycle = -1
    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1

        if pos == 0:
            cycle = i + 1
            break

    if cycle == -1:
        print(1)
    else:
        print(1 + (k - first) // cycle)
