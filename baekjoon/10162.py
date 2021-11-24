#전자레인지
T = int(input()) # s

A, B, C = 300, 60, 10 # s
count_a, count_b, count_c = 0, 0, 0

count_a += T // A
T = T % A

count_b += T // B
T = T % B

count_c += T // C
T = T % C

if T != 0:
    print(-1)
else:
    print(count_a, count_b, count_c)

