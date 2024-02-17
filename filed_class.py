from helpers.info_messages import ENTER_CORRECT_COORDS_MESSAGE, CELL_IS_OCCUPIED_MESSAGE
from helpers.variables import empty_field_vertical_line_template, \
    filled_field_vertical_line_template, \
    percent_nums_data, \
    X_SYMBOL, \
    O_SYMBOL


class Field:
    def __init__(self, size: int) -> None:
        self.size = size
        self.last_col = size - 1
        self.percent_of_size_num = percent_nums_data.get(size)
        self.horizontal_lines_count = round(size + (size * (size * self.percent_of_size_num / 100)))
        self.field = None
        self.filled_cells = {X_SYMBOL: [], O_SYMBOL: []}
        self.free_symbol_controller = {X_SYMBOL: True, O_SYMBOL: True}

    def add_user_coords(self, symbol: str, coords: str) -> str or None:
        user_coords = [int(data) for data in coords if data.isdigit()]
        if len(user_coords) != 2:
            return ENTER_CORRECT_COORDS_MESSAGE
        user_coords += symbol
        if user_coords not in self.filled_cells.get(X_SYMBOL) and user_coords not in self.filled_cells.get(O_SYMBOL):
            self.fixate_user_coords(symbol=symbol, coords=user_coords)
        else:
            return CELL_IS_OCCUPIED_MESSAGE

    def fixate_user_coords(self, symbol: str, coords: list) -> None:
        self.filled_cells.get(symbol).append(coords)

    def create_field(self) -> None:
        header_text, horizontal_text = '', ''
        for header_num in range(0, self.size):
            header_text += self.create_header(col_number=header_num)
            vertical_lines = self.create_vertical_lines(row_num=header_num)
            horizontal_lines = self.create_horizontal_lines(row_num=header_num)
            vertical_and_horizontal_lines = f"{vertical_lines}\n{' ' * 3}{horizontal_lines}\n"
            horizontal_text += f"{header_num}{vertical_and_horizontal_lines}"
        self.field = f"{header_text}\n{horizontal_text}"

    @staticmethod
    def create_header(col_number: int) -> str:
        header_indentation_num = 5 if col_number < 3 else 6
        return f"{' ' * header_indentation_num}{col_number}"

    def create_vertical_lines(self, row_num: int) -> str:
        vertical_lines = ''
        all_filled_cells = self.get_filled_cells()
        for col in range(0, self.size):
            for coords_data in all_filled_cells:
                if coords_data[0:2] == [col, row_num]:
                    vertical_lines += self.get_vertical_line(col=col, last_col=self.last_col, symbol=coords_data[-1])
                    break
            else:
                vertical_lines += self.get_vertical_line(col=col, last_col=self.last_col)
        return vertical_lines

    def get_filled_cells(self):
        filled_cells = [coords for coords in self.filled_cells.values()]
        return filled_cells

    @staticmethod
    def get_vertical_line(col: int, last_col: int, symbol=None) -> str:
        if symbol:
            return filled_field_vertical_line_template % symbol if col == last_col \
                else f"{filled_field_vertical_line_template % symbol}|"
        else:
            return empty_field_vertical_line_template if col != last_col else ""

    def create_horizontal_lines(self, row_num: int) -> str:
        horizontal_lines_count = 0 if row_num == (self.size - 1) else self.horizontal_lines_count
        return '--' * horizontal_lines_count

    def __str__(self) -> None:
        print(self.field)
