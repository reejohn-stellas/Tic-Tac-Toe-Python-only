import random


def board_checker(board):
    lst = [[board[0][0], board[1][0], board[2][0]],
           [board[0][1], board[1][1], board[2][1]],
           [board[0][2], board[1][2], board[2][2]],
           [board[0][0], board[0][1], board[0][2]],
           [board[1][0], board[1][1], board[1][2]],
           [board[2][0], board[2][1], board[2][2]],
           [board[0][0], board[1][1], board[2][2]],
           [board[0][2], board[1][1], board[2][0]]
           ]
    for i in lst:
        if i == ['X', 'X', 'X']:
            print('player1 won')
            for i in board:
                print(i)
            return 1

        elif i == ['O', 'O', 'O']:
            print('player2 won')
            for i in board:
                print(i)
            return 1


def spacechecker(board):
    board1 = list()

    for i in board:
        l = board.index(i) 

        c = 0
        for j in i:
            if j == '-':
                l1 = c
                m = l, l1
                board1.append(m)
            c += 1
    return board1


def entry():
    while True:
        try:
            x, y = input('enter rows and column no :').split()
            x = int(x)
            y = int(y)
            z = [x, y]

            if z in taken:
                print('place already taken ')
                continue
            else:
                break
        except ValueError:
            print('Enter index of row and column using space ')
            continue
        except:
            print('Enter index of row and column using space ')
            continue

    return z


while True:
    print('do you want to play with computer or player')
    choice = input('type c for computer  & p for 2 players : ')
    choice = choice.lower()

    if choice == 'c':
        player1 = ['player1', 'player2', 'player1', 'player2',
                   'player1', 'player2', 'player1', 'player2', 'player1']
        computer = ['player2', 'player1', 'player2', 'player1',
                    'player2', 'player1', 'player2', 'player1', 'player2']
        l = [player1, computer]
        chance = random.choice(l)
        board = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]
        taken = list()
        c = 0
        for i in chance:
            if i == 'player1':
                for i in board:
                    print(i)
                print('Player 1 turn: ')
                r = entry()
                x, y = r
                try:
                    board[x][y] = 'X'
                    taken.append(r)
                    c = board_checker(board)
                    if c:
                        break
                except IndexError:
                    print('index is out of range write index from 0 0 to 2 2')
                    continue
            elif i == 'player2':
                print('computer turn ')
                result = spacechecker(board)
                print(result)
                choice = random.choice(result)
                x, y = choice
                board[x][y] = 'O'
                taken.append([x, y])
                c = board_checker(board)
            if c:
                break
        else:
            print('draw')
    elif choice == 'p':
        player1 = ['player1', 'player2', 'player1', 'player2',
                   'player1', 'player2', 'player1', 'player2', 'player1']
        player2 = ['player2', 'player1', 'player2', 'player1',
                   'player2', 'player1', 'player2', 'player1', 'player2']
        l = [player1, player2]
        chance = random.choice(l)
        board = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]
        taken = list()
        c = 0
        for i in chance:
            if i == 'player1':
                for i in board:
                    print(i)
                print('Player 1 turn: ')
                r = entry()
                x, y = r
                board[x][y] = 'X'
                taken.append(r)
                c = board_checker(board)
                if c:
                    break
            elif i == 'player2':
                for i in board:
                    print(i)
                print('Player 2 turn: ')
                r = entry()
                x, y = r
                board[x][y] = 'O'
                taken.append(r)
                c = board_checker(board)
                if c:
                    break
        else:
            print('draw')
    else:
        print('\n wrong input enter again \n')
        continue
    q = input('type q to quit or type any other key to play again')
    if q.lower() == 'q':
        print('Thank You For Playing Bye !!!')
        break
