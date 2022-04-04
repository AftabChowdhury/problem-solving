def class_photos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
    elif redShirtHeights[0] > blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
    elif redShirtHeights[0] == blueShirtHeights[0]:
        return False
    return True


print(class_photos([5, 8, 1, 3, 4, 9], [6, 9, 2, 4, 5, 1]))
