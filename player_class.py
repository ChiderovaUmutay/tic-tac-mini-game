from filed_class import Field
from helpers.info_messages import ENTER_FIELD_SIZE_MESSAGE, \
    ENTER_COORDS_MESSAGE, \
    CHOOSE_SYMBOL_MESSAGE, \
    CHOOSE_CORRECT_SYMBOL_MESSAGE
from helpers.secondary_functions import user_input
from helpers.variables import X_SYMBOL, O_SYMBOL


class Player:
    def __init__(self, filed_obj):
        self.field = filed_obj
        self.symbol = None

    def choose_symbol(self) -> None:
        message = CHOOSE_SYMBOL_MESSAGE
        while True:
            symbol = input(message)
            if symbol == X_SYMBOL or symbol == O_SYMBOL:
                self.symbol = symbol
                break
            message = CHOOSE_CORRECT_SYMBOL_MESSAGE
            continue

    def step(self):
        message = ENTER_COORDS_MESSAGE
        while True:
            user_coords = input(message)
            result = self.field.add_user_coords(symbol=self.symbol, coords=user_coords)
            if isinstance(result, str):
                message = result
                continue
            else:
                message = ENTER_COORDS_MESSAGE
                self.field.create_field(symbol=self.symbol)
                self.field.__str__()


if __name__ == "__main__":
    field_size = user_input(message=ENTER_FIELD_SIZE_MESSAGE)
    field = Field(size=field_size)
    field.create_field()
    field.__str__()
    print("Start game")
    player = Player(filed_obj=field)
    player.choose_symbol()
    player.step()
