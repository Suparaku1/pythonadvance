from kitchen import KitchenTools, Recipe


def main():
    recipes = [
        Recipe("Hawaii Toast", ["toast bread", "ham", "pineapple", "cheese"]),
        Recipe("Ham and Cheese Sandwich", ["toast bread", "ham", "cheese"]),
        Recipe("Cheese Bread", ["bread", "cheese"]),
        Recipe("Jam Toast", ["toast bread", "jam"]),
    ]

    inventory = ["toast bread", "ham", "cheese", "jam"]

    kitchen = KitchenTools()

    shopping_list = kitchen.create_shopping_list(recipes, inventory)

    print("Shopping list:")
    for item in shopping_list:
        print(f"- {item}")

    print("\nPossible recipes:")
    kitchen.possible_recipes(recipes, inventory)


if __name__ == "__main__":
    main()
