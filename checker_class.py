from filed_class import Field
from helpers.variables import winning_combinations


class Checker:
    def __init__(self, filed: Field):
        self.field = filed
        self.combine_length = 0
        self.winning_combinations = winning_combinations

    def get_winning_combination(self):
        if self.field.size > 3:
            self.combine_length = self.field.size - 3
            self.winning_combinations = self.calculate_winning_combinations()

    def calculate_winning_combinations(self) -> dict:
        for key, coords_lists in winning_combinations.items():
            for c_index, coords in enumerate(coords_lists):
                if (key != "diagonally") or (key == "diagonally" and c_index == 0):
                    for i in range(1, self.combine_length + 1):
                        new_coords = self.get_new_coords(line=key, last_coords_data=coords[-1])
                        coords.append(new_coords)
                else:
                    coords = self.increase_coords_first_value(coords=coords)
                    self.add_new_coords_to_right_diagonally_data(coords=coords)
            for i in range(self.combine_length):
                new_coords_data = self.add_new_coords_data(line=key, coords=coords_lists[-1])
                coords_lists.append(new_coords_data) if new_coords_data else None
        return winning_combinations

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

    def add_new_coords_to_right_diagonally_data(self, coords: list) -> None:
        for i in list(reversed(range(self.combine_length))):
            data = coords[i]
            new_coords_data = [data[1], data[0]]
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
