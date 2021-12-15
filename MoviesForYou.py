from flask import Flask, render_template, url_for, flash, redirect, request
# from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, InputUser, AddToWatchlist
from api_calls import SortingAPI
from authenticate import Authenticate
from db_connection_take_2 import register_new_user, authenticate_user, get_movies_watched, insert_movie_watched, find_id, \
    lookup_username
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
    global login_success, current_username
    if login_success:
        logged_in_status = f"Logged in as {current_username}"
    else:
        logged_in_status = "Not logged in"
    return render_template('home.html', posts=posts, logged_in_status=logged_in_status)


@app.route("/what_to_watch", methods=['GET', 'POST'])
def what_to_watch():
    try:
        global login_success, current_username
        if login_success:
            logged_in_status = f"Logged in as {current_username}"
        else:
            logged_in_status = "Not logged in"
        form = InputUser()
        if not form.rating.data:
            raise Exception

    except:
        return render_template('what_to_watch.html', title='What To Watch', form=form, logged_in_status=logged_in_status)

    else:
        auth = Authenticate(form.rating.data, form.genre.data, form.run_time.data)
        genre_result = auth.genres()
        age_rating_result = auth.age_ratings()
        runtime_result = auth.lower_runtime()
        genre_error = auth.genre_message()
        age_rating_error = auth.age_rating_message()
        runtime_error = auth.runtime_message()

        result = SortingAPI(form.rating.data, form.genre.data, form.run_time.data)
        result.sorting_data()
        results = result.displaying_data()

        add_to_watchlist = AddToWatchlist()

        global current_film_id, current_film_name, current_film_detail, current_film_poster
        current_film_id = results[0]["ID"]
        current_film_name = results[0]["Name"]
        current_film_detail = results[0]["Description"]
        current_film_poster = results[0]["Poster"]

        if not genre_result and not age_rating_result and not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   age_rating_error=age_rating_error, runtime_error=runtime_error, results=results[0],
                                   add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
        elif not genre_result and not age_rating_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   age_rating_error=age_rating_error, results=results[0],
                                   add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
        elif not age_rating_result and not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form,
                                   age_rating_error=age_rating_error, runtime_error=runtime_error, results=results[0],
                                   add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
        elif not genre_result and not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   runtime_error=runtime_error, results=results[0], add_to_watchlist=add_to_watchlist,
                                   logged_in_status=logged_in_status)
        elif not genre_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                                   results=results[0], add_to_watchlist=add_to_watchlist,
                                   logged_in_status=logged_in_status)
        elif not age_rating_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form,
                                   age_rating_error=age_rating_error, results=results[0],
                                   add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
        elif not runtime_result:
            return render_template('what_to_watch.html', title='What To Watch', form=form, runtime_error=runtime_error,
                                   results=results[0], add_to_watchlist=add_to_watchlist,
                                   logged_in_status=logged_in_status)
        else:
            return render_template('what_to_watch.html', title='What To Watch', form=form, results=results[0],
                                   add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)


@app.route("/adding_to_watchlist", methods=['GET', 'POST'])
def adding_to_watchlist():
    if login_success:
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/watchlist")
def watchlist():
    global login_success, current_username, user_id
    if login_success:
        logged_in_status = f"Logged in as {current_username}"
        films = get_movies_watched(user_id)
        if not films:
            flash('Your watchlist is currently empty, add films here', 'warning')
            return redirect(url_for('what_to_watch'))
        else:
            return render_template('watchlist.html', title='Watchlist', films=films, logged_in_status=logged_in_status)

    else:
        flash(f'Login to view your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    global login_success, current_username
    if login_success:
        logged_in_status = f"Logged in as {current_username}"
    else:
        logged_in_status = "Not logged in"
    form = RegistrationForm()
    username_doesnt_exist = lookup_username(form.username.data)
    if not username_doesnt_exist:
        message = f"{form.username.data} is already taken, try another username"
        return render_template('register.html', title='Register', form=form, logged_in_status=logged_in_status,
                               message=message)
    else:
        if form.validate_on_submit():
            register_new_user(form.username.data, form.password.data)
            flash(f'Account has successfully been created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form, logged_in_status=logged_in_status)


@app.route("/login", methods=['GET', 'POST'])
def login():
    global login_success, current_username, user_id
    if login_success:
        logged_in_status = f"Logged in as {current_username}"
    else:
        logged_in_status = "Not logged in"
    form = LoginForm()

    if form.validate_on_submit():
        info = authenticate_user(form.username.data, form.password.data)
        if info:
            login_success = True
            user_id = find_id(form.username.data)
            current_username = form.username.data
            flash(f'Account has successfully been logged in for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f"A user with that information doesn't exist, please try again", "warning")
    return render_template('login.html', title='Login', form=form, logged_in_status=logged_in_status)

@app.route("/logout")
def logout():
    global login_success, current_username
    login_success = False
    flash(f'You have been logged out from {current_username}', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    global login_success
    login_success = False
    app.run(debug=True)
