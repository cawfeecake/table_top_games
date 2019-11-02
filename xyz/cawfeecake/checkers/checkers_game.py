from typing import Callable, Tuple, List

from xyz.cawfeecake.board_games.board import Board
from xyz.cawfeecake.checkers.checkers_piece import UpChecker, DownChecker, get_moves_for_checker, King


class CheckersGame:
    """
    Default start...

    (rows)
    8   .   b   .   b   .   b   .   b
    7   b   .   b   .   b   .   b   .
    6   .   b   .   b   .   b   .   b
    5   .   .   .   .   .   .   .   .
    4   .   .   .   .   .   .   .   .
    3   a   .   a   .   a   .   a   .
    2   .   a   .   a   .   a   .   a
    1   a   .   a   .   a   .   a   .
        1   2   3   4   5   6   7   8 (cols)
    """

    def __init__(self):
        self.board = Board(8)

        self.__player_reps = ['a', 'b']
        self.player_with_next_move = 0
        self.pieces = {}
        # set up the pieces of player that will go up the board
        for starting_location in [(1, 1), (1, 3), (1, 5), (1, 7),
                                  (2, 2), (2, 4), (2, 6), (2, 8),
                                  (3, 1), (3, 3), (3, 5), (3, 7)]:
            self.pieces[starting_location] = (UpChecker, 0)
        self.pieces[(0, 0)] = (King, 0)

        # set up the pieces of player that will go down the board
        for starting_location in [(6, 2), (6, 4), (6, 6), (6, 8),
                                  (7, 1), (7, 3), (7, 5), (7, 7),
                                  (8, 2), (8, 4), (8, 6), (8, 8)]:
            self.pieces[starting_location] = (DownChecker, 1)

    def __str__(self):
        return self.__iterate_board_left_to_right(self.__default_str_rep_function)

    def highlight_moves(self, moves: List[Tuple[int, int]]) -> str:
        return self.__iterate_board_left_to_right(
            lambda loc: 'X' if loc in moves else self.__default_str_rep_function(loc))

    def __iterate_board_left_to_right(self, func: Callable[[Tuple[int, int]], str]) -> str:
        str_rep = ''
        for i in range(self.board.size, 0, -1):
            for j in range(1, self.board.size + 1):
                str_rep += func((i, j))
                str_rep += '\t'
            str_rep += '\n'
        return str_rep.strip()

    def __default_str_rep_function(self, board_location: Tuple[int, int]) -> str:
        if board_location in self.pieces.keys():
            checker_type, checker_owner = self.pieces[board_location]
            checker_rep = self.__player_reps[checker_owner]
            return checker_rep if checker_type is not King else checker_rep.upper()
        else:
            return '.'

    def __submit_move(self, selected_position: (int, int), new_position: (int, int)):
        if selected_position in self.pieces:
            selected_checker = self.pieces.get(selected_position)
            del self.pieces[selected_position]
            self.pieces[new_position] = selected_checker

            self.player_with_next_move = (self.player_with_next_move + 1) % 2


if __name__ == '__main__':
    game = CheckersGame()
    print(game)
    while True:
        console_input = input('Next move: ').strip()
        if console_input == '':
            continue
        elif console_input == 'q' or console_input == 'quit':
            print('Goodbye...')
            break
        elif console_input == 'b' or console_input == 'board':
            print(game)
            continue
        else:
            try:
                input_tokens = list(map(int, console_input.split()))
            except ValueError:
                print(f'[ERROR] input must only include integers (input: {console_input})')
                continue

            if len(input_tokens) == 2:
                # provided coordinates of a checker; display available moves
                selected_row, selected_col = input_tokens
                selected_location = (selected_row, selected_col)
                if selected_location not in game.pieces:
                    print(f'[ERROR] no checker @ {selected_location}')
                else:
                    moves = get_moves_for_checker(selected_location, game.pieces, game.board)
                    num_moves = len(moves)
                    if len(moves) > 0:
                        print(game.highlight_moves(moves))
                        print(f'checker @ {selected_location} has {num_moves} move{"s" if num_moves > 1 else ""}: {moves}')
                    else:
                        print(f'no moves available for checker @ {selected_location}')
            elif len(input_tokens) == 4:
                # provided coordinates of a checker and target position; attempt to move
                selected_row, selected_col, target_row, target_col = input_tokens
                selected_location = (selected_row, selected_col)
                if selected_location not in game.pieces:
                    print(f'[ERROR] no checker @ {selected_location}')
                else:
                    target_location = (target_row, target_col)
                    if target_location in get_moves_for_checker(selected_location, game.pieces, game.board):
                        game._CheckersGame__submit_move(selected_location, target_location)  # TODO
                        print(game)
                    else:
                        print(f'[ERROR] invalid to move checker from {selected_location} to {target_location}')
            else:
                print(f'[ERROR] unknown operation (input: {console_input})')
