from logic import Game, HumanPlayer, ComputerPlayer, display_board

def main():
    game_mode = input("Please choose your game mode (pvp or pve):")
    game = Game()
    if game_mode == 'pvp':
        playerLetter = input("Player1 please choose'X'and'O', X goes first" )
        if playerLetter in ("X"):
            turn = "player1"
            player1Letter = "X"
            player2Letter ="O"
            player1 = HumanPlayer(take="X")
            player2 = HumanPlayer(take="O")
        else:
            turn = "player2"
            player2Letter = "X"
            player1Letter = "O"
            player1 = HumanPlayer(take="O")
            player2 = HumanPlayer(take="X")
    elif game_mode == 'pve':
        playerLetter = input("Player please choose 'X' or 'O'. 'X' goes first" )
        if playerLetter in ("X"):
            turn = "player1"
            player1Letter = "X"
            player2Letter ="O"
            player1 = HumanPlayer(take="X")
            player2 = ComputerPlayer(game=game, take="O")
        else:
            turn = "player2"
            player2Letter = "X"
            player1Letter = "O"
            player1 = HumanPlayer(take="O")
            player2 = ComputerPlayer(game=game, take="X")
    else:
        return None
    game.player1 = player1
    game.player2 = player2
    print("{}goes first".format(turn))
    while True:
        display_board(game.board)
        if turn == 'player1':
            move = player1.getPlayerMove(game.board)
            game.board[move] = player1Letter
            if game.isWinner(game.board):
                display_board(game.board)
                print("Player %s Win" % player1.name)
                winner = player1.name
                break
            else:
                turn = "player2"
        else:
            move = player2.getPlayerMove(game.board)
            game.board[move] = player2Letter
            if game.isWinner(game.board):
                display_board(game.board)
                print("Player %s Win" % player2.name)
                winner = player2.name
                break
            else:
                turn = "player1"

        if game.isDraw(game.board):
            display_board(game.board)
            print('Draw')
            winner = None
            break
    game.update_statistics(winner)

if __name__ == '__main__':
    main()