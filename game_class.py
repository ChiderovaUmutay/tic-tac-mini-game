from random import shuffle

from bot_class import Bot
from checker_class import Checker
from filed_class import Field
from helpers.info_messages import DRAW_RESULT_MESSAGE, PLAYER_WIN_MESSAGE
from helpers.secondary_functions import (user_field_size_choice_input,
                                         user_players_qty_choice_input,
                                         new_game_start_input)
from player_class import Player


class Game:
    field = None
    checker = None

    def run(self):
        while True:
            self.create_field_object()
            self.field.__str__()
            self.create_checker_object()
            players = self.create_players()
            player_1, player_2 = players[0], players[1]
            while True:
                result_1 = self.do_step(player=player_1)
                if not result_1:
                    break
                result_2 = self.do_step(player=player_2)
                if not result_2:
                    break
            answer = new_game_start_input()
            if not answer:
                break
    def create_field_object(self):
        field_size = user_field_size_choice_input()
        self.field = Field(size=field_size)
        self.field.create_field()

    def create_checker_object(self):
        self.checker = Checker(self.field)
        self.checker.get_winning_combination()

    def create_players(self) -> list:
        players_qty = user_players_qty_choice_input()
        players = [self.create_player(player_class=Player)] #player_1
        kwargs = dict(
            player_class=Bot if players_qty == 1 else Player,
            bot=True if players_qty == 1 else False,
        )
        players.append(self.create_player(**kwargs)) #player_2
        shuffle(players)
        return players

    def create_player(self, player_class: [Player], bot=False):
        player = player_class(filed_obj=self.field)
        player.create_name(bot=bot)
        player.choose_symbol(bot=bot)
        return player

    def do_step(self, player):
        player.step()
        result = self.checker.checker(player=player)
        if result:
            self.display(message=PLAYER_WIN_MESSAGE.format(player.name))
            return False
        draw_result = self.checking_on_draw()
        return draw_result

    def checking_on_draw(self):
        filled_cells = self.field.get_filled_cells()
        if len(filled_cells) == (self.field.size * self.field.size):
            self.display(message=DRAW_RESULT_MESSAGE)
            return False
        return True

    @staticmethod
    def display(message: str) -> None:
        print(message)


if __name__ == '__main__':
    Game().run()
