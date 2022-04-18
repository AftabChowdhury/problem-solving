# O(n) time | O(n) space - where n is the length of the input string
def runLengthEncoding(string):
    # Write your code here.
    count = 0
    run_length_array = []
    for i in range(1, len(string)):
        count += 1
        previous_character = string[i-1]
        current_character = string[i]
        if previous_character != current_character or count == 9:
            run_length_array.append(str(count))
            run_length_array.append(previous_character)
            count = 0
    run_length_array.append(str(count + 1))
    run_length_array.append(string[len(string) - 1])

    return "".join(run_length_array)


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
print(runLengthEncoding("aA"))
print(runLengthEncoding("************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"))
print(runLengthEncoding(" "))
