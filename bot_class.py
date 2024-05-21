from random import randint

from checker_class import Checker
from filed_class import Field
from helpers.info_messages import ENTER_FIELD_SIZE_MESSAGE
from helpers.secondary_functions import user_input
from player_class import Player


class Bot(Player):

    def step(self):
        last_col = self.field.last_col
        while True:
            coords = self.get_bot_coords(last_col_num=last_col)
            result = self.field.add_user_coords(symbol=self.symbol, coords=coords)
            if not isinstance(result, str):
                self.field.create_field()
                self.display(coords=coords)
                self.field.__str__()
                break

    @staticmethod
    def get_bot_coords(last_col_num) -> str:
        col = randint(0, last_col_num)
        row = randint(0, last_col_num)
        return f"{col} {row}"

    @staticmethod
    def display(coords: str) -> None:
        print(coords)


if __name__ == "__main__":
    field_size = user_input(message=ENTER_FIELD_SIZE_MESSAGE)
    field = Field(size=field_size)
    field.create_field()
    field.__str__()
    player = Player(filed_obj=field)
    player.choose_symbol()
    bot = Bot(filed_obj=field)
    bot.choose_symbol(bot=True)
    checker = Checker(field)
    checker.get_winning_combination()
    while True:
        player.step()
        result = checker.checker(player=player)
        if result:
            print("User win")
            break
        bot.step()
        result = checker.checker(player=bot)
        if result:
            print("Bot win")
            break
