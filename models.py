from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

db = SQLAlchemy()
default_img_url = "https://images.unsplash.com/photo-1580329503754-35ddb65d49a8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"


def connect_db(app):
    """connects to database!"""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.Text(), default=default_img_url)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text())
    available = db.Column(db.Boolean, default=True)


class AddPetForm(FlaskForm):

    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[InputRequired(), URL()])
    age = FloatField("Age", validators=[NumberRange(min=0.1, max=130, message="your pet must be 0-130")])
    notes = TextAreaField("Notes about pet", validators=[Optional()])

