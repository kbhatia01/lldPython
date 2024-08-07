from design_pattrens.stratergy.BubbleSort import BubbleSort
from design_pattrens.stratergy.MergeSort import MergeSort
from design_pattrens.stratergy.quickSort import QuickSort


class SortingFactory:
    @staticmethod
    def getSortingObj(algo):
        if algo == "Bubble Sort":
            return BubbleSort()
        if algo == "Quick":
            return QuickSort()
        if algo == "Merge":
            return MergeSort()
