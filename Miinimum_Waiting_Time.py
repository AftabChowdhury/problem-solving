def minimum_waiting_time(queries):
    queries.sort()
    sum = 0
    sum_list = []
    for i in range(len(queries) - 1):
        sum += queries[i]
        sum_list.append(sum)
    sum = 0
    for i in range(len(sum_list)):
        sum += sum_list[i]
    return sum


print(minimum_waiting_time([3, 2, 1, 2, 6]))
