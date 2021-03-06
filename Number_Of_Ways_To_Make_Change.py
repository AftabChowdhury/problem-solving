# O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(0, n+1)]
    ways[0] = 1
    for denom in denoms:
        for i in range(1, n+1):
            if denom <= i:
                ways[i] += ways[i-denom]
    return ways[n]
