class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = InventoryControl.MINIMUM_INVENTORY.copy()
        self.foods = list(InventoryControl.INGREDIENTS)
        self.available_foods = set(self.foods)

    def check_ingredient(self, order):
        for ingredient in InventoryControl.INGREDIENTS[order]:
            if self.inventory[ingredient] <= 0:
                return False
            else:
                self.inventory[ingredient] -= 1

    def get_not_available_ingredients(self):
        return {
            ingredient: value
            for ingredient, value in self.inventory.items()
            if value == 0
        }

    # para esse trecho, consultei o repositório de David Gonzaga em
    # https://github.com/tryber/sd-012-restaurant-orders/pull/55/
    # commits/6ceb37e2c73d58e1e5fa7540d767ee528d239ab7
    def get_unavailable_foods(self, unavailable_ingredients):
        unavailable_foods = set()
        for food in self.available_foods.copy():
            for ingredient in InventoryControl.INGREDIENTS[food]:
                if ingredient in unavailable_ingredients:
                    unavailable_foods.add(food)
        return unavailable_foods

    def add_new_order(self, customer, order, day):
        if self.check_ingredient(order) is False:
            return self.check_ingredient(order)
        unavailable_ingredients = self.get_not_available_ingredients()
        unavailable_foods = self.get_unavailable_foods(unavailable_ingredients)

        for food in unavailable_foods:
            self.available_foods.remove(food)

    def get_quantities_to_buy(self):
        reference = InventoryControl().MINIMUM_INVENTORY
        ingredients_to_buy = {
            ingredient: reference[ingredient] - value
            for ingredient, value in self.inventory.items()
        }
        return ingredients_to_buy

    def get_available_dishes(self):
        return self.available_foods
