n = int(input()) # 배달해야 하는 설탕의 무게
result = 0

count3 = 0 # 3 킬로그램 설탕의 수
count5 = n // 5  # 5 킬로그램 설탕의 최대 수

while True:
    if (n - (count5 * 5)) % 3 == 0:
        count3 = (n - (count5 * 5)) // 3
        result = count3 + count5
        break
    else:
        count5 -= 1 # 5 킬로그램 설탕 수를 줄여가면서 확인
        if count5 == -1:
            result = -1
            break

        if (n - (count5 * 5)) % 3 == 0:
            count3 = (n - (count5 * 5)) // 3
            result = count3 + count5
            break

print(result)
