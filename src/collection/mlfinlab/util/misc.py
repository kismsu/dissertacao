# Copyright 2019, Hudson and Thames Quantitative Research
# All rights reserved
# Read more: https://github.com/hudson-and-thames/mlfinlab/blob/master/LICENSE.txt

"""
Various useful functions
"""
# pylint: disable=invalid-name

import pandas as pd
import numpy as np


def crop_data_frame_in_batches(df: pd.DataFrame, chunksize: int):
    """
    Splits df into chunks of chunksize.

    :param df: (pd.DataFrame) Dataframe to split.
    :param chunksize: (int) Number of rows in chunk.
    :return: (list) Chunks (pd.DataFrames).
    """

    generator_object = []
    for _, chunk in df.groupby(np.arange(len(df)) // chunksize):
        generator_object.append(chunk)

    return generator_object
