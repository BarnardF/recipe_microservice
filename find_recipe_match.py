from recipes import recipes

def find_recipe(user_ingredients_list):
    recipe_stats = {}

    for title, details in recipes.items():
        matched_ing = []
        for ingredient in details['ingredients']:
            for user_ingredient in user_ingredients_list:
                if user_ingredient.lower() == ingredient.lower():
                    matched_ing.append(ingredient)
        
        if matched_ing:
            recipe_stats[title] = {
                "matches": len(matched_ing),
                "total_ingredients": len(details["ingredients"]),
                "matched_ingredients": matched_ing
            }



    return recipe_stats
                    


