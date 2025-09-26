import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY')
    SPOONACULAR_BASE_URL = 'https://api.spoonacular.com/recipes'