from recipes import recipes

#ai helped with this and its way simpler
def find_recipe(user_ingredients):
    #Create user set ONCE
    user_set = set(user_ingredients)
    
    recipe_stats = {}
    
    for title, details in recipes.items():
        recipe_set = set(ing.lower() for ing in details['ingredients'])
        
        # Find intersection
        matches = user_set & recipe_set
        # print(matches)
        
        if matches:
            recipe_stats[title] = {
                "total_matches": len(matches),
                "total_ingredients": len(details["ingredients"]),
                "matched_ingredients": matches
            }

    # print(recipe_stats)
    return recipe_stats

