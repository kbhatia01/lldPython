from design_pattrens.factory.archer import Archer
from design_pattrens.factory.knight import Knight


class CharacterFactory:

    @staticmethod
    def create_player(player_type):
        if player_type == 'Knight':
            return Knight()

        if player_type == 'Archer':
            return Archer()

