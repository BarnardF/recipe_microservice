import unittest
from recipe_finder import find_recipe

class RecipeFindTester(unittest.TestCase):
    def test_find_recipe(self):
        user_input = "milk"
        result = find_recipe(user_input)
        self.assertEqual(result, """Recipes with matching ingrediences, milk, found:
- Apple Pie: time: 1 hour, difficulty: medium 
- Shepards Pie: time: 1.5 hour, difficulty: medium 
- Pizza: time: 40 min, difficulty: easy """)