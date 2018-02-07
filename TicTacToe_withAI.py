import random
from random import randrange

#create game board
def create_board(board):
    print '   |   |   '
    print ' '+board[7]+' | '+board[8]+' | '+board[9]+' '
    print '---|---|---'
    print ' '+board[4]+' | '+board[5]+' | '+board[6]+' '
    print '---|---|---' 
    print ' '+board[1]+' | '+board[2]+' | '+board[3]+' '
    print '   |   |   '

#checks to see if any space is open and allows the game to continue
def check_full(board):
    for i in range(1,10):
        if check_open_space(board,i):
            return False
    else:
        return True

#checks if space is available
def check_open_space(board,move):
    return board[move] == ' '
    
#makes sure that player's selected move is a legal move
def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not check_open_space(board,int(move)):
        move = raw_input('What is your next move:  ')
    return int(move)

#adds player move to board list
def player_move(board,letter,move):
    board[move] = letter

#checks player move on duplicate board. To be used with computer "block" strategy
def player_move_check(dupe,letter,move):
    dupe[move] = letter

#this list is used to see if preferred spaces (corners, then middle, then sides will be entered) and creates available list
def moves_open_list(board,prefer_moves):
    open_list = []
    for i in prefer_moves:
        if check_open_space(board,i):
            open_list.append(i)
            
        if len(open_list) != 0:
            move = random.choice(open_list)
            return int(move)
        else:
            pass
        
#computer will look to win first, or block second, or select preferred move.
def get_smart_move_2(board,computer):
    if computer == 'X':
        player = 'O'
    else:
        player = 'X'
    
    #check for winning move
    for i in range(1,10):
        copy = dupe_board(board)
        if check_open_space(copy,i) == True:
            player_move(copy,computer,i)
            if check_winner(copy,computer) == True:
                return int(i)
                
    #check for player winning move and block
    for i in range(1,10):
        copy = dupe_board(board)
        if check_open_space(copy,i) == True:
            copy[i] = player
            if check_winner(copy,player):
                return int(i)
            
  
    #check for best move for computer
    move = moves_open_list(board,[1,3,7,9])
    if move != None:
        return int(move)
    
    if check_open_space(board,5):
        return 5
        
    return moves_open_list(board,[2,4,6,8])

#this function did not work like I wanted. I need to remove it.
def dupe_board(board):
    dupe = []
    for i in board:
        dupe.append(i)
        
    return dupe
            
#adds computer move to board list
def computer_move(board,letter,move):
    board[move] = letter

#lets player select letter
def player_letter():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        letter = raw_input('Which letter do you want? ').upper()
        
    if letter == 'X':
        return ('X','O')
    else:
        return ('O','X')

#checks for winning combination on board
def check_winner(board,letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))

#pick who goes first
def who_goes_first():
    if random.randint(0,1) == 1:
        return 'Player'
    else:
        return 'Computer'

#let player decide if they want to play again
def play_again():
    return raw_input('Do you want to play again? ').lower().startswith('y') 
    
#start game
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
                    break
                    
                else:
                    turn = 'Computer'               
       
        else:
            move = get_smart_move_2(board,computer)
            #get_computer_move_alt(board)
            computer_move(board,computer,move)
            print ('Computer selects: ' +str(move))
            if check_winner(board,computer):
                create_board(board)
                print ('The computer beat you!!!')
                game_is_playing = False
                
            else:
                if check_full(board):
                    create_board(board)
                    print ('The game is a draw!')
                    break
                
            turn = 'Player'
 
    if not play_again() == True:
        break
