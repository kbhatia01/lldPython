from basePizzza import BasePizzza
from cheese import Cheese
from Mushroom import Mushroom
from Panner import Panner


if __name__ == '__main__':
    imput = "Base"
    Addons = "Panner, Cheese, Mushroom"

    adddons = Addons.split(", ")

    # Implement Builder..


    Pza = BasePizzza()
    Panner_pza = Panner(Pza)

    print(Panner_pza.get_price())