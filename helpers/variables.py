percent_nums_data = {3: 50, 4: 50, 5: 45, 6: 40, 7: 32, 8: 30, 9: 26, 10: 24}

empty_field_vertical_line_template = f"{' ' * 6}|"
filled_field_vertical_line_template = f"{' ' * 3}%s{' ' * 2}"

X_SYMBOL = "X"
O_SYMBOL = "0"

winning_combinations = {
    "vertical": [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]]],
    "horizontal": [[[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]]],
    "diagonally": [[[0, 0], [1, 1], [2, 2]], [[2, 0], [1, 1], [0, 2]]]
}

DEFAULT_LEN_OF_WINNING_COORDS = 3
MIN_LEN_DIAGONAL_WINNING_COMBINATIONS_LIST = 5