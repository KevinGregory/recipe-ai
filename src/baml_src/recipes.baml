class RecipeInfo {
  title string
  ingredients string[]
  instructions string[]
  cuisine string
  cook_time int
}

class PackageOptimization {
  ingredient string
  recipe_amount string
  package_size string
  leftover_amount string
  suggestions string[]
}

function ExtractRecipeInfo(recipe_text: string) -> RecipeInfo {
  client Gemini
  prompt #"
    Extract recipe information from this text:
    {{ recipe_text }}
    
    Parse into structured format with title, ingredients list, instructions, cuisine, and the cook time in minutes. Call total time it will take to make the recipe "cook_time".
  "#
}

function OptimizePackages(recipes: RecipeInfo[]) -> PackageOptimization[] {
  client Gemini
  prompt #"
    Analyze these recipes for package optimization:
    {% for recipe in recipes %}
    Recipe: {{ recipe.title }}
    Ingredients: {{ recipe.ingredients }}
    ---
    {% endfor %}
    
    For each ingredient, determine:
    1. How much the recipes need
    2. Typical grocery store package sizes
    3. How much will be leftover
    4. Suggestions for using leftovers
  "#
}

