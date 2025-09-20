from recipes import recipes

def find_recipe(user_ingredients):
    # Create user set ONCE
    user_set = set(user_ingredients)  # How would you create this?
    
    recipe_stats = {}
    
    for title, details in recipes.items():
        # Create recipe set for THIS recipe only
        recipe_set = set(ing.lower() for ing in details['ingredients'])  # How would you create this for current recipe?
        
        # Find intersection
        matches = user_set & recipe_set
        # print(matches)
        
        # Store results if matches found
        if matches:
            recipe_stats[title] = {
                "total_matches": len(matches),
                "total_ingredients": len(details["ingredients"]),
                "matched_ingredients": matches
            }

    # print(recipe_stats)
    return recipe_stats

