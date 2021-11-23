n = int(input())

result =0

while 1:
    if n % 5 != 0:
        result += 1
        n -= 3
        if n == 2 or n == 1 or n < -1:
            result = -1
            break
        continue
    elif n % 5 == 0:
        result += (n // 5)
        break
    else:
        result = -1
        break

  

print(result) 