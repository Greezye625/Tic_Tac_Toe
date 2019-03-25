import colorama
import time
import os
from colorama import Fore, Style

colorama.init()


def cls():
    """
    Commented out - bootleg "clear console" for Pycharm,
    use while writing, and switch to "os.system..." line when
    packing into .exe

    for getting coordinates:
    time.sleep(2)
    print(pyautogui.position())

    launch program, and move cursor to the simulated console window,
    after 2s you'll get coordinates to put as pyautogui.click() arguments
    :return:
    """

    # time.sleep(0.1)
    # pyautogui.click(x=778, y=832)
    # pyautogui.hotkey('ctrl', 'l')

    os.system('cls' if os.name == 'nt' else 'clear')


def victory(arg_grid):
    if arg_grid['1'] == arg_grid['2'] == arg_grid['3']:
        return True
    if arg_grid['1'] == arg_grid['4'] == arg_grid['7']:
        return True
    if arg_grid['1'] == arg_grid['5'] == arg_grid['9']:
        return True
    if arg_grid['2'] == arg_grid['5'] == arg_grid['8']:
        return True
    if arg_grid['3'] == arg_grid['6'] == arg_grid['9']:
        return True
    if arg_grid['3'] == arg_grid['5'] == arg_grid['7']:
        return True
    if arg_grid['4'] == arg_grid['5'] == arg_grid['6']:
        return True
    if arg_grid['7'] == arg_grid['8'] == arg_grid['9']:
        return True
    return False


def gameboard(arg_grid):
    print('     |     |')
    print('  {}  |  {}  |  {}  '.format(arg_grid['7'],
                                        arg_grid['8'], arg_grid['9']))
    print('     |     |')
    print('-----|-----|-----')
    print('     |     |')
    print('  {}  |  {}  |  {}  '.format(arg_grid['4'],
                                        arg_grid['5'], arg_grid['6']))
    print('     |     |')
    print('-----|-----|-----')
    print('     |     |')
    print('  {}  |  {}  |  {}  '.format(arg_grid['1'],
                                        arg_grid['2'], arg_grid['3']))
    print('     |     |')


def next_player(arg_current_player):
    global color
    if arg_current_player == 'X':
        nextplayer = 'O'
        color = Fore.CYAN
        return nextplayer
    else:
        nextplayer = 'X'
        color = Fore.RED
        return nextplayer


print('Welcome in the game of Tic Tac Toe')
again = 'y'

while again.casefold() != 'n':

    player1 = input('Player 1 choose your team X/O  ')
    player2 = None
    grid = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9'}
    checkgrid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if player1.casefold() == 'x':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'

    print(f'Player1 is {player1} \nPlayer2 is {player2}')
    print('GAME BEGINS...')

    current_player = player1
    counter = 0

    if current_player == 'X':
        color = Fore.RED
    else:
        color = Fore.CYAN

    time.sleep(2)
    cls()
    while not victory(grid) and counter < 9:
        gameboard(grid)

        move = input(f'Player {current_player} make your move: ')
        if (move not in checkgrid) and (move != 0):
            print('!!!INVALID MOVE!!!')
            continue
        grid[move] = Style.BRIGHT + color + current_player + Style.RESET_ALL
        checkgrid[int(move)-1] = '0'

        current_player = next_player(current_player)

        counter += 1
        cls()

    gameboard(grid)

    if victory(grid):
        current_player = next_player(current_player)
        print(f'Player {current_player} Has Won!!!')
    else:
        print("It's a Draw!!!")

    again = input('\nDo you want to play again? (Y/N)')
    cls()

print('\nThanks For Playing!!!')

time.sleep(2.0)
