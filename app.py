from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet, PetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, RadioField

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask-adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config["SECRET_KEY"] = "keyyyy"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def show_pet_listing():

    pets = Pet.query.all()

    return render_template("pet-list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def show_add_pet_form():
    """show add pet form"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}!!!!!!")

        return redirect("/")

    else:

        return render_template("add-pet-form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_page(pet_id):
    """show pet page"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

    return render_template("display-pet.html", pet=pet, form=form)
