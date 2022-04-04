"""

  You're given a non-empty array of positive integers representing the amounts
  of time that specific queries take to execute. Only one query can be executed
  at a time, but the queries can be executed in any order.

  A query's waiting time is defined as the amount of time that it must
  wait before its execution starts. In other words, if a query is executed
  second, then its waiting time is the duration of the first query; if a query
  is executed third, then its waiting time is the sum of the durations of the
  first two queries.
"""


# O(nlogn) time | O(n) space - where n is the number of queries
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


# O(nlogn) time | O(1) space - where n is the number of queries
def minimum_waiting_time_solution2(queries):
    queries.sort()
    total_waiting_time = 0
    for i in range(len(queries) - 1):
        waiting_time = queries[i]
        remaining_query = len(queries) - (i+1)
        total_waiting_time += waiting_time * remaining_query
    return total_waiting_time


print(minimum_waiting_time([3, 2, 1, 2, 6]))

print(minimum_waiting_time_solution2([3, 2, 1, 2, 6]))
