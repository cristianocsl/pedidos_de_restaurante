import csv


class Method:
    def validate_extension(self, path_to_file):
        path_split = path_to_file.split(".")
        if 'csv' not in path_split:
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    def get_frequency(csv_file, key, person):
        dict_frequency = {}
        for item in csv_file:
            if item['name'] == person:
                if item[key] not in dict_frequency:
                    dict_frequency[item[key]] = 1
                else:
                    dict_frequency[item[key]] += 1
        return dict_frequency

    def reader_method(path_to_file):
        method = Method()
        method.validate_extension(path_to_file)
        try:
            with open(path_to_file, "r") as file:
                fieldnames = ['name', 'food', 'day']
                csv_file = csv.DictReader(file, fieldnames=fieldnames)
                return [row for row in csv_file]
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    def get_key_by_types(csv_file, key_name, list_or_set):
        value_list = [item[key_name] for item in csv_file]
        if list_or_set == 'set':
            return (set(value_list))
        if list_or_set == 'list':
            return value_list

    def get_most_busiest_day(list_of_days):
        day_frequency = {}
        most_frequent_day = list_of_days[0]

        for day in list_of_days:
            if day not in day_frequency:
                day_frequency[day] = 1
            else:
                day_frequency[day] += 1
            if day_frequency[day] > day_frequency[most_frequent_day]:
                most_frequent_day = day

        return most_frequent_day

    def get_least_busiest_day(list_of_days):
        day_frequency = {}
        least_frequent_day = list_of_days[0]

        for day in list_of_days:
            if day not in day_frequency:
                day_frequency[day] = 1
            else:
                day_frequency[day] += 1
            if day_frequency[day] < day_frequency[least_frequent_day]:
                least_frequent_day = day

        return least_frequent_day
