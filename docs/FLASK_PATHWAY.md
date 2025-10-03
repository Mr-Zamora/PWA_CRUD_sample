# Flask Pathway: From Static HTML to Dynamic Web Application

This document outlines the educational pathway for Year 12 software engineering students to transform this static HTML website into a dynamic Flask web application with SQL database integration.

## Current Structure: Flat HTML Website

The current project demonstrates fundamental web development concepts:

1. **HTML Structure**: Multiple pages with consistent layout (index, recipe-detail, about-this, contact, add-recipe)
2. **CSS Styling**: Responsive design using flexbox and grid layouts
3. **Basic JavaScript**: Simple interactivity with the hamburger menu
4. **Asset Management**: Local images and audio files organized in dedicated folders
5. **Form Handling**: Basic form structure in add-recipe.html (currently non-functional)

## Educational Value

This project is valuable for Year 12 students because it:

1. **Demonstrates Clean HTML/CSS**: Shows proper separation of structure and presentation
2. **Illustrates Responsive Design**: Uses media queries to adapt to different screen sizes
3. **Shows Consistent Navigation**: Header and footer patterns across all pages
4. **Presents Form Design**: Input fields, labels, and submission buttons

## Pathway to Flask and SQL

### 1. Flask Integration

- **Convert HTML to Templates**:
  - Move HTML files to a `/templates` folder
  - Extract repeated elements (header, footer) into a base template
  - Use template inheritance with `{% extends %}` and `{% block %}` tags

- **Create Flask Application Structure**:
  ```python
  from flask import Flask, render_template
  
  app = Flask(__name__)
  
  @app.route('/')
  def index():
      return render_template('index.html')
  
  @app.route('/recipe/<recipe_id>')
  def recipe_detail(recipe_id):
      # Later will fetch from database
      return render_template('recipe_detail.html')
  ```

- **Organize Static Files**:
  - Move CSS, images, and audio to a `/static` folder
  - Update references in templates: `<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">`

### 2. Database Integration

- **Create Database Models**:
  ```python
  from flask_sqlalchemy import SQLAlchemy
  
  db = SQLAlchemy(app)
  
  class Recipe(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(100), nullable=False)
      description = db.Column(db.Text, nullable=False)
      ingredients = db.Column(db.Text, nullable=False)
      directions = db.Column(db.Text, nullable=False)
      category = db.Column(db.String(50), nullable=False)
      image_path = db.Column(db.String(255))
  ```

- **Populate Templates with Data**:
  ```python
  @app.route('/')
  def index():
      recipes = Recipe.query.all()
      return render_template('index.html', recipes=recipes)
  ```

- **In Templates**:
  ```html
  {% for recipe in recipes %}
  <div class="card">
      <p class="category">{{ recipe.category }}</p>
      <h3><a href="{{ url_for('recipe_detail', recipe_id=recipe.id) }}" class="recipe-link">{{ recipe.name }}</a></h3>
      <p class="recipe-short-des">{{ recipe.description }}</p>
  </div>
  {% endfor %}
  ```

### 3. Form Processing

- **Create Form Classes with Flask-WTF**:
  ```python
  from flask_wtf import FlaskForm
  from wtforms import StringField, TextAreaField, FileField, SubmitField
  from wtforms.validators import DataRequired
  
  class RecipeForm(FlaskForm):
      name = StringField('Recipe Name', validators=[DataRequired()])
      description = StringField('Description', validators=[DataRequired()])
      ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
      directions = TextAreaField('Directions', validators=[DataRequired()])
      image = FileField('Upload Image')
      submit = SubmitField('Add')
  ```

- **Handle Form Submission**:
  ```python
  @app.route('/add-recipe', methods=['GET', 'POST'])
  def add_recipe():
      form = RecipeForm()
      if form.validate_on_submit():
          # Process form data and save to database
          new_recipe = Recipe(
              name=form.name.data,
              description=form.description.data,
              ingredients=form.ingredients.data,
              directions=form.directions.data
          )
          db.session.add(new_recipe)
          db.session.commit()
          return redirect(url_for('index'))
      return render_template('add_recipe.html', form=form)
  ```

### 4. Additional Features

- **User Authentication**:
  - Implement login/registration with Flask-Login
  - Add user relationships to recipes

- **Search Functionality**:
  - Create search forms and queries
  - Implement filtering by category

- **API Development**:
  - Create RESTful endpoints for recipe data
  - Enable AJAX interactions

## Recommended Flask Project Structure

```
app/
├── static/
│   ├── images/
│   ├── audio/
│   └── styles.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── recipe_detail.html
│   ├── about.html
│   ├── contact.html
│   └── add_recipe.html
├── models.py      # Database models
├── routes.py      # Route handlers
├── forms.py       # Form classes
├── app.py         # Application setup
└── instance/
    └── database.db
```

## Learning Progression

1. **Week 1**: Flask basics, templates, and static files
2. **Week 2**: Database setup and models
3. **Week 3**: Forms and data validation
4. **Week 4**: User authentication
5. **Week 5**: Advanced features (search, API)

This pathway provides a structured approach to transforming a static website into a fully functional web application, introducing students to important concepts in modern web development including server-side programming, databases, and user authentication.
