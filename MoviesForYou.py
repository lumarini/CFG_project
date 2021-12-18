from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, Input_User
app = Flask(__name__)

app.config["SECRET_KEY"] = 'caf68d5a247e7d1c5c7fb2e44b1c258c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


# class Users:
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(55), unique=True, nullalbe=False)
#    email = db.Column(db.String(55), unique=True, nullalbe=False)
#    password = db.Column(db.String(55), unique=True, nullalbe=False)


posts = [ 
    {
        "name": "Saamiya",
        "about_me": "Cat-lover and web dev whiz",
        "fav_movie": "Avenger's Endgame"
    },
    {
        "name": "Luciana",
        "about_me": "full-stack whiz kid",
        "fav_movie": "The Ring"
    },
    {
        "name": "Lizzie",
        "about_me": "book collector",
        "fav_movie": "Cats and Dogs"
    },
    {
        "name": "Lowena",
        "about_me": "voracious reader, coffee addict",
        "fav_movie": "Chicago"
    },
    {
        "name": "Maebh",
        "about_me": "barista queen",
        "fav_movie": "Sharknado"
    },
    {
        "name": "Annie",
        "about_me": "love to eat but loathe cooking",
        "fav_movie": "Reservoir Dogs"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/what_to_watch", methods=['GET', 'POST'])
def what_to_watch():
    form = Input_User()
    return render_template('what_to_watch.html', title='What To Watch', form=form)

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
