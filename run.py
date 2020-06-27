  
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


@app.route('/recipes')
def recipes():
    return render_template("recipes.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your reservation!".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")



#------add recipe------
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

# -----recipes page---

@app.route('/recipes')
@app.route('/get_recipes')
def get_recipes():
    if (request.args.get('recipe_name') is not None 
    or request.args.get('preparation_time') is not None): 
    
        recipename = None
        preparationtime = None
        
        
        if request.args.get('recipe_name') is not None and request.args.get('recipe_name') is not '':
            recipenameregex = "\W*"+request.args.get("recipe_name")+"\W*"
            recipename = re.compile(recipenameregex, re.IGNORECASE)
          
        if request.args.get('preparation_time') is not None and request.args.get('preparation_time') is not '':
            preparationtimeregex = "\W*"+request.args.get("preparation_time")+"\W*"
            preparationtime = re.compile(preparationtimeregex, re.IGNORECASE)
        
        
            

        recipes=mongo.db.recipes.find( { "$or": [{"recipe_name": recipename}, {"preparation_time": preparationtime}] } )
        return render_template("recipes.html", recipes=recipes, ) 
        
    return render_template("recipes.html", recipes=mongo.db.recipes.find(),) 
    

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True,
    )