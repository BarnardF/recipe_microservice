from flask import Flask, jsonify
from data.recipes import recipes
from services.spoonacular_service import SpoonacularService


app = Flask(__name__)
spoonacular = SpoonacularService()

@app.route('/')
def hello():
    return "recipe api local + spoonacular"

@app.route('/find_recipe/<string:ingredients>')
def find_recipe(ingredients):
    ingredient_list = [ing.strip().lower() for ing in ingredients.split(',')]

    local_results = get_local_recipes(ingredient_list)
    api_results = get_spoonacular_recipes(ingredient_list)

    combined_results = {
        'query': ingredients,
        'local_recipes': local_results,
        'spoonacular_recipes': api_results,
        'total_local': len(local_results),
        'total_api': len(api_results)
    }

    return jsonify(combined_results)

def get_local_recipes(ingredient_list):
    user_set = set(ingredient_list)
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
                "matched_ingredients": list(matches)
            }

    # used to sort recipes based on the most matches and recipe with the least ingredients
    sorted_recipes = sorted(
        recipe_stats.items(),
        key=lambda x: (-x[1]['total_matches'], x[1]['total_ingredients'])
    )

    # print(recipe_stats)
    return sorted_recipes

def get_spoonacular_recipes(ingredient_list):
    return spoonacular.find_recipes_by_ingredients(ingredient_list)

#testing api endpoint
@app.route('/test_api/<string:ingredients>')
def test_api(ingredients):
    ingredients_list = [ing.strip().lower() for ing in ingredients.split(",")]
    api_results = spoonacular.find_recipes_by_ingredients(ingredients_list)
    
    return jsonify({
        "query": ingredients,
        "api_results": api_results,
        "count": len(api_results)
    })

if __name__=="__main__":
    app.run(debug=True, port=5000)