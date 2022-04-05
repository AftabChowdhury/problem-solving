def tandem_bicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    total_speed = 0
    if fastest:
        blueShirtSpeeds.reverse()
    for i in range(len(redShirtSpeeds)):
        total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return total_speed


print(tandem_bicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))
print(tandem_bicycle([3, 6, 7, 2, 1], [5, 5, 3, 9, 2], False))
