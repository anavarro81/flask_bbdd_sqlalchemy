from flask import Flask, render_template, request
from config import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # app.config.from_object(config['development'])
    app.run()