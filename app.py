from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Sonal! Your Flask app is running 🎉"

if __name__ == '__main__':
    app.run(debug=True)
