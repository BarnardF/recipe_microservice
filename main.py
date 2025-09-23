from flask import Flask
from data.recipes import recipes
from find_recipe_match import find_recipe

app = Flask(__name__)



@app.route('/')
def main():
    user_input = input("Enter ingredients (seperated by comma's): ").lower().split(",")
    user_ingredients_list = [u_input.strip() for u_input in user_input]

    recipe_stats = find_recipe(user_ingredients_list)
    
    if recipe_stats:
        print(f"Recipes with matching ingrediences, {user_ingredients_list}, found:")

        
        sorted_recipes = sorted(
            recipe_stats.items(),
            key=lambda x: (-x[1]['total_matches'], x[1]['total_ingredients'])
        )

        for recipe, stats in sorted_recipes:
            print(f"- {recipe}:\n  Time: {recipes[recipe]['time']}\n  Difficulty: {recipes[recipe]['difficulty']}\n  {stats['total_matches']}/{stats['total_ingredients']} matches-{stats['matched_ingredients']}")
        
    else:
        print(f"No recipes found with ingredients - {user_ingredients_list}")
    
    # print(amount_of_ingredients)


if __name__=="__main__":
    app.run(debug=True, port=5000)