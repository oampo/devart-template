from main import app

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'
