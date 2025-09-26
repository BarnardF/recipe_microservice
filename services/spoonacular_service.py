#claude helped with creating this service to handle spoonacular api calls
import requests
from config import Config


class SpoonacularService:
    def __init__(self):
        self.api_key = Config.SPOONACULAR_API_KEY
        self.base_url = Config.SPOONACULAR_BASE_URL

    def find_recipes_by_ingredients(self, ingredients, number=10):
        if not self.api_key:
            print("No spoonacular api key found")
            return []
        
        #converts list into comma seperated string
        ingredients_str = ','.join(ingredients)

        url = f"{self.base_url}/findByIngredients"
        params = {
            #https://spoonacular.com/food-api/docs#Authentication
            'apiKey': self.api_key,
            #https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients
            'ingredients': ingredients_str,
            'number': number,
            'ranking': 2,
            'ignorePantry': True
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API error: {e}")
            return []