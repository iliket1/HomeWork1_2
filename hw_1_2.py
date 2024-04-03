with open ('recipes.txt') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish_name] = ingredients
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = int(ingredient['quantity']) * person_count
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list
