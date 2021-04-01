# n: 동전의 종류
# k: 동전의 합
n, k = map(int, input().split())
coin = []
index = 0
result = 0

# 동전의 가치 입력 (오름차순)
for i in range(n):
    x = int(input())
    coin.append(x)

coin.sort(reverse=True)

for i in range(n):
    if coin[i] <= k:
        index = i
        result += k // coin[i]
        k = k - ((k // coin[i]) * coin[i])

print(result)
