from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=6, max=12)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=12)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password"), Length(
        min=6, max=12)])
    submit = SubmitField("Sign Up!")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=6, max=12)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=12)])
    remember_me = BooleanField("Remember Me!")
    submit = SubmitField("Login")


class InputUser(FlaskForm):
    genre = StringField("What genre of film are you interested in?", validators=[DataRequired()])
    run_time = StringField("How long is the film?", validators=[DataRequired()])
    rating = StringField("What age rating do you prefer?", validators=[DataRequired()])
    submit = SubmitField("Enter your choices!")


class AddToWatchlist(FlaskForm):
    submit = SubmitField("Add to Watchlist")
