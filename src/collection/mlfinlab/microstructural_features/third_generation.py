# Copyright 2019, Hudson and Thames Quantitative Research
# All rights reserved
# Read more: https://github.com/hudson-and-thames/mlfinlab/blob/master/LICENSE.txt

"""
Third generation models implementation (VPIN).
"""

import pandas as pd

from mlfinlab.util import devadarsh


def get_vpin(volume: pd.Series, buy_volume: pd.Series, window: int = 1) -> pd.Series:
    """
    Advances in Financial Machine Learning, p. 292-293.

    Get Volume-Synchronized Probability of Informed Trading (VPIN) from bars.

    :param volume: (pd.Series) Bar volume.
    :param buy_volume: (pd.Series) Bar volume classified as buy (either tick rule, BVC or aggressor side methods applied).
    :param window: (int) Estimation window.
    :return: (pd.Series) VPIN series.
    """

    devadarsh.track('get_vpin')

    sell_volume = volume - buy_volume
    volume_imbalance = abs(buy_volume - sell_volume)

    return volume_imbalance.rolling(window=window).mean() / volume
