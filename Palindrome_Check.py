def is_palindrome(string):
    start = 0
    last = len(string) - 1
    while start <= len(string)/2:
        if string[start] != string[last]:
            return False
        start += 1
        last -= 1
    return True


print(is_palindrome('abcdcba'))
