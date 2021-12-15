from flask import Flask, render_template, url_for, flash, redirect  # <------ import Flask
from forms_version_2 import RegistrationForm, LoginForm, InputUser, AddToWatchlist
from database.db_connection import register_new_user, authenticate_user, get_movies_watched, insert_movie_watched, \
    find_id, lookup_username, check_movies_watched
from post_info import posts
from reccomendation.api_calls import DisplayingAPI
from reccomendation.authenticate import Authenticate

app = Flask(__name__)

app.config["SECRET_KEY"] = 'caf68d5a247e7d1c5c7fb2e44b1c258c'


def return_true():
    return True


def return_false():
    return False


########################################################################################################################
########################################################################################################################
# APP ROUTES


@app.route("/")
@app.route("/home")
def home():
    global login_success, current_username
    logged_in_status = check_login_success(login_success)
    return render_template('home.html', posts=posts, logged_in_status=logged_in_status)


@app.route("/what_to_watch", methods=['GET', 'POST'])
def what_to_watch():
    try:
        global login_success, current_username, user_id
        logged_in_status = check_login_success(login_success)
        form = InputUser()
        if not form.rating.data:
            # if form not completed, return page display without results
            raise Exception
    except:
        return render_template('what_to_watch.html', title='What To Watch', form=form,
                               logged_in_status=logged_in_status)

    else:
        return display_results(form, logged_in_status)


@app.route("/adding_to_watchlist", methods=['GET', 'POST'])
def adding_to_watchlist():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/watchlist")
def watchlist():
    global login_success, current_username, user_id
    if login_success:
        # if logged in display films in their watchlist
        logged_in_status = f"Logged in as {current_username}"
        films = get_movies_watched(user_id)
        if not films:
            flash('Your watchlist is currently empty, add films here', 'warning')
            return redirect(url_for('what_to_watch'))
        else:
            return render_template('watchlist.html', title='Watchlist', films=films, logged_in_status=logged_in_status)

    else:
        # if not logged in redirect to login page
        flash(f'Login to view your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    global login_success, current_username
    logged_in_status = check_login_success(login_success)
    form = RegistrationForm()
    username_doesnt_exist = lookup_username(form.username.data)
    if not username_doesnt_exist:
        # if username already exists, prompts to try another one
        message = f"{form.username.data} is already taken, try another username"
        return render_template('register.html', title='Register', form=form, logged_in_status=logged_in_status,
                               message=message)
    else:
        # if username doesn't already exist, creates account with details provided
        if form.validate_on_submit():
            register_new_user(form.username.data, form.password.data)
            flash(f'Account has successfully been created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form, logged_in_status=logged_in_status)


@app.route("/login", methods=['GET', 'POST'])
def login():
    global login_success, current_username, user_id
    logged_in_status = check_login_success(login_success)
    form = LoginForm()
    if form.validate_on_submit():
        info = authenticate_user(form.username.data, form.password.data)
        if info:
            # if info provided is correct, user is logged in
            login_success = True
            user_id = find_id(form.username.data)
            current_username = form.username.data
            flash(f'Account has successfully been logged in for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            # if info provided is incorrect, user is prompted to try again
            flash(f"A user with that information doesn't exist, please try again", "warning")
    return render_template('login.html', title='Login', form=form, logged_in_status=logged_in_status)


@app.route("/logout")
def logout():
    # user is logged out
    global login_success, current_username
    login_success = False
    flash(f'You have been logged out from {current_username}', 'success')
    return redirect(url_for('home'))


########################################################################################################################
########################################################################################################################
# FUNCTIONS

def display_results(form, logged_in_status):
    # info is checked to see if it matches any of the available options
    auth = Authenticate(form.rating.data, form.genre.data, form.run_time.data)
    genre_result = auth.genres()
    age_rating_result = auth.age_ratings()
    runtime_result = auth.lower_runtime()
    genre_error = auth.genre_message()
    age_rating_error = auth.age_rating_message()
    runtime_error = auth.runtime_message()

    result = DisplayingAPI(form.rating.data, form.genre.data, form.run_time.data)
    results = result.displaying_data()

    add_to_watchlist = AddToWatchlist()
    global login_success, user_id
    if login_success:
        films_watched = check_movies_watched(user_id)
        print(films_watched)
        count = check_films(films_watched, results, 0)

        global current_film_id, current_film_name, current_film_detail, current_film_poster
        current_film_id = results[count]["ID"]
        current_film_name = results[count]["Name"]
        current_film_detail = results[count]["Description"]
        current_film_poster = results[count]["Poster"]
    else:
        count = 0

    # if any of the info provided doesn't match the available options, the relevant error message iis shown, along with
    # the results which aren't filtered by the incorrect info
    if not genre_result and not age_rating_result and not runtime_result:
        return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                               age_rating_error=age_rating_error, runtime_error=runtime_error, results=results[count],
                               add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
    elif not genre_result and not age_rating_result:
        return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                               age_rating_error=age_rating_error, results=results[count],
                               add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
    elif not age_rating_result and not runtime_result:
        return render_template('what_to_watch.html', title='What To Watch', form=form,
                               age_rating_error=age_rating_error, runtime_error=runtime_error, results=results[count],
                               add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
    elif not genre_result and not runtime_result:
        return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                               runtime_error=runtime_error, results=results[count], add_to_watchlist=add_to_watchlist,
                               logged_in_status=logged_in_status)
    elif not genre_result:
        return render_template('what_to_watch.html', title='What To Watch', form=form, genre_error=genre_error,
                               results=results[count], add_to_watchlist=add_to_watchlist,
                               logged_in_status=logged_in_status)
    elif not age_rating_result:
        return render_template('what_to_watch.html', title='What To Watch', form=form,
                               age_rating_error=age_rating_error, results=results[count],
                               add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)
    elif not runtime_result:
        return render_template('what_to_watch.html', title='What To Watch', form=form, runtime_error=runtime_error,
                               results=results[count], add_to_watchlist=add_to_watchlist,
                               logged_in_status=logged_in_status)
    else:
        return render_template('what_to_watch.html', title='What To Watch', form=form, results=results[count],
                               add_to_watchlist=add_to_watchlist, logged_in_status=logged_in_status)


def check_login_success(this_login_success):
    if this_login_success:
        global current_username
        logged_in_status = f"Logged in as {current_username}"
    else:
        logged_in_status = "Not logged in"
    return logged_in_status


def check_films(films, results, count):
    for film in films:
        if film == results[count]["ID"]:
            count = count + 1
            check_films(films, results, count)
    return count


if __name__ == '__main__':
    global login_success
    login_success = False
    app.run(debug=True)
