from src.analize_log_methods import Method


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.track_orders = []
        self.read_file = Method.reader_method('data/orders_1.csv')

    def __len__(self):
        return len(self.track_orders)

    def add_new_order(self, customer, order, day):
        self.track_orders.append(
            [customer, order, day]
        )

    def get_customer_info(self, customer, index):
        user_info = {}
        for info in self.track_orders:
            if customer in info:
                if customer not in user_info:
                    user_info[customer] = [info[index]]
                else:
                    user_info[customer].append(info[index])
        return user_info

    def get_most_ordered_dish_per_customer(self, customer):
        food_list = self.get_customer_info(customer, 1)

        food_frequency = {}
        most_frequent = food_list[customer][0]

        for food in food_list[customer]:
            if food not in food_frequency:
                food_frequency[food] = 1
            else:
                food_frequency[food] += 1
            if food_frequency[food] > food_frequency[most_frequent]:
                most_frequent = food

        return most_frequent

    def get_never_ordered_per_customer(self, customer):
        food_list_by_customer = set(
            self.get_customer_info(customer, 1)[customer]
        )

        available_dishes = Method.get_key_by_types(
            self.read_file,
            'food',
            'set'
        )

        unordered_dishes = available_dishes.difference(food_list_by_customer)

        return unordered_dishes

    def get_days_never_visited_per_customer(self, customer):
        day_list_by_customer = set(
            self.get_customer_info(customer, 2)[customer]
        )

        available_days = Method.get_key_by_types(self.read_file, 'day', 'set')

        unordered_days = available_days.difference(day_list_by_customer)

        return unordered_days

    def get_days(self):
        return [info[2] for info in self.track_orders]

    def get_busiest_day(self):
        all_days_list = self.get_days()

        busiest_day = Method.get_most_busiest_day(all_days_list)

        return busiest_day

    def get_least_busy_day(self):
        all_days_list = self.get_days()

        less_busiest_day = Method.get_least_busiest_day(all_days_list)

        return less_busiest_day
