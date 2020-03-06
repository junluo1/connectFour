from connect_four import create_board_state, is_horizontal_win, is_vertical_win,\
    is_right_to_left_win, is_left_to_right_win, board_full, piece_counter


def test_create_board_state():
    assert create_board_state() == [[None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None]]


def test_is_horizontal_win():
    assert is_horizontal_win((1, 0)) is True


def test_is_vertical_win():
    assert is_vertical_win((0, 1)) is True


def test_is_right_to_left_win():
    assert is_right_to_left_win((1, 1)) is True


def test_is_left_to_right_win():
    assert is_left_to_right_win((1, 0)) is True


def test_board_full():
    assert board_full() is False


def test_piece_counter():
    assert piece_counter() is None
