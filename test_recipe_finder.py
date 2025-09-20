import unittest
from find_recipe_match import find_recipe
from main import main

class RecipeFindTester(unittest.TestCase):
    def test_find_recipe(self):
        # preprocess like main()
        raw_input = ["egg", "milk"]

        result = find_recipe(raw_input)

        expected = {
            'Apple Pie': {
                'total_matches': 2,
                'total_ingredients': 5,
                'matched_ingredients': ['Egg', 'Milk']
            },
            'Shepards Pie': {
                'total_matches': 2,
                'total_ingredients': 6,
                'matched_ingredients': ['Egg', 'Milk']
            },
            'Pizza': {
                'total_matches': 2,
                'total_ingredients': 7,
                'matched_ingredients': ['Egg', 'Milk']
            }
        }

        self.assertEqual(result, expected)


    

if __name__ == "__main__":
    unittest.main()
