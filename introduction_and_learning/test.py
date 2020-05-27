__all__ = [
    'matrix'
]

import random
import pandas as pd
import numpy as np


def matrix(cols_size: int, rows_size: int) -> 'pd.DataFrame':
    """
    Generate matrix of random numbers between 0 and 100 of size passed to
    function arguments.

    Parameters
    ----------
    cols_size: int, required
        Number of columns in matrix.
    rows_size: int, required
        Number of rows in matrix.

    Returns
    -------
    Function returns matrix of dimension cols_size x rows_size,
    filled with random generated numbers. The matrix is instance of pandas'
    DataFrame object.

    Example
    -------
    >>> array = matrix(5,5)
    """
    table = []

    for i in range(rows_size):
        table.append([random.randint(0, 100) for x in range(rows_size)])

    x = np.array(table, np.int32)
    df = pd.DataFrame(x, index=range(rows_size), columns=range(cols_size))

    return df
