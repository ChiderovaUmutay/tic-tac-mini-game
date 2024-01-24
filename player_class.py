from filed_class import Field
from helpers.info_messages import ENTER_COORDS_MESSAGE, CHOOSE_SYMBOL_MESSAGE, CHOOSE_CORRECT_SYMBOL_MESSAGE, \
    SYMBOL_IS_OCCUPIED_MESSAGE
from helpers.variables import X_SYMBOL, O_SYMBOL


class Player:
    def __init__(self, filed_obj: Field):
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

    def step(self) -> None:
        message = ENTER_COORDS_MESSAGE
        while True:
            user_coords = input(message)
            result = self.field.add_user_coords(symbol=self.symbol, coords=user_coords)
            if isinstance(result, str):
                message = result
                continue
            else:
                self.field.create_field(symbol=self.symbol)
                self.field.__str__()
                break
