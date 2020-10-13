import itertools
import operator


def Score(s, DNA, k):
    score = 0
    word = ""
    for i in range(k):
        # loop over string positions
        cnt = dict(zip("ACGT",(0,0,0,0)))
        for j, sval in enumerate(s):
            # loop over DNA strands
            base = DNA[j][sval+i]
            cnt[base] += 1
        score += max(cnt.values())
        word += max(cnt.keys(), key=(lambda key: cnt[key]))
    return score, word

def increment(s, n, l):
    if s[0] < n-l:
        s[0] += 1
        return s
    else:
        try:
            return [s[0]] + increment(s[1:], n, l)
        except IndexError:
            return s

def bruteForceSearch(DNA, t, n, l):

    bestScore = 0
    s = [0] * t
    perms = itertools.permutations(s)
    for one in perms:
        score, word = Score(one, DNA, l)
        if score > bestScore:
            bestScore = score
            bestMotif = one
            consensus = word



    return bestMotif, consensus