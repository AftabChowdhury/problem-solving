"""
  It's photo day at the local school, and you're the photographer assigned to
  take class photos. The class that you'll be photographing has an even number
  of students, and all these students are wearing red or blue shirts. In fact,
  exactly half of the class is wearing red shirts, and the other half is wearing
  blue shirts. You're responsible for arranging the students in two rows before
  taking the photo. Each row should contain the same number of the students and
  should adhere to the following guidelines:
  1. All students wearing red shirts must be in the same row.
  2. All students wearing blue shirts must be in the same row.
  3. Each student in the back row must be strictly taller than the student
    directly in front of them in the front row.


  You're given two input arrays: one containing the heights of all the students
  with red shirts and another one containing the heights of all the students
  with blue shirts. These arrays will always have the same length, and each
  height will be a positive integer. Write a function that returns whether or
  not a class photo that follows the stated guidelines can be taken.

"""


# O(nlog(n)) time | O(1) space - where n is the number of students
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
