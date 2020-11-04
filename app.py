import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/lolas_cookbook")
def lolas_cookbook():
    return render_template("index.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/get_mealplanner")
def get_mealplanner():
    mealplanner = list(mongo.db.mealplanner.find())
    return render_template("mealplanner.html", mealplanner=mealplanner)


@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipes = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "family_story": request.form.get("family_story"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "cooking_instruction": request.form.get("cooking_instruction"),
        }
        mongo.db.recipes.insert_one(recipes)
        flash("Your recipe is succesfully added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipes.html", categories=categories)


@app.route("/edit_recipes/<recipes_id>", methods=["GET", "POST"])
def edit_recipes(recipes_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "family_story": request.form.get("family_story"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "cooking_instruction": request.form.get("cooking_instruction"),
            "recipe_day": request.form.get("recipe_day")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipes_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipes.html", recipes=recipes, categories=categories)


@app.route("/add_mealplanner", methods=["GET", "POST"])
def add_mealplanner():
    if request.method == "POST":
        mealplanner = {
            "recipe_name": request.form.get("recipe_name"),

            "recipe_day": request.form.get("recipe_day")
        }
        mongo.db.recipes.insert_one(recipe_name)
        flash("Your recipe is succesfully added to your mealplanner")
        return redirect(url_for("get_mealplanner"))

    recipes = mongo.db.recipes.find().sort("recipe_name", 1)
    return render_template("add_mealplanner.html", recipes=recipes)


@app.route("/delete_recipes/<recipes_id>")
def delete_recipes(recipes_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipes_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)