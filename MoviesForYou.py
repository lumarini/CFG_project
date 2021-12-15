from flask import Flask, render_template, url_for, flash, redirect  # <------ import Flask
from forms import RegistrationForm, LoginForm, InputUser, AddToWatchlist
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
        if not form.genre.data:
            # if form not completed, return page display without results
            raise Exception
    except:
        return render_template('what_to_watch.html', title='What To Watch', form=form,
                               logged_in_status=logged_in_status)

    else:
        return display_results(form, logged_in_status)


@app.route("/adding_to_watchlist_button_1", methods=['GET', 'POST'])
def adding_to_watchlist_button_1():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[0]]["ID"]
        current_film_name = results[count_list[0]]["Name"]
        current_film_detail = results[count_list[0]]["Description"]
        current_film_poster = results[count_list[0]]["Poster"]

        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_2", methods=['GET', 'POST'])
def adding_to_watchlist_button_2():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[1]]["ID"]
        current_film_name = results[count_list[1]]["Name"]
        current_film_detail = results[count_list[1]]["Description"]
        current_film_poster = results[count_list[1]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_3", methods=['GET', 'POST'])
def adding_to_watchlist_button_3():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[2]]["ID"]
        current_film_name = results[count_list[2]]["Name"]
        current_film_detail = results[count_list[2]]["Description"]
        current_film_poster = results[count_list[2]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_4", methods=['GET', 'POST'])
def adding_to_watchlist_button_4():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[3]]["ID"]
        current_film_name = results[count_list[3]]["Name"]
        current_film_detail = results[count_list[3]]["Description"]
        current_film_poster = results[count_list[3]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_5", methods=['GET', 'POST'])
def adding_to_watchlist_button_5():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[4]]["ID"]
        current_film_name = results[count_list[4]]["Name"]
        current_film_detail = results[count_list[4]]["Description"]
        current_film_poster = results[count_list[4]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_6", methods=['GET', 'POST'])
def adding_to_watchlist_button_6():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[5]]["ID"]
        current_film_name = results[count_list[5]]["Name"]
        current_film_detail = results[count_list[5]]["Description"]
        current_film_poster = results[count_list[5]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_7", methods=['GET', 'POST'])
def adding_to_watchlist_button_7():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[6]]["ID"]
        current_film_name = results[count_list[6]]["Name"]
        current_film_detail = results[count_list[6]]["Description"]
        current_film_poster = results[count_list[6]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_8", methods=['GET', 'POST'])
def adding_to_watchlist_button_8():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[7]]["ID"]
        current_film_name = results[count_list[7]]["Name"]
        current_film_detail = results[count_list[7]]["Description"]
        current_film_poster = results[count_list[7]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_9", methods=['GET', 'POST'])
def adding_to_watchlist_button_9():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[8]]["ID"]
        current_film_name = results[count_list[8]]["Name"]
        current_film_detail = results[count_list[8]]["Description"]
        current_film_poster = results[count_list[8]]["Poster"]
        insert_movie_watched(user_id, current_film_id, current_film_name, current_film_detail, current_film_poster)
        flash(f'{current_film_name} has successfully been added to watchlist!', 'success')
        return redirect(url_for('what_to_watch'))
    else:
        # if not logged in redirect to login page
        flash(f'Login to add films to your watchlist', 'warning')
        return redirect(url_for('login'))


@app.route("/adding_to_watchlist_button_10", methods=['GET', 'POST'])
def adding_to_watchlist_button_10():
    if login_success:
        # if logged in , add film to watchlist
        global current_film_id, current_film_name, user_id, current_film_detail, current_film_poster, count_list, \
            results
        current_film_id = results[count_list[9]]["ID"]
        current_film_name = results[count_list[9]]["Name"]
        current_film_detail = results[count_list[9]]["Description"]
        current_film_poster = results[count_list[9]]["Poster"]
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
    global results, login_success, user_id, count_list
    # info is checked to see if it matches any of the available options
    auth = Authenticate(form.rating.data, form.genre.data, form.lower_run_time.data, form.upper_run_time.data)
    genre_result = auth.genres()
    age_rating_result = auth.age_ratings()
    lower_runtime_result = auth.lower_runtime()
    upper_runtime_result = auth.upper_runtime()
    genre_error = auth.genre_message()
    age_rating_error = auth.age_rating_message()
    lower_runtime_error = auth.lower_runtime_message()
    upper_runtime_error = auth.upper_runtime_message()
    result = DisplayingAPI(form.rating.data, form.genre.data, form.lower_run_time.data, form.upper_run_time.data,
                           form.keywords.data)
    results = result.displaying_data()
    keywords = True
    no_keyword_message = ""
    print("hi")
    print(results)
    print("hi")
    print(len(results))
    if not results and form.keywords.data:
        result = DisplayingAPI(form.rating.data, form.genre.data, form.lower_run_time.data, form.lower_run_time.data,
                               "")
        results = result.displaying_data()
        keywords = False
        no_keyword_message = "There were no results with those keywords, here are some excluding them"
        if not results:
            no_result_message = "There are no results for those options"
            return render_template('what_to_watch.html', title='What To Watch', form=form,
                           logged_in_status=logged_in_status, no_result_message=no_result_message)
    elif not results:
        no_result_message = "There are no results for those options"
        return render_template('what_to_watch.html', title='What To Watch', form=form,
                           logged_in_status=logged_in_status, no_result_message=no_result_message)
    add_to_watchlist = AddToWatchlist()
    if login_success:
        films_watched = check_movies_watched(user_id)
        count_list = []
        count = 0
        if len(results) < 3:
            count = check_films(films_watched, results, count)
            count_list.append(count)
        elif int(form.number_of_results.data) == 10 and len(results) >= 10:
            while len(count_list) < 10:
                if count == len(results):
                    break
                count = check_films(films_watched, results, count)
                count_list.append(count)
                count = count + 1

        elif (int(form.number_of_results.data) == 5 and len(results) >= 5) or (int(form.number_of_results.data) == 10
                                                                               and len(results) >= 5):
            while len(count_list) < 5:
                if count == len(results):
                    break
                count = check_films(films_watched, results, count)
                count_list.append(count)
                count = count + 1

        elif (int(form.number_of_results.data) == 3 and len(results) >= 3) or (int(form.number_of_results.data) == 10
                                                                               and len(results) >= 3) or (
                int(form.number_of_results.data) == 5 and len(results) >= 3):
            while len(count_list) < 3:
                if count == len(results):
                    break
                count = check_films(films_watched, results, count)
                count_list.append(count)
                count = count + 1

    else:
        if len(results) < 3:
            count_list = [0]

        elif int(form.number_of_results.data) == 10 and len(results) >= 10:
            count_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        elif (int(form.number_of_results.data) == 5 and len(results) >= 5) or (int(form.number_of_results.data) == 10
                                                                               and len(results) >= 5):
            count_list = [0, 1, 2, 3, 4]

        elif (int(form.number_of_results.data) == 3 and len(results) >= 3) or (int(form.number_of_results.data) == 10
                                                                               and len(results) >= 3) or (
                int(form.number_of_results.data) == 5 and len(results) >= 3):
            count_list = [0, 1, 2]

    result_list = []
    count = 0
    print(len(count_list))
    print(form.number_of_results.data)

    if len(count_list) == 3:
        while len(result_list) < 3:
            result_list.append(results[count_list[count]])
            count = count + 1
        page = 'what_to_watch_3_results.html'
    elif len(count_list) == 5:
        while len(result_list) < 5:
            result_list.append(results[count_list[count]])
            count = count + 1
        page = 'what_to_watch_5_results.html'
    elif len(count_list) == 10:
        while len(result_list) < 10:
            result_list.append(results[count_list[count]])
            count = count + 1
        page = 'what_to_watch_10_results.html'
    else:
        result_list.append(results[count_list[count]])
        page = 'what_to_watch_1_results.html'

    if not result_list:
        no_result_message = "There are no results for those options"
        return render_template('what_to_watch.html', title='What To Watch', form=form,
                               logged_in_status=logged_in_status, no_result_message=no_result_message)
    elif len(result_list) < 3:
        page = 'what_to_watch_1_results.html'

    different_result_message = ""
    if len(result_list) != int(form.number_of_results.data):
        different_result_message = f"This search didn't produce {int(form.number_of_results.data)} results, here are " \
                                   f"the available ones"
    # if any of the info provided doesn't match the available options, the relevant error message iis shown, along with
    # the results which aren't filtered by the incorrect info
    return render_template(page, title='What To Watch', form=form, result_list=result_list, genre_error=genre_error,
                           age_rating_error=age_rating_error, lower_runtime_error=lower_runtime_error,
                           upper_runtime_error=upper_runtime_error, add_to_watchlist=add_to_watchlist,
                           logged_in_status=logged_in_status, no_keyword_message=no_keyword_message,
                           different_result_message=different_result_message)


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
