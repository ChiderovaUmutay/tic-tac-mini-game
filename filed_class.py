empty_cell_vertical_line_template = f"{' ' * 6}|"


class Field:
    percent_nums_data = {3: 50, 4: 50, 5: 45, 6: 40, 7: 32, 8: 30, 9: 26, 10: 24}

    def __init__(self, size):
        self.size = size
        self.last_col = self.size - 1
        self.percent_of_size_num = self.percent_nums_data.get(self.size)
        self.horizontal_lines_count = self.calculate_horizontal_lines_count(size=self.size,
                                                                            percent=self.percent_of_size_num)
        self.field = self.create_game_field()

    @staticmethod
    def calculate_horizontal_lines_count(size, percent):
        count = size + (size * (size * percent / 100))
        return round(count)

    def create_game_field(self):
        header_text = ''
        horizontal_text = ''
        for header_num in range(0, self.size):
            header_indentation_num = 5 if header_num < 3 else 6
            header_text += f"{' ' * header_indentation_num}{header_num}"
            vertical_lines = self.create_vertical_lines()
            horizontal_lines_count = 0 if header_num == (self.size - 1) else self.horizontal_lines_count
            lines = f"{vertical_lines}\n{' ' * 3}{'--' * horizontal_lines_count}\n"
            horizontal_text += f"{header_num}{lines}"
        return f"{header_text}\n{horizontal_text}"

    def create_vertical_lines(self):
        horizontal_lines = ''
        for col in range(0, self.size):
            horizontal_lines += empty_cell_vertical_line_template if col != self.last_col else ""
        return horizontal_lines

    def __str__(self):
        print(self.field)


def user_input(message=""):
    while True:
        user_choice = input(f"{message}: \n")
        try:
            user_choice = int(user_choice)
            if user_choice < 3 or user_choice > 10:
                message = "Enter correct value"
                continue
        except ValueError:
            message = "Enter only integers"
            continue
        else:
            break
    return user_choice


if __name__ == "__main__":
    field_size = user_input(message="Enter size of filed")
    game = Field(size=field_size)
    game.__str__()
