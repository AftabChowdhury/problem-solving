# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    ways = [float("inf") for i in range(n+1)]
    ways[0] = 0
    for denom in denoms:
        for i in range(1, n+1):
            if denom <= i:
                ways[i] = min(ways[i], ways[i-denom] + 1)
    if ways[n] != float('inf'):
        return ways[n]
    return -1


minNumberOfCoinsForChange(7, [1, 5, 10])
