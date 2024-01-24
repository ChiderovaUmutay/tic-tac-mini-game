from helpers.info_messages import ENTER_CORRECT_COORDS_MESSAGE, CELL_IS_OCCUPIED_MESSAGE
from helpers.variables import empty_field_vertical_line_template, \
    filled_field_vertical_line_template, \
    percent_nums_data, \
    X_SYMBOL, \
    O_SYMBOL


class Field:
    def __init__(self, size):
        self.size = size
        self.last_col = size - 1
        self.percent_of_size_num = percent_nums_data.get(size)
        self.horizontal_lines_count = round(size + (size * (size * self.percent_of_size_num / 100)))
        self.field = None
        self.filled_cells = {X_SYMBOL: [], O_SYMBOL: []}


    def add_user_coords(self, symbol: str, coords: list) -> str or None:
        user_coords = [int(data) for data in coords if data.isdigit()]
        if len(user_coords) != 2:
            return ENTER_CORRECT_COORDS_MESSAGE
        elif user_coords not in self.filled_cells.get(X_SYMBOL) and user_coords not in self.filled_cells.get(O_SYMBOL):
            self.fixate_user_coords(symbol=symbol, coords=user_coords)
        else:
            return CELL_IS_OCCUPIED_MESSAGE

    def fixate_user_coords(self, symbol: str, coords: list) -> None:
        user_symbol_filled_cells = self.filled_cells.get(symbol)
        user_symbol_filled_cells.append(coords)
        self.filled_cells[symbol] = user_symbol_filled_cells


    def create_field(self, symbol=None) -> None:
        header_text, horizontal_text = '', ''
        for header_num in range(0, self.size):
            header_text += self.create_header(col_number=header_num)
            vertical_lines = self.create_vertical_lines(symbol=symbol, row_num=header_num)
            horizontal_lines = self.create_horizontal_lines(row_num=header_num)
            vertical_and_horizontal_lines = f"{vertical_lines}\n{' ' * 3}{horizontal_lines}\n"
            horizontal_text += f"{header_num}{vertical_and_horizontal_lines}"
        self.field = f"{header_text}\n{horizontal_text}"

    @staticmethod
    def create_header(col_number):
        header_indentation_num = 5 if col_number < 3 else 6
        return f"{' ' * header_indentation_num}{col_number}"

    def create_vertical_lines(self, symbol, row_num) -> str:
        vertical_lines = ''
        for col in range(0, self.size):
            for coords_data in self.filled_cells.get(symbol, []):
                if coords_data == [col, row_num]:
                    vertical_lines += self.get_vertical_line(col=col, last_col=self.last_col, symbol=symbol)
                    break
            else:
                vertical_lines += self.get_vertical_line(col=col, last_col=self.last_col)
        return vertical_lines

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

    def __str__(self):
        print(self.field)
