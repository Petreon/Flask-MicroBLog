from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
# another way to do this is using blueprints


@app.route('/')
@app.route('/index')
def index():
    user = {"username":"Miguel"}

    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beatiful day in Portland'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The Avenger movie was so cool'
        }
    ]

    return render_template('index.html', user=user, title = 'Home', posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    ## this LoginForm is on forms.py
    form = LoginForm()

    ## this handle the post method for us
    if form.validate_on_submit():
        #When the browser sends the POST request as a result of the user pressing the submit button, form.validate_on_submit() is going to gather all the data, run all the validators attached to fields, and if everything is all right it will return True, indicating that the data is valid and can be processed by the application
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')

        return redirect(url_for('index'))
    ## the error handling from the form is in the form boject in the html template with form.username.errors method


    return render_template('login.html', form=form)