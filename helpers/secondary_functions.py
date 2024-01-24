from helpers.info_messages import ENTER_CORRECT_FIELD_SIZE_MESSAGE, ENTER_NUMBERS_ONLY_MESSAGE


def user_input(message: str) -> int:
    while True:
        user_choice = input(message)
        try:
            user_choice = int(user_choice)
            if 3 <= user_choice <= 10:
                return user_choice
            message = ENTER_CORRECT_FIELD_SIZE_MESSAGE
            continue
        except ValueError:
            message = ENTER_NUMBERS_ONLY_MESSAGE
            continue