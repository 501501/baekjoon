a, b = map(int, input().split())
result = 1
while True:
    # a와 b가 같은 경우
    if a == b:
        break

    # a를 2로 나눈 나머지가 0이 아니고 10으로 나눈 나머지가 1이 아니거나,
    # b가 a보다 작은 경우
    elif (b % 2 != 0 and b % 10 != 1) or (b < a):
        result = -1
        break
    else:
        # 10으로 나누었을 때 나머지가 1인 경우
        if b % 10 == 1:
            b = b // 10
            result += 1
        # 2로 나누었을 때 나머지가 0인 경우
        else:
            b = b // 2
            result += 1

print(result)
