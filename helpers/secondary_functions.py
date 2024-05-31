from helpers.info_messages import (ENTER_CORRECT_FIELD_SIZE_MESSAGE,
                                   ENTER_NUMBERS_ONLY_MESSAGE,
                                   ENTER_FIELD_SIZE_MESSAGE,
                                   ENTER_PLAYERS_QTY_MESSAGE,
                                   ENTER_CORRECT_PLAYERS_QTY_MESSAGE,
                                   NEW_GAME_START_MESSAGE)
from helpers.variables import YES_WORD


def user_field_size_choice_input() -> int:
    message = ENTER_FIELD_SIZE_MESSAGE
    while True:
        user_choice = input(message)
        try:
            user_choice = int(user_choice)
            if 3 <= user_choice <= 10:
                return user_choice
            message = ENTER_CORRECT_FIELD_SIZE_MESSAGE
        except ValueError:
            message = ENTER_NUMBERS_ONLY_MESSAGE


def user_players_qty_choice_input() -> int:
    message = ENTER_PLAYERS_QTY_MESSAGE
    while True:
        try:
            players_qty = input(message)
            players_qty = int(players_qty)
            if 0 < players_qty < 3:
                return players_qty
            message = ENTER_CORRECT_PLAYERS_QTY_MESSAGE
        except ValueError:
            message = ENTER_NUMBERS_ONLY_MESSAGE

def new_game_start_input() -> int:
    message = input(NEW_GAME_START_MESSAGE)
    if message == YES_WORD:
        return True
    return False
