n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
current_sum = 0
left = 0

for right in range(n):
    current_sum += arr[right]
    while current_sum > s:
        current_sum -= arr[left]
        left += 1
    count += (right - left + 1)

print(count)
