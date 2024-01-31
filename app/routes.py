from app import app
# another way to do this is using blueprints


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"