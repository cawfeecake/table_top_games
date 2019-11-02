from __future__ import annotations  # required for referencing the containing class type within type hints

from typing import Tuple, Dict, List, Type

from xyz.cawfeecake.board_games.board import Board


class Checker:
    """
    Defines the public interface
    """

    @classmethod
    def get_moves(cls, owner: int, location: Tuple[int, int],
                  pieces: Dict[Tuple[int, int], Tuple[Type[Checker], int]], board: Board) -> List[Tuple[int, int]]:
        pass


def get_moves_for_checker(checker_location: Tuple[int, int],
                          pieces: Dict[Tuple[int, int], Tuple[Type[Checker], int]],
                          board: Board) \
        -> List[Tuple[int, int]]:
    """
    :param checker_location: this is the checker that will be considered moving
    :param pieces: all pieces on the board currently in play; [NOTE] must include a value for key "checker_location"
    :param board: the board the game of checkers is being played on
    :return: a list of available moves for the checker (empty if there are none)
    """
    checker_type, checker_owner = pieces[checker_location]
    return checker_type.get_moves(checker_owner, checker_location, pieces, board)


class UpChecker(Checker):
    """A checker that travels in an increasing rank direction on the board"""

    @classmethod
    def get_moves(cls, owner: int, location: Tuple[int, int],
                  pieces: Dict[Tuple[int, int], Tuple[Type[Checker], int]], board: Board) -> List[Tuple[int, int]]:
        moves = []

        file_inc_move = board.next_row_next_col_diag(location)
        if file_inc_move:
            if file_inc_move not in pieces:
                moves.append(file_inc_move)

        file_dec_move = board.next_row_prev_col_diag(location)
        if file_dec_move:
            if file_dec_move not in pieces:
                moves.append(file_dec_move)

        return moves


class DownChecker(Checker):
    """A checker that travels in a decreasing rank direction on the board"""

    @classmethod
    def get_moves(cls, owner: int, location: Tuple[int, int],
                  pieces: Dict[Tuple[int, int], Tuple[Type[Checker], int]], board: Board) -> List[Tuple[int, int]]:
        moves = []

        file_inc_move = board.prev_row_next_col_diag(location)
        if file_inc_move:
            if file_inc_move not in pieces:
                moves.append(file_inc_move)

        file_dec_move = board.prev_row_prev_col_diag(location)
        if file_dec_move:
            if file_dec_move not in pieces:
                moves.append(file_dec_move)

        return moves


class King(Checker):
    """
    A checker can travel in directions of either increasing or decreasing rank on the board.

    Is a promoted form of both "Up..." and "Down..." checkers.
    """

    @classmethod
    def get_moves(cls, owner: int, location: Tuple[int, int],
                  pieces: Dict[Tuple[int, int], Tuple[Type[Checker], int]], board: Board) -> List[Tuple[int, int]]:
        moves = []
        moves += UpChecker.get_moves(owner, location, pieces, board)
        moves += DownChecker.get_moves(owner, location, pieces, board)
        return moves
