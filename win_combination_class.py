from filed_class import Field
from helpers.variables import (winning_combinations,
                               DEFAULT_LEN_OF_WINNING_COORDS,
                               MIN_LEN_DIAGONAL_WINNING_COMBINATIONS_LIST)


class WinningCombinationClass:
    def __init__(self, filed: Field):
        self.field = filed
        self.combine_length = 0
        self.winning_combinations = winning_combinations

    def get_winning_combination(self):
        if self.field.size > 3:
            self.combine_length = self.field.size - DEFAULT_LEN_OF_WINNING_COORDS
            self.calculate_winning_combinations()

    def calculate_winning_combinations(self):
        for key, coords_lists in winning_combinations.items():
            for c_index, coords in enumerate(coords_lists):
                if (key != "diagonally") or (key == "diagonally" and c_index == 0):
                    for _ in range(self.combine_length):
                        new_coords = self.get_new_coords(line=key, last_coords_data=coords[-1])
                        coords.append(new_coords)
                else:
                    coords = self.increase_coords_first_value(coords=coords)
                    self.add_right_diagonally_new_coords(coords=coords)
            for _ in range(self.combine_length):
                new_coords_data = self.add_new_coords_data(line=key, coords=coords_lists[-1])
                coords_lists.append(new_coords_data) if new_coords_data else None
            if key == "diagonally" and self.field.size > 5:
                new_diagonal_coords = self.add_diagonal_new_coords(coords_data=coords_lists)
                for coords in new_diagonal_coords:
                    coords_lists.append(coords)
        self.winning_combinations = winning_combinations
    @staticmethod
    def get_new_coords(line: str, last_coords_data: list) -> list:
        new_coords_data = {"vertical": [last_coords_data[0], last_coords_data[1] + 1],
                           "horizontal": [last_coords_data[0] + 1, last_coords_data[1]],
                           "diagonally": [last_coords_data[0] + 1, last_coords_data[1] + 1]}
        return new_coords_data.get(line)

    def increase_coords_first_value(self, coords: list) -> list:
        for d_index, data in enumerate(coords):
            coords[d_index] = [data[0] + self.combine_length, data[1]]
        return coords

    def add_right_diagonally_new_coords(self, coords: list) -> None:
        for i in list(reversed(range(self.combine_length))):
            try:
                data = coords[i]
                new_coords_data = [data[1], data[0]]
            except IndexError:
                data = coords[-1]
                new_coords_data = [data[0] - 1, data[1] + 1]
            coords.append(new_coords_data)

    @staticmethod
    def add_new_coords_data(line: str, coords: list) -> list:
        new_data = []
        for data in coords:
            if line == "vertical":
                new_data.append([data[0] + 1, data[1]])
            elif line == "horizontal":
                new_data.append(([data[0], data[1] + 1]))
        return new_data

    def add_diagonal_new_coords(self, coords_data: list) -> (list, list):
        winning_combinations_qty = self.field.size - MIN_LEN_DIAGONAL_WINNING_COMBINATIONS_LIST
        new_left_coords = self.create_new_diagonals_combinations(up_num=1,
                                                                 low_num=1,
                                                                 coords_data=coords_data[0],
                                                                 combinations_qty=winning_combinations_qty)
        new_right_coords = self.create_new_diagonals_combinations(up_num=-1,
                                                                 low_num=1,
                                                                 coords_data=coords_data[1],
                                                                 combinations_qty=winning_combinations_qty)
        return new_left_coords + new_right_coords

    @staticmethod
    def create_new_diagonals_combinations(up_num: int, low_num: int, coords_data: list, combinations_qty: int) -> list:
        upper_coords = [coords_data]
        lower_coords = [coords_data]
        for index in range(combinations_qty):
            up = [[data[0] + up_num, data[1]] for data in upper_coords[index][:-1]]
            low = [[data[0], data[1] + low_num] for data in lower_coords[index][:-1]]
            upper_coords.append(up)
            lower_coords.append(low)
        new_coords = upper_coords[1:] + lower_coords[1:]
        return new_coords