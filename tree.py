# Usama Humayun - CS481 HW1

def nextLeaf(a, L, k):
    for i in range(L-1, -1, -1):
        if a[i] < k:
            a[i] += 1
            return a
        a[i] = 1
    return a

def allLeaves(L, k):
    a = [1] * L
    while True:
        print(a)
        a = nextLeaf(a, L, k)
        if a == [1] * L:
            return

def nextVertex(a, i, L, k):
    if i < L:
        a[i] = 1
        return a,i+1
    else:
        for j in range(L-1, -1, -1):
            if a[j] < k:
                a[j] += 1
                return a, j+1
    return a,0

def bypass(a, i, L, k):
    for j in range(i-1, -1, -1):
        if a[j] < k:
            a[j] += 1
            return a, j+1
    return a, 0