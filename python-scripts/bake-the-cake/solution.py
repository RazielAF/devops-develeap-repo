import math 

def main(recipe, available):
    max_amount = []
    for ingredient in recipe:
        try:
            amount = available[ingredient]/recipe[ingredient]
        except:
            amount = 0
        max_amount.append(amount)

    return math.floor(min(max_amount))

