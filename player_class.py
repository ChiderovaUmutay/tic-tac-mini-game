from filed_class import Field
from helpers.info_messages import (ENTER_COORDS_MESSAGE,
                                   CHOOSE_SYMBOL_MESSAGE,
                                   CHOOSE_CORRECT_SYMBOL_MESSAGE,
                                   SYMBOL_IS_OCCUPIED_MESSAGE,
                                   ENTER_YOUR_NAME)
from helpers.variables import X_SYMBOL, O_SYMBOL, BOT_NAME


class Player:
    symbol = None
    name = None

    def __init__(self, filed_obj: Field):
        self.field = filed_obj

    def create_name(self, bot=False):
        self.name = input(ENTER_YOUR_NAME) if not bot else BOT_NAME

    def choose_symbol(self, bot=False) -> None:
        if not bot:
            self.user_choose_symbol()
        else:
            self.add_bot_symbol()

    def user_choose_symbol(self):
        message = CHOOSE_SYMBOL_MESSAGE
        while True:
            symbol = input(message)
            if symbol == X_SYMBOL or symbol == O_SYMBOL:
                if self.field.free_symbol_controller.get(symbol):
                    self.symbol = symbol
                    self.field.free_symbol_controller[symbol] = False
                    break
                else:
                    message = SYMBOL_IS_OCCUPIED_MESSAGE
                    continue
            message = CHOOSE_CORRECT_SYMBOL_MESSAGE
            continue

    def add_bot_symbol(self):
        free_symbol = [symbol for symbol, bool_val in self.field.free_symbol_controller.items() if bool_val is True]
        self.symbol = free_symbol[0]

    def step(self) -> None:
        message = ENTER_COORDS_MESSAGE
        while True:
            user_coords = input(message)
            result = self.field.add_user_coords(symbol=self.symbol, coords=user_coords)
            if isinstance(result, str):
                message = result
                continue
            else:
                self.field.create_field()
                self.field.__str__()
                break
