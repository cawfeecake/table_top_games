from typing import Tuple


class Board:

    def __init__(self, size: int):
        """
        Creates a square board.
        :param size: the number of rows and columns the board will have
        """
        self.size = size if size > 0 else 1

    def is_on_board(self, location: Tuple[int, int]) -> bool:
        """
        Determines if the location is on the board.
        :param location: a tuple for the (row, col) coordinates of the location of interest
        :return: True if the location is on the board; False otherwise
        """
        row, col = location
        return 0 < row <= self.size and 0 < col <= self.size

    def next_row(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row + 1, col)
        return new_loc if self.is_on_board(new_loc) else None

    def get_next_row_generator(self, start_location):
        next_loc = self.next_row(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.next_row(next_loc)

    def prev_row(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row - 1, col)
        return new_loc if self.is_on_board(new_loc) else None

    def get_prev_row_generator(self, start_location):
        next_loc = self.prev_row(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.prev_row(next_loc)

    def next_col(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row, col + 1)
        return new_loc if self.is_on_board(new_loc) else None

    def get_next_col_generator(self, start_location):
        next_loc = self.next_col(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.next_col(next_loc)

    def prev_col(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row, col - 1)
        return new_loc if self.is_on_board(new_loc) else None

    def get_prev_col_generator(self, start_location):
        next_loc = self.prev_col(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.prev_col(next_loc)

    def next_row_next_col_diag(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row + 1, col + 1)
        return new_loc if self.is_on_board(new_loc) else None

    def get_next_row_next_col_diag_generator(self, start_location):
        next_loc = self.next_row_next_col_diag(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.next_row_next_col_diag(next_loc)

    def next_row_prev_col_diag(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row + 1, col - 1)
        return new_loc if self.is_on_board(new_loc) else None

    def get_next_row_prev_col_diag_generator(self, start_location):
        next_loc = self.next_row_prev_col_diag(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.next_row_prev_col_diag(next_loc)

    def prev_row_next_col_diag(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row - 1, col + 1)
        return new_loc if self.is_on_board(new_loc) else None

    def get_prev_row_next_col_diag_generator(self, start_location):
        next_loc = self.prev_row_next_col_diag(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.prev_row_next_col_diag(next_loc)

    def prev_row_prev_col_diag(self, location: Tuple[int, int]) -> Tuple[int, int]:
        row, col = location
        new_loc = (row - 1, col - 1)
        return new_loc if self.is_on_board(new_loc) else None

    def get_prev_row_prev_col_diag_generator(self, start_location):
        next_loc = self.prev_row_prev_col_diag(start_location)
        while next_loc:
            yield next_loc
            next_loc = self.prev_row_prev_col_diag(next_loc)
