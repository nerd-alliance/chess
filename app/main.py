import jinja2 as j2
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def demo():
    return render_template('game.html.j2', title='Hello world', content='content')


if __name__ == '__main__':
    app.run()
