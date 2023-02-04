from collections import Counter
def nonDivisibleSubset(k, s):
    rems = Counter(a % k for a in s)
    return ( (rems[0] > 0) + (k%2 == 0 and rems[k//2] > 0) +
            sum(max(rems[i], rems[k-i]) for i in range(1,(k+1)//2)) )
