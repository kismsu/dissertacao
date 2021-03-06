# Copyright 2019, Hudson and Thames Quantitative Research
# All rights reserved
# Read more: https://github.com/hudson-and-thames/mlfinlab/blob/master/LICENSE.txt

"""
Various miscellaneous microstructural features (VWAP, average tick size).
"""

import numpy as np

from mlfinlab.util import devadarsh


def vwap(dollar_volume: list, volume: list) -> float:
    """
    Get Volume Weighted Average Price (VWAP).

    :param dollar_volume: (list) Dollar volumes.
    :param volume: (list) Trades sizes.
    :return: (float) VWAP value.
    """

    devadarsh.track('vwap')

    return sum(dollar_volume) / sum(volume)


def get_avg_tick_size(tick_size_arr: list) -> float:
    """
    Get average tick size in a bar.

    :param tick_size_arr: (list) Trade sizes.
    :return: (float) Average trade size.
    """

    devadarsh.track('get_avg_tick_size')

    return np.mean(tick_size_arr)
