'''
Created on Aug 10, 2020

@author: noemi
'''
import requests

random_meal_url = "https://www.themealdb.com/api/json/v1/1/random.php"

"""
"strMeal" = name of meal
"strCategory" = category of meal
"strArea" = cultural region
"strInstructions" = instructions
"strMealThumb" = thumbnail
"strYoutube" = youtube link
"strTags" = tags
"strIngredient[i]" = ith ingredient (1-20)
"strMeasure[i]=ith measure for ingredient (1-20)
"""

class Recipe(object):
    '''
    Recipe class that holds information an a recipe
    '''
    
    def __init__(self):
        '''
        Constructor - Calls getNewRecipe to get random recipe
        '''
        self.getNewRecipe()
      
    def getNewRecipe(self):
        """ Obtains new random recipe from themealdb.com API and sets 
            appropriate class attributes with the new recipe info
        """
        # Obtain new recipe from themealdb.com via GET request
        json_data = requests.get(random_meal_url)
        
        # Obtains JSON data for the one random recipe. 
        # Original JSON data from GET request returns a list of recipes
        #     but only contains 1 recipe, so we just directly save the first recipe
        recipe_json = json_data.json()["meals"][0]

        # Set attributes from JSON data
        self.name = recipe_json["strMeal"]
        self.category = recipe_json["strCategory"]
        self.area = recipe_json["strArea"]
        self.tags = recipe_json["strTags"]
        self.instructions = recipe_json["strInstructions"]
        self.thumbnail = recipe_json["strMealThumb"]
        self.yt_url = recipe_json["strYoutube"]
        
        # JSON data stores corresponding ingredients & measures as their own variables
        #    i.e. "strIngredient1" & "strMeasure1", "strIngredient2" & strMeasure2", etc...
        self.ingredients_list = []
        self.measures_list = []
        
        # Iterate through the 20 ingredients/measure JSON keys and append the
        #    ingredient keys whose values are not empty (i.e. the ingredient
        #    exists
        for i in range(1, 21):
            cur_ingred = recipe_json["strIngredient"+str(i)]
            if cur_ingred:
                # If the string is not empty, put the ingredient and measure in the appropriate lists
                self.ingredients_list.append(cur_ingred)
                self.measures_list.append(recipe_json["strMeasure"+str(i)])


    def get_name(self):
        return self.name


    def get_category(self):
        return self.category


    def get_area(self):
        return self.area


    def get_tags(self):
        return self.tags


    def get_instructions(self):
        return self.instructions


    def get_thumbnail(self):
        return self.thumbnail


    def get_yt_url(self):
        return self.yt_url


    def get_ingredients_list(self):
        return self.ingredients_list


    def get_measures_list(self):
        return self.measures_list   

if __name__ == "__main__":
    Recipe()