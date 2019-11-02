from unittest import TestCase

from xyz.cawfeecake.board_games.board import Board


class BoardTest(TestCase):

    """
    5   x   x   x   x   x
    4   x   x   x   x   x
    3   x   x   x   x   x
    2   x   x   x   x   x
    1   x   x   x   x   x
        1   2   3   4   5
    """
    test_board = Board(5)

    def test_is_on_board(self):
        for i in range(1, 6):
            for j in range(1, 6):
                test_location = (i, j)
                self.assertTrue(self.test_board.is_on_board(test_location))
        self.assertFalse(self.test_board.is_on_board((0, 1)))
        self.assertFalse(self.test_board.is_on_board((6, 6)))

    def test_next_row(self):
        test_location = (4, 2)
        next_row = self.test_board.next_row(test_location)
        self.assertIsNotNone(next_row)
        next_row = self.test_board.next_row(next_row)
        self.assertIsNone(next_row)

    def test_prev_row(self):
        test_location = (2, 2)
        prev_row = self.test_board.prev_row(test_location)
        self.assertIsNotNone(prev_row)
        prev_row = self.test_board.prev_row(prev_row)
        self.assertIsNone(prev_row)

    def test_next_col(self):
        test_location = (2, 4)
        next_col = self.test_board.next_col(test_location)
        self.assertIsNotNone(next_col)
        next_col = self.test_board.next_col(next_col)
        self.assertIsNone(next_col)

    def test_prev_col(self):
        test_location = (2, 2)
        prev_col = self.test_board.prev_col(test_location)
        self.assertIsNotNone(prev_col)
        prev_col = self.test_board.prev_col(prev_col)
        self.assertIsNone(prev_col)

    def test_next_row_next_col_diag(self):
        test_location = (4, 4)
        next_diag_loc = self.test_board.next_row_next_col_diag(test_location)
        self.assertIsNotNone(next_diag_loc)
        next_diag_loc = self.test_board.next_row_next_col_diag(next_diag_loc)
        self.assertIsNone(next_diag_loc)

    def test_next_row_prev_col_diag(self):
        test_location = (4, 2)
        next_diag_loc = self.test_board.next_row_prev_col_diag(test_location)
        self.assertIsNotNone(next_diag_loc)
        next_diag_loc = self.test_board.next_row_prev_col_diag(next_diag_loc)
        self.assertIsNone(next_diag_loc)

    def test_prev_row_next_col_diag(self):
        test_location = (2, 4)
        next_diag_loc = self.test_board.prev_row_next_col_diag(test_location)
        self.assertIsNotNone(next_diag_loc)
        next_diag_loc = self.test_board.prev_row_next_col_diag(next_diag_loc)
        self.assertIsNone(next_diag_loc)

    def test_prev_row_prev_col_diag(self):
        test_location = (2, 2)
        next_diag_loc = self.test_board.prev_row_prev_col_diag(test_location)
        self.assertIsNotNone(next_diag_loc)
        next_diag_loc = self.test_board.prev_row_prev_col_diag(next_diag_loc)
        self.assertIsNone(next_diag_loc)

    def test_generate_next_row(self):
        test_start_row = 1
        test_location = (test_start_row, 2)
        test_gen = self.test_board.get_next_row_generator(test_location)

        curr_test_row = test_start_row + 1
        for next_row, _ in test_gen:
            self.assertEqual(curr_test_row, next_row)
            curr_test_row += 1

        self.assertEqual(6, curr_test_row)

    def test_no_iteration_given_generate_at_location_off_board(self):
        test_location = (6, 5)
        test_gen = self.test_board.get_next_row_generator(test_location)
        for _, _ in test_gen:
            self.fail()

    def test_no_iteration_given_generate_at_location_with_no_next_location(self):
        test_location = (5, 5)
        self.assertTrue(self.test_board.is_on_board(test_location))
        test_gen = self.test_board.get_next_row_generator(test_location)
        for _, _ in test_gen:
            self.fail()

    def test_generate_prev_row(self):
        test_start_location = (5, 2)
        test_gen = self.test_board.get_prev_row_generator(test_start_location)
        next_col_locations = list(test_gen)
        self.assertEqual([(4, 2), (3, 2), (2, 2), (1, 2)], next_col_locations)

    def test_generate_next_col(self):
        test_start_location = (2, 1)
        test_gen = self.test_board.get_next_col_generator(test_start_location)
        next_col_locations = list(test_gen)
        self.assertEqual([(2, 2), (2, 3), (2, 4), (2, 5)], next_col_locations)

    def test_generate_prev_col(self):
        test_start_location = (2, 5)
        test_gen = self.test_board.get_prev_col_generator(test_start_location)
        next_col_locations = list(test_gen)
        self.assertEqual([(2, 4), (2, 3), (2, 2), (2, 1)], next_col_locations)

    def test_generate_next_row_next_col_diag(self):
        test_start_location = (1, 1)
        test_gen = self.test_board.get_next_row_next_col_diag_generator(test_start_location)
        next_col_locations = list(test_gen)
        self.assertEqual([(2, 2), (3, 3), (4, 4), (5, 5)], next_col_locations)

    def test_generate_next_row_prev_col_diag(self):
        test_start_location = (1, 5)
        test_gen = self.test_board.get_next_row_prev_col_diag_generator(test_start_location)
        next_col_locations = list(test_gen)
        self.assertEqual([(2, 4), (3, 3), (4, 2), (5, 1)], next_col_locations)

    def test_generate_prev_row_next_col_diag(self):
        test_start_location = (5, 1)
        test_gen = self.test_board.get_prev_row_next_col_diag_generator(test_start_location)
        next_col_locations = list(test_gen)
        self.assertEqual([(4, 2), (3, 3), (2, 4), (1, 5)], next_col_locations)

    def test_generate_prev_row_prev_col_diag(self):
        test_start_location = (5, 5)
        test_gen = self.test_board.get_prev_row_prev_col_diag_generator(test_start_location)
        next_col_locations = list(test_gen)
        self.assertEqual([(4, 4), (3, 3), (2, 2), (1, 1)], next_col_locations)
