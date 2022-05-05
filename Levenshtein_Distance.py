# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    for r in range(0, len(str1) + 1):
        for c in range(0, len(str2) + 1):
            if r == 0 and c == 0:
                edits[r][c] = 0
            elif r == 0:
                edits[r][c] = edits[r][c - 1] + 1
            elif c == 0:
                edits[r][c] = edits[r - 1][c] + 1
            elif str1[r - 1] == str2[c - 1]:
                edits[r][c] = edits[r - 1][c - 1]
            else:
                edits[r][c] = 1 + min(edits[r][c - 1], edits[r - 1][c - 1], edits[r - 1][c])

    return edits[len(str1)][len(str2)]


print(levenshteinDistance('abc', 'yabd'))
