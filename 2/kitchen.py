class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print(self):
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")


class KitchenTools:
    def create_shopping_list(self, recipes, inventory):
        shopping_list = []

        for recipe in recipes:
            for ingredient in recipe.ingredients:
                if ingredient not in inventory and ingredient not in shopping_list:
                    shopping_list.append(ingredient)

        return shopping_list

    def possible_recipes(self, recipes, inventory):
        possible = []

        for recipe in recipes:
            can_cook = True

            for ingredient in recipe.ingredients:
                if ingredient not in inventory:
                    can_cook = False
                    break

            if can_cook:
                possible.append(recipe)

        for recipe in possible:
            print(recipe.name)

        return possible
