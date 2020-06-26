  
import os
from flask import Flask, render_template, request, flash ,redirect ,url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tasty'
app.config["MONGO_URI"] = 'mongodb+srv://sree:sreeUser@tasty-mq6mv.mongodb.net/tasty?retryWrites=true&w=majority'

mongo = PyMongo(app)

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

# -----Add Recipe------
@app.route('/add_recipe')
def add_recipe():
    return render_template('add recipe.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True,
    )