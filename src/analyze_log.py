from src.analize_log_methods import Method


def analyze_log(path_to_file):
    csv_file = Method.reader_method(path_to_file)

    food_types = Method.get_key_by_types(csv_file, 'food', 'set')
    open_days = Method.get_key_by_types(csv_file, 'day', 'set')

    food_frequency_maria = Method.get_frequency(csv_file, 'food', 'maria')
    bigger_value_maria_food = max(food_frequency_maria.values())

# https://www.w3schools.com/python/ref_func_next.asp
# The next() function returns the next item in an iterator.
# https://stackoverflow.com/questions/7006839/alternative-to-list-comprehension-if-there-will-be-only-one-result
    most_frequent_maria_food = next(
        item[0]
        for item in food_frequency_maria.items()
        if item[1] == bigger_value_maria_food
    )

    food_frequency_arnaldo = Method.get_frequency(csv_file, 'food', 'arnaldo')
    food_frequency_joao = Method.get_frequency(csv_file, 'food', 'joao')
    day_frequency_joao = Method.get_frequency(csv_file, 'day', 'joao')

    difference_joao = food_types.difference(food_frequency_joao)
    days_difference_joao = open_days.difference(day_frequency_joao)

    infos = [
        most_frequent_maria_food,
        str(food_frequency_arnaldo['hamburguer']),
        str(difference_joao),
        str(days_difference_joao)
    ]

    break_line_infos = "\n".join(infos)

    with open('data/mkt_campaign.txt', 'w') as file:
        for item in break_line_infos:
            file.writelines(item)
