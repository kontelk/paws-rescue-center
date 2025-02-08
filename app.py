"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
app = Flask(__name__)

"""1. Add a View Function for the Home page."""
@app.route("/")
def home():
    home_output_text = 'Paws Rescue Center 🐾'
    return home_output_text

"""2. Add a View Function for the About page."""
@app.route("/about")
def learn():
    about_output_text = 'We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology "adopt, don\'t hop"!'
    return about_output_text


if __name__ == "__main__":
    """ """
    app.run(debug=True, host="0.0.0.0", port=3000)
