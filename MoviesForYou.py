from flask import Flask, render_template, url_for, flash, redirect, flash
# from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, InputUser
from api_calls import SortingAPI
app = Flask(__name__)

app.config["SECRET_KEY"] = 'caf68d5a247e7d1c5c7fb2e44b1c258c'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# db = SQLAlchemy(app)

# class Users:
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(55), unique=True, nullalbe=False)
#    email = db.Column(db.String(55), unique=True, nullalbe=False)
#    password = db.Column(db.String(55), unique=True, nullalbe=False)


posts = [
    {
        "name": "Saamiya",
        "about_me": "I love the feeling I get when I watch a film. I probably have seen 1000 over my life!",
        "fav_movie": "Avenger's Endgame"
    },
    {
        "name": "Annie",
        "about_me": "A great soundtrack to a great film is a match made in heaven.",
        "fav_movie": "High School Musical"
    },
    {
        "name": "Lizzie",
        "about_me": "I feel like a kid again when I go to the movies!",
        "fav_movie": "Cats and Dogs"
    },
    {
        "name": "Lowena",
        "about_me": "The most fun I have is when I watch a good film.",
        "fav_movie": "Chicago"
    },
    {
        "name": "Maebh",
        "about_me": "A great film gets you talking even after it's over.",
        "fav_movie": "Sharknado"
    },
    {
        "name": "Luciana",
        "about_me": "A movie where the family can enjoy is right up my street.",
        "fav_movie": "The Ring"
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/what_to_watch", methods=['GET', 'POST'])
def what_to_watch():
    form = InputUser()
    data = SortingAPI(form.rating.data, form.genre.data, form.run_time.data, form.number_of_results, form.keywords)
    data.sorting_data()

    results = data.displaying_data()
    try:
        if int(form.number_of_results.data) == 3:
            return render_template('what_to_watch_3_results.html', title='What To Watch', form=form,
                                   results=[results[0], results[1], results[2]])
        elif int(form.number_of_results.data) == 5:
            return render_template('what_to_watch_5_results.html', title='What To Watch', form=form,
                                   results=[results[0], results[1], results[2], results[3], results[4]])
        else:
            return render_template('what_to_watch_10_results.html', title='What To Watch', form=form,
                                   results=[results[0], results[1], results[2], results[3], results[4],
                                            results[5], results[6], results[7], results[8], results[9]])
    except:
        try:
            return render_template('what_to_watch.html', title='What To Watch', form=form, results=results[0])
        except:
            flash(u'No films could be found with that criteria.', 'error')
            return redirect(url_for('what_to_watch'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account has successfully been created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
