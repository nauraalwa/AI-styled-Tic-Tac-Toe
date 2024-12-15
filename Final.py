import random

# Initialize the board
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])

def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove():
    run = True
    while run:
        move = input('Pick a position to place an \'x\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('x', move)
                else:
                    print('Sorry, the space is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = [i for i in possibleMoves if i in [1, 3, 7, 9]]

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        return 5

    edgesOpen = [i for i in possibleMoves if i in [2, 4, 6, 8]]

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return 0

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    return board.count(' ') == 0

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not isBoardFull(board):
        if isWinner(board, 'o'):
            print('Sorry, o won this time..')
            break
        elif isWinner(board, 'x'):
            print('You won! Great Job!')
            break
        else:
            playerMove()
            printBoard(board)

        if not isBoardFull(board):
            move = compMove()
            if move == 0:
                print('Tie game!')
                break
            else:
                insertLetter('o', move)
                print(f'Computer placed an \'o\' in position {move}:')
                printBoard(board)
        else:
            print('Tie game!')
            break

main()
