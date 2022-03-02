board=[' ' for x in range(10)]
#functions
def insert_letter(let,pos):
    board[pos]=let

def spaceisfree(pos):
    return board[pos]==' '

def display_board(board):
    print('   |   |')
    print('',board[1],'|',board[2],'|',board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('',board[4],'|',board[5],'|',board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('',board[7],'|',board[8],'|',board[9])
    print('   |   |')
   
def is_winner(board,let):
    return (board[1]==let and board[2]==let and board[3]==let)or(board[4]==let and board[5]==let and board[6]==let)or(board[7]==let and board[8]==let and board[9]==let)or(board[1]==let and board[5]==let and board[9]==let)or(board[2]==let and board[5]==let and board[8]==let)or(board[3]==let and board[5]==let and board[7]==let)or(board[1]==let and board[4]==let and board[7]==let)or(board[3]==let and board[9]==let and board[6]==let)

def player_move(playerString):
    run=True
    while run:
        move=int(input('enter position(1-9): '))
        if move>0 and move<10:
            if spaceisfree(move):
                insert_letter(playerString, move)
                run=False
            else:
                print('space is occupied. Try again!')
        else:
            print('type number in range!')


def isboardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def main():
    print('Welecome to tic tac toe!')
    display_board(board)
    while not (isboardfull(board)):
        if not(is_winner(board,'O')):
            player_move("X")
            display_board(board)
        else:
            print('player2 wins')
            break
        if not(is_winner(board,'X')):
            player_move("O")
            display_board(board)
        else:
            print('player1 wins')
            break
    if isboardfull(board):
        print('Tie game!')

if __name__ == "__main__":
    board = [' ' for x in range(10)]
    print('----------------------')
    main()
    while True:
        answer = input('Do u want to play again(y/n): ')
        if answer.lower() == 'y':
            board = [' ' for x in range(10)]
            print('----------------------')
            main()
        else:
            print("Thank you for playing!!!")
            break