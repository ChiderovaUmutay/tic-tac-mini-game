from random import randint

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
    def get_bot_coords(last_col_num: int) -> str:
        col = randint(0, last_col_num)
        row = randint(0, last_col_num)
        return f"{col} {row}"

    @staticmethod
    def display(coords: str) -> None:
        print(coords)
