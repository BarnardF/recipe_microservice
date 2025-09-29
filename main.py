from flask import Flask, jsonify, render_template
from data.recipes import recipes
from services.spoonacular_service import SpoonacularService


app = Flask(__name__)
spoonacular = SpoonacularService()

@app.route('/')
def hello():
    return "something's running!"

@app.route('/interface')
def interface():
    return render_template('index.html')

@app.route('/find_recipe/<string:ingredients>')
def find_recipe(ingredients):
    if not ingredients or ingredients.strip() == "":
        return jsonify({"error": "No ingredients provided"}), 400 #missing required fields - https://restfulapi.net/http-status-codes
    
    try:
        #Split the input string by commas, remove extra spaces, convert to lowercase,
        # and build a clean list of ingredients while ignoring any empty entries
        ingredient_list = [ing.strip().lower() for ing in ingredients.split(',') if ing.strip()]

        if not ingredient_list:
            return jsonify({"error": "No valid ingredients provided"}), 400
        
        local_results = get_local_recipes(ingredient_list)
        api_results = get_spoonacular_recipes(ingredient_list)

    #     combined_results = {
    #         'query': ingredients,
    #         'local_recipes': local_results,
    #         'spoonacular_recipes': api_results,
    #         'total_local': len(local_results),
    #         'total_api': len(api_results),
    #         'status': 'success'
    #     }

    # return jsonify(combined_results)

        return jsonify({
            'query': ingredients,
            'local_recipes': local_results,
            'spoonacular_recipes': api_results,
            'total_local': len(local_results),
            'total_api': len(api_results),
            'status': 'local' if not api_results else 'local + spoonacular'
        })
    
    except Exception as e:
        return jsonify({"error": f"server error: {str(e)}"}), 500



def get_local_recipes(ingredient_list):
    user_set = set(ingredient_list)
    recipe_stats = {}
    
    for title, details in recipes.items():
        recipe_set = set(ing.lower() for ing in details['ingredients'])
        # Find intersection
        matches = user_set & recipe_set
        # print(matches)

        if matches:
            match_percentage = len(matches) / len(details['ingredients']) * 100

            # if match_percentage >= 0.4:
            recipe_stats[title] = {
                "total_matches": len(matches),
                "total_ingredients": len(details["ingredients"]),
                "matched_ingredients": list(matches),
                "match_percentage": round(match_percentage, 1)
            }

    #sort by match percentage and then by fewer total ingredients
    sorted_recipes = sorted(
        recipe_stats.items(),
        key=lambda x: (-x[1]['match_percentage'], x[1]['total_ingredients'])
    )

    #if only 3 or less ingredients givin return top 5 macthes
    if len(ingredient_list) <= 3:
        return sorted_recipes[:5]
    else:
        #if more ingredients return recipes with a 40 or above match
        filtered_recipes = []
        for r in sorted_recipes:
            match_percentage = r[1]['match_percentage']
            if match_percentage >= 40:
                filtered_recipes.append(r) 
        return filtered_recipes

    # print(recipe_stats)
    # return sorted_recipes



def get_spoonacular_recipes(ingredient_list):
    # raw_results = spoonacular.find_recipes_by_ingredients(ingredient_list)

    # filtered_results = []
    # for recipe in raw_results:
    #     used_count = len(recipe.get('usedIngredients', []))
    #     missed_count = len(recipe.get('missedIngredients', []))
    #     total_count = used_count + missed_count

    #     if total_count > 0:
    #         match_percentage = used_count/ total_count * 100

    #         recipe["match_percentage"] = round(match_percentage, 1)

    #         if len(ingredient_list) <= 3:
    #             filtered_results.append(recipe)
    #         else:
    #             if match_percentage >= 40:
    #                 filtered_results.append(recipe)

    # filtered_results.sort(key=lambda r: r.get("match_percentage", 0), reverse=True) #largest to smallest
    
    # if len(ingredient_list) <= 3:
    #     return filtered_results[:5]
    # else:
    #     return filtered_results

    #ai helped with the following to format spoonacular to be more similar with local recipes - chatgpt 29 Sep 2025
    raw_results = spoonacular.find_recipes_by_ingredients(ingredient_list)
    user_set = set(ingredient_list)

    normalized_results = []
    for recipe in raw_results:
        used_ingredients = [ing['name'].lower() for ing in recipe.get('usedIngredients', [])]
        missed_ingredients = [ing['name'].lower() for ing in recipe.get('missedIngredients', [])]

        total_count = len(used_ingredients) + len(missed_ingredients)
        if total_count == 0:
            continue

        match_percentage = len(used_ingredients) / total_count * 100

        normalized_recipe = {
            "title": recipe.get("title", "Unknown"),
            "total_matches": len(used_ingredients),
            "total_ingredients": total_count,
            "matched_ingredients": used_ingredients,
            "missed_ingredients": missed_ingredients,
            "match_percentage": round(match_percentage, 1),
            "spoonacular_id": recipe.get("id")  # optional, useful for API links
        }

        if len(ingredient_list) <= 3:
            normalized_results.append(normalized_recipe)
        else:
            if match_percentage >= 40:
                normalized_results.append(normalized_recipe)

    normalized_results.sort(key=lambda r: r["match_percentage"], reverse=True) #largest to smallest
    
    if len(ingredient_list) <= 3:
        return normalized_results[:5]
    else:
        return normalized_results



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