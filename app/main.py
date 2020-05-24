import jinja2 as j2
from flask import render_template
from flask import Flask
from Board import Board

app = Flask(__name__)

@app.route('/')
def demo():
    game_board = Board()
    return render_template(
        'game.html.j2',
        title = 'Board - Demo',
        board = game_board
    )


if __name__ == '__main__':
    app.run()
