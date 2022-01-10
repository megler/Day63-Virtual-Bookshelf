from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Book(FlaskForm):
    book_name = StringField(label='Book Name', validators=[DataRequired()])
    book_author = StringField(label='Book Author', validators=[DataRequired()])
    book_rating = StringField(label='Book Rating', validators=[DataRequired()])
    submit = SubmitField(label="Submit")