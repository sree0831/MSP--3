  
import os
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/menu')
def menu():
    return render_template("menu.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your reservation!".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")


@app.route('/recipes')
def recipes():
    return render_template("recipes.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True,
    )