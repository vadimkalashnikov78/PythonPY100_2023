list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

left_team = list_players[:middle_index]
right_team = list_players[middle_index:]

print(left_team)
print(right_team)
