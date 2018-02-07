import random
#create tic tac toe board with empty space. Board numbers are placeholders.
def create_board(board):
    print '   |   |   '
    print ' '+board[7]+' | '+board[8]+' | '+board[9]+' '
    print '---|---|---'
    print ' '+board[4]+' | '+board[5]+' | '+board[6]+' '
    print '---|---|---' 
    print ' '+board[1]+' | '+board[2]+' | '+board[3]+' '
    print '   |   |   '

#check spaces 1-9 to see if any space is open, if space is open then game can continue.
def check_full(board):
    for i in range(1,10):
        if check_open_space(board,i):
            return False
    else:
        return True

#looks to see if a space is available
def check_open_space(board,move):
    return board[move] == ' '

#gets player move and verifies it is a legal and open move
def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not check_open_space(board,int(move)):
        move = raw_input('What is your next move:  ')
    return int(move)

#adds players selected move to board list.
def player_move(board,letter,move):
    board[move] = letter

#gets randompy selected computer move. (don't need the list/split...need to come back and take it out)
def get_computer_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not check_open_space(board,int(move)):
        move = random.randint(1,9)
        return int(move)

#adds computers move to board list.
def computer_move(board,letter,move):
    board[move] = letter

#lets player select letter, verifies that it is x or o and capitalizes selection
def player_letter():
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = raw_input('Which letter do you want? ').upper()
        
    if letter == 'X':
        return ('X','O')
    else:
        return ('O','X')

#checks to see if any combination on the board is a winner.
def check_winner(board,letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))

#randomly selects who goes first.
def who_goes_first():
    if random.randint(0,1) == 1:
        return 'Player'
    else:
        return 'Computer'

#if game is won or draw, asks player if they want play again.
def play_again():
    return raw_input('Do you want to play again? ').lower().startswith('y')

#tictactoe game
print ('Welcome to tic-tac-toe!')
while True:

    board = [' ']*10
    player,computer = player_letter()
    turn = who_goes_first()
    game_is_playing = True
    
    while game_is_playing:
        if turn == 'Player':
            print ("Player's turn")
            create_board(board)
            move = get_player_move(board)
            player_move(board,player,move)
            if check_winner(board,player):
                create_board(board)
                print("You're a winner!!!")
                game_is_playing = False
                
            else:
                if check_full(board):
                    create_board(board)
                    print ('The game is a draw!')
                    
                else:
                    turn = 'Computer'               
       
        else:
            move = get_computer_move(board)
            computer_move(board,computer,move)
            if check_winner(board,computer):
                create_board(board)
                print ('The computer beat you!!!')
                game_is_playing = False
                
            else:
                if check_full(board):
                    create_board(board)
                    print ('The game is a draw!')
                    
                else:
                    turn = 'Player'
 
    if not play_again():
        break
