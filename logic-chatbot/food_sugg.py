"""This project help you to suggest for food to eat
and save you from wasting time thinking on what to EAT """

import random


def food_suggestion():
    breakfast = [
        {
            "name": "Bread and Tea",
            "ingredients": "Bread, tea, hot water, milk, and sugar"
        },
        {
            "name": "Akara and Pap",
            "ingredients": "Beans, pepper, onions, pap, and vegetable oil"
        },
        {
            "name": "Yam and Egg",
            "ingredients": "Yam, eggs, pepper, onions, and vegetable oil"
        }
    ]

    lunch = [
        {
            "name": "Rice and Stew",
            "ingredients": "Rice, tomatoes, pepper, onions, and seasoning"
        },
        {
            "name": "Beans and Plantain",
            "ingredients": "Beans, ripe plantain, pepper, and onions"
        },
        {
            "name": "Eba and Egusi Soup",
            "ingredients": "Garri, egusi, vegetables, meat or fish, and palm oil"
        }
    ]

    dinner = [
        {
            "name": "Amala and Ewedu",
            "ingredients": "Yam flour, ewedu leaves, locust beans, and meat"
        },
        {
            "name": "Pounded Yam and Egusi",
            "ingredients": "Yam, egusi, vegetables, meat, and palm oil"
        },
        {
            "name": "Noodles and Egg",
            "ingredients": "Instant noodles, eggs, vegetables, and seasoning"
        }
    ]

    print("\n" + "=" * 45)
    print(" WELCOME TO NIGERIAN FOOD SUGGESTER")
    print("=" * 45)

    while True:

        food_time = input(
            "\nWhat would you like to eat?\n"
            "Breakfast, Lunch, or Dinner: "
        ).strip().lower()

        if food_time == "breakfast":
            selected_food = random.choice(breakfast)

        elif food_time == "lunch":
            selected_food = random.choice(lunch)

        elif food_time == "dinner":
            selected_food = random.choice(dinner)

        else:
            print("\n Invalid option.")
            print("Please enter Breakfast, Lunch, or Dinner.")
            continue

        print("\nFOOD SUGGESTION")
        print("-" * 45)

        print(f"Food: {selected_food['name']}")
        print(f"Ingredients: {selected_food['ingredients']}")

        break


food_suggestion()