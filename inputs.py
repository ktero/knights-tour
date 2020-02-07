from os import system, name


def clear():
    """
    Clears the console
    """
    # For windows
    if name == 'nt':
        _ = system('cls')
    
    # For mac and linux
    else:
        _ = system('clear')


def validate_input(p):
    """
    Check if user input is valid.
    """
    try:
        row, col = list(map(int, p.split(',')))

        if not 0 <= row < 8 or not 0 <= col < 8:
            raise ValueError()
    except:
        return False
    return True


def print_empty_board():
    """
    Print an empty board with indexes for all the cells
    """
    j = 0

    print()
    for i in range(9):
        if i != 0:
            # And so on...
            print(
                str(j) + '   ' +
                '|   |   |   |   |   |   |   |   |')
            print('    ' + '---------------------------------')
            j += 1
        else:
            # Top most
            print('      ' + '0   1   2   3   4   5   6   7\n')
            print('    ' + '---------------------------------')
    print('\n')