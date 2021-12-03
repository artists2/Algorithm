T = int(input())
answer = []
n = []
for _ in range(0, T):
    tmp = int(input())
    n.append(str(bin(tmp)[2::][::-1]))

for i in n:
    location = []
    for j in range(0, len(str(i))):
        if i[j] == '1':
            location.append(j)
    answer.append(location)

for i in answer:
    print(' '.join(str(_) for _ in i))
