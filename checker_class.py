from player_class import Player
from win_combination_class import WinningCombinationClass


class Checker(WinningCombinationClass):

    def checker(self, player: Player):
        player_combinations = self.field.filled_cells.get(player.symbol)
        cleaned_combinations = [data[0:2] for data in player_combinations]
        for combinations in self.winning_combinations.values():
            for combination in combinations:
                win = [data for data in combination if data in cleaned_combinations]
                if len(win) == len(combination):
                    return True
