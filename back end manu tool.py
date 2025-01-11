from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Example menu data
menu = [
    {"name": "Chicken Burger", "type": "Fast Food", "diet": "Non-Vegetarian"},
    {"name": "Veggie Salad", "type": "Healthy", "diet": "Vegetarian"},
    {"name": "Pasta Alfredo", "type": "Italian", "diet": "Vegetarian"},
    {"name": "Spicy Tacos", "type": "Mexican", "diet": "Non-Vegetarian"},
    {"name": "Fruit Smoothie", "type": "Healthy", "diet": "Vegan"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    preferences = request.form
    diet = preferences.get('diet')
    meal_type = preferences.get('type')
    
    # Filter menu based on preferences
    filtered_menu = [item for item in menu if (diet in item["diet"] and meal_type in item["type"])]
    suggestion = random.choice(filtered_menu) if filtered_menu else "No matching menu items found!"
    return {"suggestion": suggestion}

if __name__ == "__main__":
    app.run(debug=True)
