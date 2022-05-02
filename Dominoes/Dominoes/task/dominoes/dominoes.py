import random


def try_or_take_extra_piece_from_stock(the_pieces, the_scores, list_pieces):
    _piece = 0
    left = list_pieces[0]
    right = list_pieces[-1]

    reorder_pieces = []
    for key in the_scores:
        reorder_pieces.append(the_pieces[key])

    # print(pieces)
    # print(reorder_pieces, "reorder gamer pieces")

    for p in reorder_pieces:
        if p[0] == left[0] or p[1] == left[0]:
            # _piece = p
            _piece = 0 - (the_pieces.index(p) + 1)

        if p[0] == right[1] or p[1] == right[1]:
            # _piece = p
            _piece = the_pieces.index(p) + 1

    return _piece


def scores(the_pieces, d_count):
    d_scores = {}
    for idx, p in enumerate(the_pieces):
        d_scores.update({idx: d_count[p[0]] + d_count[p[1]]})

    d_scores = {k: v for k, v in sorted(d_scores.items(), key=lambda item: item[1], reverse=True)}

    return d_scores


def number_of_repetitions(the_list_pieces):
    flat = flatten_list(the_list_pieces)
    n_dict = dict()
    for n in range(6 + 1):
        n_dict.update({n: flat.count(n)})

    return n_dict


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


def generate_pieces_set():
    pieces = []
    for i in range(7):
        pieces.extend([[i, j] for j in range(i, 7)])
    return pieces


def split_pieces_set(pieces_set):
    random.shuffle(pieces_set)
    return pieces_set[:7], pieces_set[7:14], pieces_set[14:]


def find_highest_piece(pieces_set):
    highest = None
    for piece in pieces_set:
        if piece[0] == piece[1] \
                and (highest is None or sum(piece) > sum(highest)):
            highest = piece
    return highest


def determine_starting_piece(player_piece, computer_piece):
    if player_piece is not None \
            and computer_piece is not None:
        return player_piece if sum(player_piece) > sum(computer_piece) else computer_piece
    if player_piece is not None \
            and computer_piece is None:
        return player_piece
    if player_piece is None \
            and computer_piece is not None:
        return computer_piece
    return None


def is_draw():
    if len(domino_snake) > 2:
        end_number = domino_snake[0][0]
        if end_number == domino_snake[-1][1]:
            return sum([piece.count(end_number) for piece in domino_snake if end_number in piece]) == 8
    return False


def is_valid_move(pieces_set, piece_number):
    if piece_number == 0:
        return True
    else:
        piece = pieces_set[abs(piece_number) - 1]
        return domino_snake[0][0] in piece \
            if piece_number < 0 else domino_snake[-1][1] in piece


def setup_game():
    global player_pieces, computer_pieces, stock_pieces, turn

    piece = None
    computer_piece = find_highest_piece(computer_pieces)
    player_piece = find_highest_piece(player_pieces)

    if player_piece is not None \
            and computer_piece is not None:
        piece = player_piece if sum(player_piece) > sum(computer_piece) else computer_piece
    elif player_piece is not None \
            and computer_piece is None:
        piece = player_piece
    elif player_piece is None \
            and computer_piece is not None:
        piece = computer_piece

    if piece is not None:
        if piece == player_piece:
            player_pieces.remove(piece)
            turn = 'computer'
        else:
            computer_pieces.remove(piece)
            turn = 'player'
        domino_snake.append(piece)
    else:
        player_pieces, computer_pieces, stock_pieces = split_pieces_set(generate_pieces_set())
        setup_game()


def draw_the_snake():
    if len(domino_snake) > 6:
        print(*domino_snake[:3],
              '...',
              *domino_snake[(len(domino_snake) - 3):],
              sep='')
    else:
        print(*domino_snake, sep='')


def display_current_field():
    print('=' * 70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_pieces)}\n')

    draw_the_snake()

    print()
    print(f'Your pieces:')
    for i in range(len(player_pieces)):
        print(f'{i + 1}:{player_pieces[i]}')
    print()


def prompt():
    display_current_field()

    if turn == 'computer':
        print('Status: Computer is about to make a move. '
              + 'Press Enter to continue...')
        input()
    else:

        print("Status: It's your turn to make a move. "
              + 'Enter your cmd.')

        while True:
            try:
                piece_number = int(input())
            except ValueError:
                print('Invalid input. '
                      + 'Please try again.')
            else:
                if abs(piece_number) not in range(len(player_pieces) + 1):
                    print('Invalid input. '
                          + 'Please try again.')
                elif not is_valid_move(player_pieces, piece_number):
                    print('Illegal move. '
                          + 'Please try again.')
                else:
                    return piece_number

    return None


def play_game():
    global domino_snake, turn
    setup_game()

    game_over = False
    while not game_over:

        piece_number = prompt()
        if piece_number is None:

            computer_size = len(computer_pieces)

            # while True:
            #     piece_number = random.choice(range(-computer_size, computer_size + 1))
            #     if is_valid_move(computer_pieces, piece_number):
            #         break

            while True:
                d_flat = number_of_repetitions(computer_pieces + domino_snake)
                score_computer = scores(computer_pieces, d_flat)
                piece_number = try_or_take_extra_piece_from_stock(computer_pieces, score_computer, domino_snake)
                if is_valid_move(computer_pieces, piece_number):
                    break

            if piece_number == 0:
                if len(stock_pieces) > 0:
                    piece = random.choice(stock_pieces)
                    computer_pieces.append(piece)
                    stock_pieces.remove(piece)
            else:
                piece = computer_pieces.pop(abs(piece_number) - 1)
                game_over = len(computer_pieces) == 0
                if piece_number > 0:
                    domino_snake.append(piece if domino_snake[-1][1] == piece[0] else piece[::-1])
                else:
                    domino_snake.insert(0, piece if domino_snake[0][0] == piece[1] else piece[::-1])

            turn = 'player'

        else:
            if piece_number == 0:
                if len(stock_pieces) > 0:
                    piece = random.choice(stock_pieces)
                    player_pieces.append(piece)
                    stock_pieces.remove(piece)
            else:
                piece = player_pieces.pop(abs(piece_number) - 1)
                game_over = len(player_pieces) == 0
                if piece_number > 0:
                    domino_snake.append(piece if domino_snake[-1][1] == piece[0] else piece[::-1])
                else:
                    domino_snake.insert(0, piece if domino_snake[0][0] == piece[1] else piece[::-1])
            turn = 'computer'

        if not game_over:
            game_over = is_draw()

    display_current_field()

    if len(player_pieces) == 0:
        print('Status: The game is over. '
              + 'You won!')
    elif len(computer_pieces) == 0:
        print('Status: The game is over. '
              + 'The computer won!')
    else:
        print('Status: The game is over. '
              + "It's a draw!")


player_pieces, computer_pieces, stock_pieces = split_pieces_set(generate_pieces_set())
domino_snake, turn = [], None

play_game()
