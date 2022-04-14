def bin_search(data, target, start, end):
    idx = (start + end) // 2
    mid = data[idx]

    if target == mid:
        print(f'idx: {idx}')
        return
    elif mid > target:
        bin_search(data, target, start, idx-1)
    elif mid < target:
        bin_search(data, target, idx+1, end)

    else:
        return




target = 25
data = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(data)

data.sort()
start = 0 
end = length-1
print(data)
bin_search(data,target,0,end)
