import math
import random as rm

class GameCubes:
    def __init__(self, distribution):
        self._distribution = distribution

        self._check_correct_distribution()

    def roll_of_dice(self):
        cdf = self._calculate_cdf()

        random_point = rm.random()

        for i, interval_border in enumerate(cdf):
            if math.isclose(interval_border, random_point) or (random_point < interval_border):
                return i + 2

    def _calculate_cdf(self):
        cumsum = 0
        cdf = []

        percentages = self._calculate_percentages()

        for p in percentages:
            cumsum += p

            cdf.append(cumsum / 100)

        return cdf

    def _calculate_percentages(self):
        return [100*percent for percent in self._distribution]

    def _check_correct_distribution(self):
        if math.fsum(self._distribution) != 1:
            raise ValueError('Сумма вероятностей должна быть равна 1')