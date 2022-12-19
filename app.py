from flask import Flask, render_template, request, jsonify
from logic import HumanPlayer, Game

app = Flask(__name__)
player1 = None
player2 = None
game = None
turn = 'player1'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    global player1, player2, game
    game = Game()
    player1 = HumanPlayer(take="X", name=request.args.get("player1"))
    player2 = HumanPlayer(take="O", name=request.args.get("player2"))
    game.player1 = player1
    game.player2 = player2
    return render_template("game.html")

@app.route("/move", methods=["POST"])
def move():
    global turn
    move = request.json["move"]
    if turn == 'player1':
        game.board[move] = player1.take
        if game.isWinner(game.board):
            print("Player %s Win" % player1.name)
            winner = player1.name
            game.update_statistics(winner)
            return jsonify({
                "winner": winner,
                "draw": False,
                "gameover": True,
            })
        else:
            turn = "player2"
    else:
        game.board[move] = player2.take
        if game.isWinner(game.board):
            print("Player %s Win" % player2.name)
            winner = player2.name
            game.update_statistics(winner)
            return jsonify({
                "winner": winner,
                "draw": False,
                "gameover": True,
            })
        else:
            turn = "player1"
    if game.isDraw(game.board):
        print('Draw')
        winner = None
        game.update_statistics(winner)
        return jsonify({
            "winner": None,
            "draw": True,
            "gameover": True,
        })
    else:
        return jsonify({
            "winner": None,
            "draw": False,
            "gameover": False,
        })

@app.route("/stat")
def stat():
    return render_template("stats.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=4000)