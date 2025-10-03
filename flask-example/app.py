from flask import Flask, render_template

app = Flask(__name__)

# Sample data - in a real app, this would come from a database
recipes = [
    {
        'id': 1,
        'name': 'Adobo',
        'category': 'Main Course',
        'description': 'A savoury dish of marinated pork or chicken simmered in soy sauce, vinegar, and garlic.'
    },
    {
        'id': 2,
        'name': 'Kare-Kare',
        'category': 'Main Course',
        'description': 'A rich peanut-based stew with oxtail, beef, or pork, served with a side of shrimp paste (bagoong).'
    },
    {
        'id': 3,
        'name': 'Lumpia',
        'category': 'Main Course',
        'description': 'A crispy, golden fried spring roll filled with seasoned ground pork and vegetables, often served with sweet and sour dipping sauce.'
    }
]

@app.route('/')
def index():
    """Home page showing all recipes"""
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    """Detail page for a specific recipe"""
    # Find the recipe with the matching ID
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    
    if recipe:
        return render_template('recipe_detail.html', recipe=recipe)
    else:
        return "Recipe not found", 404

@app.route('/add-recipe')
def add_recipe():
    """Page for adding a new recipe"""
    return render_template('add_recipe.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
