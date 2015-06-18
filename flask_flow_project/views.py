from flask_flow_project import app


@app.route('/')
def index():
    print('route loaded!')
    return 'Flask is running!'