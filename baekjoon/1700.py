#멀티탭 스케줄링 2022-02-16 22:18 start


N, K = map(int, input().split())

seq = list(map(int, input().split()))

plug = []
cnt = 0

for i in range(K):
    if seq[i] in plug:
        continue
    if len(plug) < N:
        plug.append(seq[i])
        continue
    
    idxs = []

    for j in range(N):
        if plug[j] in seq[i:]:
            idx = seq[i:].index(plug[j])
        else:
            idx = 101
        idxs.append(idx)

    del plug[idxs.index(max(idxs))]
    plug.append(seq[i])
    cnt += 1

print(cnt)






#     print(plug)
#     tmp = 101  # 개수 최대 값
    
#     for c in plug:
#         if seq[i:].count(c) < tmp:
#             tmp = min(seq[i:].count(c), tmp)
#             tmp_chr = c
    


#     del plug[plug.index(tmp_chr)]
#     plug.append(seq[i])
#     cnt += 1

    

# print(plug)
print(cnt)
        