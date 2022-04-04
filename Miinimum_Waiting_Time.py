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
