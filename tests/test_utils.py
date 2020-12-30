"""
    Unit tests for pygo
    Date: 20.12.20
    Author: Hayk Karapetyan
"""
import pytest
from ..utils.board import Board

########## BOARD CLASS TESTS ##########


def test_board_type():
    """
        Tests default board type
    """
    new_board = Board()
    assert new_board.board_type == "19x19"


def test_empty_board():
    """
        Tests the default empty board set
    """
    default_goban = []
    default_n = 19
    for i in range(0, default_n):
        for j in range(0, default_n):
            default_goban.append({"x": i, "y": j, "val": None})

    new_board = Board()
    assert default_goban == new_board.board


def test_board_size():
    """
        Tests the sizes of boards
    """

    board = Board(9)
    assert len(board.board) == 81

    board2 = Board(13)
    assert len(board2.board) == 169

    board3 = Board(19)
    assert len(board3.board) == 361


def test_wrong_attr():
    with pytest.raises(AttributeError):
        Board(93)


def test_all_clear_board():
    """
        Tests if the board is empty aka has no values
    """

    size = 9
    board9 = Board(size)
    for i in board9.board:
        assert i["val"] == None

    size = 13
    board13 = Board(size)
    for i in board13.board:
        assert i["val"] == None

    size = 19
    board19 = Board(size)
    for i in board19.board:
        assert i["val"] == None


# ##### POSITIONS #####


def test_getting_position():
    """
        Test functionality of getting the position of
        specific stone by givving coordinates as parameters
    """

    board9 = Board(9)
    zero_pos = board9.get_position(4, 1)

    assert zero_pos["x"] == 4
    assert zero_pos["y"] == 1


def test_getting_wrong_position():
    """
        Test functionality of getting the position of
        specific stone by givving coordinates as parameters
    """
    with pytest.raises(AttributeError):
        board9 = Board(9)
        board9.get_position(10, 12)


def test_setting_position():
    """
        Tests if setting a stone on a position
        saves the data in the board
    """

    board9 = Board(9)
    board9.set_position(4, 5, "B")
    position_value = board9.get_position(4, 5)["val"]

    assert position_value == "B"


def test_setting_wrong_position():
    """
        Test functionality of setting the position of
        specific stone by givving wrong coordinates as parameters
    """
    with pytest.raises(AttributeError):
        board9 = Board(9)
        board9.set_position(32, 65, "W")


def test_setting_possition_on_non_empty_spot():
    """
        Test functionality of getting the position of
        specific stone by givving coordinates as parameters
    """
    board9 = Board(9)
    board9.set_position(1, 1, "B")
    with pytest.raises(Exception):
        board9.set_position(1, 1, "W")


# ##### VALUES #####


def test_setting_wrong_value():
    """
        Test functionality of setting the position of
        specific stone by givving wrong value
    """
    with pytest.raises(AttributeError):
        board9 = Board(9)
        board9.set_position(1, 1, "V")


def test_val_check_true():
    """
        Test val_check function on setting right values.
        Possible variants are: "B", "W" and None
    """
    board9 = Board(9)
    assert True == board9.val_check("B")


def test_val_check_true_None():
    """
        Test val_check function on setting right values.
        Possible variants are: "B", "W" and None
    """
    board9 = Board(9)
    assert True == board9.val_check(None)


def test_val_check_false():
    """
        Test val_check function on setting wrong values.
        Possible variants are: "B", "W" and None
    """
    with pytest.raises(AttributeError):
        board9 = Board(9)
        board9.val_check("Z")


# ##### SIBLINGS #####


def test_find_next_sibling_1hor():
    """
        Test functionality of function find_next_sibling.
        Givven 2 spots of same color, one should be able to
        find the other if they are adjacent.
        2 spots, same color, horizontal
    """
    board9 = Board(9)
    board9.set_position(2, 1, "B")
    board9.set_position(3, 1, "B")
    result = board9.find_next_siblings((2, 1), None, [])
    assert result[0] == (3, 1)


def test_find_next_siblings_1vert():
    """
        Test functionality of function find_next_siblings.
        Givven 2 spots of same color, one should be able to
        find the other if they are adjacent.
        2 spots, same color, vertical
    """
    board9 = Board(9)
    board9.set_position(3, 1, "B")
    board9.set_position(3, 2, "B")
    result = board9.find_next_siblings((3, 1), None, [])
    assert result[0] == (3, 2)


def test_find_next_siblings_2_hor():
    """
        Test functionality of function find_next_siblings.
        Givven 2 spots of same color, one should be able to
        find the other if they are adjacent.
        2 spots, same color, horizontal
    """
    board9 = Board(9)
    board9.set_position(3, 3, "B")
    board9.set_position(2, 3, "B")
    board9.set_position(4, 3, "B")
    result = board9.find_next_siblings((3, 3), None, [])
    assert result == [(2, 3), (4, 3)]


def test_find_next_siblings_2_vert():
    """
        Test functionality of function find_next_siblings.
        Givven 2 spots of same color, one should be able to
        find the other if they are adjacent.
        2 spots, same color, vertical
    """
    board9 = Board(9)
    board9.set_position(4, 3, "B")
    board9.set_position(4, 4, "B")
    board9.set_position(4, 2, "B")
    result = board9.find_next_siblings((4, 3), None, [])
    assert result == [(4, 4), (4, 2)]


def test_find_next_siblings_3_vert_hor():
    """
        Test functionality of function find_next_siblings.
        Givven 4 spots of same color, one should be able to
        find the other if they are adjacent.
        4 spots, same color, vertical and horizontal
    """
    board9 = Board(9)
    board9.set_position(4, 2, "B")
    board9.set_position(4, 3, "B")
    board9.set_position(4, 4, "B")
    board9.set_position(3, 3, "B")
    result = board9.find_next_siblings((4, 3), None, [])

    # sorting the result data and the assumed data to have
    # a common structured data to check
    assert sorted(result) == sorted([(4, 4), (4, 2), (3, 3)])


def test_find_next_siblings_4_vert_hor():
    """
        Test functionality of function find_next_siblings.
        Givven 5 spots of same color, one should be able to
        find the other if they are adjacent.
        5 spots, same color, vertical and horizontal
    """
    board9 = Board(9)
    board9.set_position(4, 2, "B")
    board9.set_position(4, 3, "B")
    board9.set_position(4, 4, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(5, 3, "B")
    result = board9.find_next_siblings((4, 3), None, [])

    # sorting the result data and the assumed data to have
    # a common structured data to check
    assert sorted(result) == sorted([(4, 4), (4, 2), (3, 3), (5, 3)])


# ##### CONNECTED GROUPS #####


def test_connected_positions_ver_up():
    """
        Tests if two positions are connected / adjacent intersections.
        Definition: two positions are said to be "adjacent" if
        they are distinct and connected by a horizontal or vertical
        line with no other intersections between them
        Vertical Up
    """

    board9 = Board(9)
    x1 = 2
    y1 = 2
    x2 = 2
    y2 = 3
    board9.set_position(x1, y1, "B")
    board9.set_position(x2, y2, "B")

    result = board9.is_adjacent(x1, y1, x2, y2)
    assert result == True


def test_connected_positions_ver_down():
    """
        Tests if two positions are connected / adjacent intersections.
        Vertical Down
    """

    board9 = Board(9)
    x1 = 3
    y1 = 8
    x2 = 3
    y2 = 7
    board9.set_position(x1, y1, "B")
    board9.set_position(x2, y2, "B")

    result = board9.is_adjacent(x1, y1, x2, y2)
    assert result == True


def test_connected_positions_hor_left():
    """
        Tests if two positions are connected / adjacent intersections.
        Horizontal Left
    """
    board9 = Board(9)
    x1 = 4
    y1 = 2
    x2 = 3
    y2 = 2
    board9.set_position(x1, y1, "B")
    board9.set_position(x2, y2, "B")

    result = board9.is_adjacent(x1, y1, x2, y2)
    assert result == True


def test_false_connection_positions_diagonal():
    """
        Tests false positive
    """

    board9 = Board(9)
    x1 = 5
    y1 = 5
    x2 = 6
    y2 = 6
    board9.set_position(x1, y1, "W")
    board9.set_position(x2, y2, "B")

    with pytest.raises(AttributeError):
        board9.is_adjacent(x1, y1, x2, y2)


def test_disconnected_positions_diagonal():
    """
        Tests if two positions are not connected / adjacent intersections.
        Diagonal
    """

    board9 = Board(9)
    x1 = 5
    y1 = 5
    x2 = 6
    y2 = 6
    board9.set_position(x1, y1, "W")
    board9.set_position(x2, y2, "W")

    result = board9.is_adjacent(x1, y1, x2, y2)

    assert result == False


def test_disconnected_positions_random():
    """
        Tests if two positions are not connected / adjacent intersections.
        Random two points
    """

    board9 = Board(9)
    x1 = 3
    y1 = 8
    x2 = 8
    y2 = 2
    board9.set_position(x1, y1, "W")
    board9.set_position(x2, y2, "W")

    result = board9.is_adjacent(x1, y1, x2, y2)

    assert result == False


def test_disconnected_positions_2steps_hor():
    """
        Tests if two steps away positions are not connected / adjacent intersections.
        Two steps away points
        Horizontal
    """

    board9 = Board(9)
    x1 = 3
    y1 = 3
    x2 = 5
    y2 = 3
    board9.set_position(x1, y1, "W")
    board9.set_position(x2, y2, "W")

    result = board9.is_adjacent(x1, y1, x2, y2)

    assert result == False


def test_disconnected_positions_2steps_vert():
    """
        Tests if two steps away positions are not connected / adjacent intersections.
        Two steps away points
        Vertical
    """

    board9 = Board(9)
    x1 = 5
    y1 = 3
    x2 = 5
    y2 = 5
    board9.set_position(x1, y1, "W")
    board9.set_position(x2, y2, "W")

    result = board9.is_adjacent(x1, y1, x2, y2)

    assert result == False


def test_same_spot_connected():
    """
        Tests if two steps away positions are not connected / adjacent intersections.
        Two steps away points
        Vertical
    """

    board9 = Board(9)
    x1 = 3
    y1 = 3
    x2 = 3
    y2 = 3
    board9.set_position(x1, y1, "W")
    with pytest.raises(Exception):
        board9.set_position(x2, y2, "W")


def test_is_connected_to_adjacent_dots():
    """
        Tests if two adjucent spots are connected
    """
    board9 = Board()
    board9.set_position(5, 6, "B")
    board9.set_position(5, 7, "B")

    result = board9.is_connected_group(5, 6, 5, 7)
    assert result == True


def test_multiple_spots_connected():
    """
        Tests if multiple spots are connected as a group
        Input values: two different spots with more than
        1 leg between each other
    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")

    result = board9.is_connected_group(3, 2, 3, 4)
    assert result == True


def test_multiple_spots_connected_long_leg():
    """
        Tests if multiple spots are connected as a group
        Input values: two different spots with more than
        1 leg between each other
    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")
    board9.set_position(3, 5, "B")
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(6, 5, "B")
    board9.set_position(6, 4, "B")

    result = board9.is_connected_group(2, 2, 6, 4)
    assert result == True


def test_multiple_spots_connected_long_leg_subgrou():
    """
        Tests if multiple spots are connected as a group,
        but are inside of a bigger group.
    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")
    board9.set_position(3, 5, "B")
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(6, 5, "B")
    board9.set_position(6, 4, "B")

    result = board9.is_connected_group(3, 3, 4, 5)
    assert result == True


def test_multiple_spots_connected_long_leg_false():
    """
        Tests if multiple spots are not connected as a group
        Input values: two different spots with same color with
        more than 1 leg between each other
    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")
    board9.set_position(3, 5, "B")
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(6, 5, "B")
    board9.set_position(6, 4, "B")

    result = board9.is_connected_group(2, 2, 7, 6)
    assert result == False


def test_multiple_spots_connected_long_leg_with_1deadend():
    """
        Tests if multiple spots are connected as a group, but
        there is a dead end sibling

    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")
    board9.set_position(3, 5, "B")
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(6, 5, "B")
    board9.set_position(6, 4, "B")
    board9.set_position(6, 3, "B")
    board9.set_position(7, 3, "B")
    board9.set_position(7, 2, "B")

    # A dead end sibling
    board9.set_position(4, 6, "B")

    result = board9.is_connected_group(2, 2, 7, 2)
    assert result == True


def test_multiple_spots_connected_long_leg_with_M_deadends():
    """
        Tests if multiple spots are connected as a group, but
        there are dead end siblings

    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")
    board9.set_position(3, 5, "B")
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(6, 5, "B")
    board9.set_position(6, 4, "B")
    board9.set_position(6, 3, "B")
    board9.set_position(7, 3, "B")
    board9.set_position(7, 2, "B")

    # A dead end sibling
    board9.set_position(4, 6, "B")
    board9.set_position(4, 7, "B")
    board9.set_position(4, 8, "B")

    result = board9.is_connected_group(2, 2, 7, 2)
    assert result == True


def test_multiple_spots_connected_long_leg_closed_circle_siblings():
    """
        Tests if multiple spots are connected as a group, but
        there are dead end siblings

    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")
    board9.set_position(3, 5, "B")
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(6, 5, "B")
    board9.set_position(6, 4, "B")
    board9.set_position(6, 3, "B")
    board9.set_position(7, 3, "B")
    board9.set_position(7, 2, "B")

    # Closed sibling circle
    board9.set_position(4, 6, "B")
    board9.set_position(4, 7, "B")
    board9.set_position(5, 7, "B")
    board9.set_position(6, 7, "B")
    board9.set_position(6, 6, "B")

    result = board9.is_connected_group(2, 2, 7, 2)
    assert result == True


def test_multiple_spots_not_connected_long_leg_closed_circle_siblings():
    """
        Tests if multiple spots are connected as a group, but
        there are dead end siblings

    """

    board9 = Board(9)
    # setting multiple stones with same color
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    board9.set_position(3, 3, "B")
    board9.set_position(3, 4, "B")
    board9.set_position(3, 5, "B")
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(6, 5, "B")
    board9.set_position(6, 4, "B")
    board9.set_position(6, 3, "B")
    board9.set_position(7, 3, "B")
    board9.set_position(7, 2, "B")

    # Closed sibling circle
    board9.set_position(4, 6, "B")
    board9.set_position(4, 7, "B")
    board9.set_position(5, 7, "B")
    board9.set_position(6, 7, "B")
    board9.set_position(6, 6, "B")

    result = board9.is_connected_group(2, 2, 8, 2)
    assert result == False


# ##### LIBERTIES #####


def test_single_spot_liberties():
    """
        Tests if on single spot on an empty board
        has liberties and how many of them.
        Expected result: True
    """

    board9 = Board(9)
    board9.set_position(4, 4, "B")
    result = board9.has_liberties(4, 4, "B")
    assert result[0] == True


def test_single_spot_surrounded_liberties():
    """
        Tests if on single spot surrounded with other
        color spots has liberties
        Expected result: False
    """

    board9 = Board(9)
    board9.set_position(4, 4, "B")
    board9.set_position(4, 3, "W")
    board9.set_position(4, 5, "W")
    board9.set_position(3, 4, "W")
    board9.set_position(5, 4, "W")
    result = board9.has_liberties(4, 4, "B")
    assert result[0] == False
    assert result[1] == []


def test_2_spots_liberties_vert():
    """
        Tests if single spot on an empty board
        has liberties and how many of them. Vertical
        Expected result: True
    """

    board9 = Board(9)
    board9.set_position(4, 4, "B")
    board9.set_position(4, 5, "B")
    result = board9.has_liberties(4, 4, "B")
    assumed_lib_result = sorted([(4, 3), (3, 4), (3, 5), (4, 6), (5, 5), (5, 4)])

    assert result[0] == True
    assert sorted(result[1]) == assumed_lib_result


def test_3_spots_liberties_hor():
    """
        Tests if single spot on an empty board
        has liberties and how many of them. Horizontal
        Expected result: True and a list of Liberties
    """

    board9 = Board(9)
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    result = board9.has_liberties(4, 5, "B")
    assumed_lib_result = sorted([(4, 4), (3, 5), (4, 6), (5, 6), (6, 5), (5, 4)])

    assert result[0] == True
    assert sorted(result[1]) == assumed_lib_result


def test_3_spots_liberties_L_shaped():
    """
        Tests if single spot on an empty board
        has liberties and how many of them. L shaped
        Expected result: True and a list of Liberties
        Started from bottom
    """

    board9 = Board(9)
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(4, 4, "B")
    result = board9.has_liberties(4, 4, "B")
    assumed_lib_result = sorted(
        [(4, 3), (3, 4), (3, 5), (4, 6), (5, 6), (6, 5), (5, 4)]
    )

    assert result[0] == True
    assert sorted(result[1]) == assumed_lib_result


def test_3_spots_liberties_L_shaped_from_center():
    """
        Tests if single spot on an empty board
        has liberties and how many of them. L shaped
        Expected result: True and a list of Liberties
        Started from bottom
    """

    board9 = Board(9)
    board9.set_position(4, 5, "B")
    board9.set_position(5, 5, "B")
    board9.set_position(4, 4, "B")
    result = board9.has_liberties(4, 5, "B")
    assumed_lib_result = sorted(
        [(4, 3), (3, 4), (3, 5), (4, 6), (5, 6), (6, 5), (5, 4)]
    )

    assert result[0] == True
    assert sorted(result[1]) == assumed_lib_result


def test_spots_liberties_L_shaped_from_Y0():
    """
        Tests if multiple spots on an empty board
        has liberties and how many of them. L shaped
        Expected result: True and a list of Liberties
        Started from Y=0
    """

    board9 = Board(9)
    board9.set_position(2, 0, "B")
    board9.set_position(2, 1, "B")
    board9.set_position(2, 2, "B")
    board9.set_position(3, 2, "B")
    result = board9.has_liberties(2, 0, "B")
    assumed_lib_result = sorted(
        [(1, 1), (1, 0), (1, 2), (2, 3), (3, 3), (4, 2), (3, 1), (3, 0)]
    )

    assert result[0] == True
    assert sorted(result[1]) == assumed_lib_result


def test_spots_liberties_L_shaped_from_X0():
    """
        Tests if multiple spots on an empty board
        has liberties and how many of them. L shaped
        Expected result: True and a list of Liberties
        Started from X=0
    """

    board9 = Board(9)
    board9.set_position(0, 4, "B")
    board9.set_position(1, 4, "B")
    board9.set_position(1, 5, "B")
    board9.set_position(1, 6, "B")
    result = board9.has_liberties(0, 4, "B")
    assumed_lib_result = sorted(
        [(0, 3), (1, 3), (2, 4), (2, 5), (2, 6), (1, 7), (0, 6), (0, 5)]
    )

    assert result[0] == True
    assert sorted(result[1]) == assumed_lib_result
