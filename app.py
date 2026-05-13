from flask import Flask, render_template

app = Flask(__name__)

ice_creams = [
    {"name": "Chocolate Delight", "price": "₹120", "image": "🍫"},
    {"name": "Vanilla Dream", "price": "₹100", "image": "🍦"},
    {"name": "Strawberry Blast", "price": "₹130", "image": "🍓"},
    {"name": "Mango Magic", "price": "₹140", "image": "🥭"},
]

@app.route("/")
def home():
    return render_template("index.html", ice_creams=ice_creams)

if __name__ == "__main__":
    app.run(debug=True)
