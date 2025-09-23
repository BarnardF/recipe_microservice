from flask import Flask, jsonify
from data.recipes import recipes

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello,world"

@app.route('/find_recipe/<string:ingredients>')
#ai helped with this and its way simpler
def find_recipe(ingredients):
    user_set = set(ing.strip().lower() for ing in ingredients.split(","))

    
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

        sorted_recipes = sorted(
            recipe_stats.items(),
            key=lambda x: (-x[1]['total_matches'], x[1]['total_ingredients'])
        )

    # print(recipe_stats)
    return jsonify(sorted_recipes)


if __name__=="__main__":
    app.run(debug=True, port=5000)