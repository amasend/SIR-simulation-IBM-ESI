import random
import pandas as pd
import numpy as np


def test(cols_size, rows_size):
    table = []

    for i in range(rows_size):
        table.append([random.randint(0, 100) for x in range(rows_size)])

    x = np.array(table, np.int32)
    df = pd.DataFrame(x, index=range(rows_size), columns=range(cols_size))
    print(df)


test(10, 10)
