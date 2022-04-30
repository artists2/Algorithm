s = [1,2,3,4,5]

def right_shift(l):
    print(l[-1], l[:-1])
    return [l[-1]] + l[:-1]

print(right_shift(s))