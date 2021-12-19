from flask_wtf import FlaskForm  # <------ import Flask-WTF
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Optional


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
    genre = StringField("What genre of film are you interested in? (Action, Adventure, Animation, Comedy, Crime, "
                        "Documentary, Drama, Family, Fantasy, History, Horror, Music, Romance, Science Fiction, "
                        "TV Movie, Thriller, War, Western)", validators=[DataRequired()])
    lower_run_time = IntegerField("What is the minimum length of the film? (in minutes)", validators=[Optional()])
    upper_run_time = IntegerField("What is the maximum length of the film? (in minutes)", validators=[Optional()])
    rating = StringField("What age rating do you prefer? (U, PG, 12, 12A, 15, 18, R18)", validators=[Optional()])
    keywords = StringField("Enter any keywords", validators=[Optional(), Length(max=200)])
    number_of_results = SelectField("Return how many results", choices=["3", "5", "10"], validate_choice=True)
    submit = SubmitField("Enter your choices!")


class AddToWatchlist(FlaskForm):
    submit = SubmitField("Add to Watchlist")
