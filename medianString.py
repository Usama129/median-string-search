from operator import ne
from tree import nextLeaf, nextVertex, bypass

# Usama Humayun - CS481 HW1

def bounded_median_string(DNA, t, n, l):
    v = [1] * l
    consensus = ['A'] * l
    # algorithm minimizes distance
    bestDistance = 100000
    i = 1 # prefix length being inspected
    while i > 0:
        if i < l:
            prefix = pattern(v[:i])
            optimisticDistance = total_distance(prefix, DNA)
            if optimisticDistance > bestDistance:
                v, i = bypass(v, i, l, 4)
            else:
                v, i = nextVertex(v, i, l, 4)
                # nextVertex() increments prefix length if going from parent to leaf
                # and increments v if going from leaf to leaf, and decrements prefix length if going from last leaf to
                # next parent
        else:
            word = pattern(v)
            dist = total_distance(word, DNA)
            if dist < bestDistance:
                bestDistance = dist
                consensus = word
            v, i = nextVertex(v, i, l, 4)
    return consensus


def median_string_tree_search(DNA, t, n, l): #brute force
    # minimizing distance
    num_pattern = [1] * l
    bestDistance = 100000
    while True:
        num_pattern = nextLeaf(num_pattern, l, 4) # DNA alphabet max is 4
        dist = total_distance(pattern(num_pattern), DNA)
        if dist < bestDistance:
            bestDistance = dist
            consensus = pattern(num_pattern)
        if num_pattern == [1] * l:
            return consensus


def total_distance(pattern, DNA):
    # aligns pattern over each DNA chain n - l + 1 times to find the minimum possible distance for each chain
    # adds up the result for each chain and returns the sum
    l = len(pattern)
    distance = 0
    for i in range (len(DNA)):
        chain = DNA[i]
        bestDistance = 100000
        for j in range (len(chain) - l + 1):
            kmer = chain[j:j+l]
            kmerDistance = hammingDistance(pattern, kmer)
            if kmerDistance < bestDistance:
                bestDistance = kmerDistance
        distance += bestDistance

    return distance

def pattern(num): # returns string DNA sequence corresponding to numerics
    pdict = dict(zip((1, 2, 3, 4), "ACGT"))
    out = ""
    for i in num:
        out += pdict[i]
    return out

def hammingDistance(x, y):
    if len(x) != len(y):
        raise ValueError('Length not equal')
    return sum(map(ne, x, y)) # number of mismatches