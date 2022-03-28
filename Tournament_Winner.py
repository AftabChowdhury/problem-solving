def tournament_winner(competitions, results):
    point_table = {}
    for id_num, competitive_team in enumerate(competitions):
        home_team, away_team = competitive_team
        point = 3
        if results[id_num] == 0:
            point_table = assign_point_to_winning_team(away_team, point_table, point)
        else:
            point_table = assign_point_to_winning_team(home_team, point_table, point)
    highest_point = 0
    for key, value in point_table.items():
        if value > highest_point:
            highest_point = value
            winning_team = key
    return winning_team


def assign_point_to_winning_team(team, point_table, point):
    if point_table.get(team) is None:
        point_table[team] = point
    else:
        point_table[team] += point
    return point_table


champion = tournament_winner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])
print('Champion Team: ', champion)
