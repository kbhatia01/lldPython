from design_pattrens.stratergy.Factory.SortingFactory import SortingFactory


class Sorter:

    def sort_data(self, data, algo):
        stratergy = SortingFactory.getSortingObj(algo)
        stratergy.sort(data)
