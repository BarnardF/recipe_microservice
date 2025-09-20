import unittest
from find_recipe_match import find_recipe

class RecipeFindTester(unittest.TestCase):
    def test_find_recipe(self):
        user_input = "egg, milk"
        result = find_recipe(user_input)
        self.assertEqual(result, "{'Apple Pie': {'matches': 2, 'total_ingredients': 5, 'matched_ingredients': ['Egg', 'Milk']}, 'Shepards Pie': {'matches': 2, 'total_ingredients': 6, 'matched_ingredients': ['Egg', 'Milk']}, 'Pizza': {'matches': 2, 'total_ingredients': 7, 'matched_ingredients': ['Egg', 'Milk']}} ")