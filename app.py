import os
import random
from flask import Flask

app = Flask(__name__)

# Predefined color codes
COLOR_CODES = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "orange": "#e67e22",
    "gray": "#30336b",
    "pink": "#be2edd",
    "darkBlue": "#130f40"
}

 
selected_color_name = os.getenv("APP_COLOR", random.choice(list(COLOR_CODES.keys())))
selected_color_code = COLOR_CODES[selected_color_name]

@app.route("/")
def home():
    return f"<h1 style='color:{selected_color_code}'>Hello, Sonal! Your Flask app is running with {selected_color_name} theme 🎨</h1>"

if __name__ == "__main__":
    app.run(debug=True)
