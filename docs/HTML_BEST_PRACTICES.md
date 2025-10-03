# HTML Best Practices for Year 12 Software Engineering Students

This document outlines the HTML best practices implemented in this project to make it more beginner-friendly, accessible, and maintainable. These practices will help you transition from static HTML to dynamic Flask templates.

## Semantic HTML Elements

### What We Used
- `<header>`, `<main>`, `<footer>` for page structure
- `<nav>` for navigation menus
- `<article>` for self-contained content (recipe cards)
- `<section>` for thematic grouping of content
- `<figure>` and `<figcaption>` for images with captions

### Why It Matters
- Improves accessibility for screen readers
- Makes code more readable and maintainable
- Provides clearer structure for CSS styling
- Prepares for easier Flask template conversion

### Example
```html
<!-- Before -->
<div class="content">
  <div class="card">
    <p class="category">Main Course</p>
    <h3><a href="#">Adobo</a></h3>
    <p>Description text...</p>
  </div>
</div>

<!-- After -->
<main class="content">
  <article class="card">
    <header class="card-header">
      <p class="category">Main Course</p>
      <h3><a href="#">Adobo</a></h3>
    </header>
    <div class="card-body">
      <p>Description text...</p>
    </div>
  </article>
</main>
```

## Accessibility Improvements

### What We Added
- ARIA roles (`role="banner"`, `role="main"`, `role="contentinfo"`)
- ARIA attributes (`aria-label`, `aria-required`, `aria-expanded`)
- Improved alt text for images
- Keyboard navigation support
- Screen reader only text (`sr-only` class)

### Why It Matters
- Makes content accessible to users with disabilities
- Improves navigation for keyboard-only users
- Provides context for screen readers
- Follows web accessibility standards (WCAG)

### Example
```html
<!-- Before -->
<div class="nav-toggle">&#9776;</div>

<!-- After -->
<div class="nav-toggle" 
     aria-label="Toggle navigation menu" 
     role="button" 
     tabindex="0" 
     aria-expanded="false">&#9776;</div>
```

## HTML5 Form Validation

### What We Added
- Input validation attributes (`required`, `minlength`, `maxlength`)
- Descriptive placeholders
- Helper text for form fields
- Proper label associations
- Appropriate input types

### Why It Matters
- Provides immediate feedback to users
- Reduces server-side validation burden
- Improves user experience
- Demonstrates HTML5 validation capabilities

### Example
```html
<!-- Before -->
<div class="form-group">
  <label for="recipe-name">Recipe Name:</label>
  <input type="text" id="recipe-name" name="recipe-name" required>
</div>

<!-- After -->
<div class="form-group">
  <label for="recipe-name">Recipe Name:</label>
  <input type="text" id="recipe-name" name="recipe-name" 
         required minlength="3" maxlength="50" 
         aria-required="true" 
         placeholder="Enter recipe name (3-50 characters)">
  <span class="form-hint">Required. Enter 3-50 characters.</span>
</div>
```

## Data Attributes for JavaScript Integration

### What We Added
- `data-category` for recipe categorization
- `data-recipe-id` for unique identification
- Other data attributes for metadata

### Why It Matters
- Provides hooks for JavaScript functionality
- Stores metadata directly in HTML
- Facilitates dynamic filtering and sorting
- Prepares for Flask/JavaScript integration

### Example
```html
<!-- Before -->
<div class="card">
  <p class="category">Dessert</p>
  <h3><a href="#" class="recipe-link">Leche Flan</a></h3>
  <p class="recipe-short-des">Description text...</p>
</div>

<!-- After -->
<article class="card" data-category="Dessert" data-recipe-id="12">
  <header class="card-header">
    <p class="category">Dessert</p>
    <h3><a href="#" class="recipe-link">Leche Flan</a></h3>
  </header>
  <div class="card-body">
    <p class="recipe-short-des">Description text...</p>
  </div>
</article>
```

## Comprehensive Comments

### What We Added
- Section-level comments
- Component-level comments
- Purpose explanations
- Educational notes

### Why It Matters
- Improves code readability
- Helps beginners understand code structure
- Documents design decisions
- Makes maintenance easier

### Example
```html
<!-- Before -->
<div class="form-group">
  <label for="ingredients">Ingredients:</label>
  <textarea id="ingredients" name="ingredients" rows="5" required></textarea>
</div>

<!-- After -->
<!-- Ingredients Input - Textarea for list of ingredients -->
<div class="form-group">
  <label for="ingredients">Ingredients:</label>
  <textarea id="ingredients" name="ingredients" rows="5" 
            required aria-required="true"
            placeholder="Enter ingredients, one per line"></textarea>
  <span class="form-hint">Required. List each ingredient on a new line.</span>
</div>
```

## Preparing for Flask Integration

These HTML improvements make the transition to Flask templates easier:

1. **Consistent Component Structure**: Components like recipe cards have a consistent structure that can be converted to Flask macros or template includes

2. **Data Attributes**: Already set up to receive dynamic data from Flask routes

3. **Form Structure**: Ready for Flask-WTF integration with validation attributes in place

4. **Semantic Structure**: Clear separation of concerns makes it easier to identify which parts should be in base templates vs. content templates

## Next Steps for Students

1. Study the improved HTML structure and understand the purpose of each change
2. Practice creating similar semantic structures in your own projects
3. Experiment with HTML5 form validation
4. Learn how these elements will map to Flask templates
5. Refer to the FLASK_PATHWAY.md document for guidance on converting to a Flask application
