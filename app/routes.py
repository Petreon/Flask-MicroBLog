from flask import render_template
from app import app
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