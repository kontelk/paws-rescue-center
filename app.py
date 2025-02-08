from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Paws Rescue Center 🐾"

@app.route("/about")
def learn():
    about_text = """ We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology "adopt, don't hop"! """
    return about_text

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
