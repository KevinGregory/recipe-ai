import os
from dotenv import load_dotenv
from baml_client import b
from baml_client.types import RecipeInfo
import chromadb

load_dotenv()

# Sample recipe data (same as before)
SAMPLE_RECIPES = [
    """
    Chicken Parmesan
    Ingredients:
    - 1.5 lbs chicken breast
    - 2 cups marinara sauce
    - 1 cup mozzarella cheese
    - 1/2 cup parmesan cheese
    - 1 cup breadcrumbs
    
    Instructions:
    1. Pound chicken to 1/4 inch thickness
    2. Bread chicken with breadcrumbs
    3. Fry until golden
    4. Top with sauce and cheese
    5. Bake at 375°F for 25 minutes
    """,
    
    """
    Chicken Stock Risotto
    Ingredients:
    - 1 cup arborio rice
    - 4 cups chicken stock
    - 1/2 cup white wine
    - 1 medium onion
    - 2 tbsp butter
    - 1/2 cup parmesan cheese
    
    Instructions:
    1. Sauté onion in butter
    2. Add rice, toast for 2 minutes
    3. Add wine, then stock gradually
    4. Stir constantly for 18 minutes
    5. Finish with parmesan
    """
]


def test_baml_extraction():
    """Test BAML recipe extraction"""
    print("🧪 Testing BAML recipe extraction with Gemini...")
    
    recipes = []
    for recipe_text in SAMPLE_RECIPES:
        try:
            recipe_info = b.ExtractRecipeInfo(recipe_text)
            recipes.append(recipe_info)
            print(f"✅ Extracted: {recipe_info.title}")
            print(f"   Ingredients: {len(recipe_info.ingredients)} items")
            print(f"   Cuisine: {recipe_info.cuisine}")
            print(f"   Time: {recipe_info.cook_time}")
            print()
        except Exception as e:
            print(f"❌ Error extracting recipe: {e}")
    
    return recipes


def test_package_optimization(recipes):
    """Test package optimization"""
    print("📦 Testing package optimization...")
    
    try:
        optimizations = b.OptimizePackages(recipes)
        
        print(f"Found {len(optimizations)} package optimizations:")
        for opt in optimizations:
            print(f"• {opt.ingredient}")
            print(f"  Recipe needs: {opt.recipe_amount}")
            print(f"  Package size: {opt.package_size}")
            print(f"  Leftover: {opt.leftover_amount}")
            if opt.suggestions:
                print(f"  Suggestions: {', '.join(opt.suggestions[:2])}")
            print()
            
    except Exception as e:
        print(f"❌ Error optimizing packages: {e}")


def main():
    """Main test function"""
    print("🚀 Testing Package-Aware Recipe Assistant with Gemini")
    print("=" * 55)
    
    # Test BAML extraction
    recipes = test_baml_extraction()   

    if recipes:
        test_package_optimization(recipes)
    
    print("✨ Basic Gemini system test complete!")

if __name__ == "__main__":
    main()