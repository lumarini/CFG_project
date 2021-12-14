from flask import Flask, render_template, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, InputUser
from api_calls import SortingAPI
from authenticate import Authenticate
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

def return_true():
    return True

def return_false():
    return False

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/what_to_watch", methods=['GET', 'POST'])
def what_to_watch():
    try:
        form = InputUser()
        if not form.rating.data:
            raise Exception

    except:
        return render_template('what_to_watch.html', title='What To Watch', form=form)

    else:
        auth = Authenticate(form.rating.data, form.genre.data, form.run_time.data)
        genre_result = auth.genres()
        age_rating_result = auth.age_ratings()
        runtime_result = auth.lower_runtime()
        genre_error = auth.genre_message()
        age_rating_error = auth.age_rating_message()
        runtime_error = auth.runtime_message()
        results = [{"Name": "", "Descriptions": "",
                    "Poster": "https://cdn.schoolstickers.com/products/en/819/10MM_SMILE-02.png"}]
        if not genre_result and not age_rating_result and not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   age_rating_error=age_rating_error, runtime_error=runtime_error, results=results[0])
        elif not genre_result and not age_rating_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   age_rating_error=age_rating_error, results=results[0])
        elif not age_rating_result and not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form,
                                   age_rating_error=age_rating_error, runtime_error=runtime_error, results=results[0])
        elif not genre_result and not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   runtime_error=runtime_error, results=results[0])
        elif not genre_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   results=results[0])
        elif not age_rating_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form,
                                   age_rating_error=age_rating_error, results=results[0])
        elif not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, runtime_error=runtime_error,
                                   results=results[0])
        else:
            result = SortingAPI(form.rating.data, form.genre.data, form.run_time.data)
            result.sorting_data()
            results = result.displaying_data()
            if form.rating.data and genre_result and age_rating_result and runtime_result:
                print(form.rating.data)
                print(results)
                print(genre_result)
                print(runtime_result)
                print(age_rating_result)
                return render_template('what_to_watch.html', title='What To Watch', form=form, results=results[0])


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
