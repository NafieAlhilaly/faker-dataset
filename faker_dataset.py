from typing import Optional, Union
from faker import Faker
import pandas as pd
from random import randint


class FakeDataset:
    def simple_dataset(self, n_rows: int = 7, as_df: bool = False) -> Optional[Union[dict, pd.DataFrame]]:

        """
        generate simple dataset with a given number of rows.

        :param n_rows: number of rows
        :param as_df: if true return as DataFrame, otherwise return a dictionary

        :return:
            if as_df == False: return a dictionary, else a pandas DataFrame
        """

        faker = Faker()

        data = {
            "name": [faker.name() for _ in range(n_rows)],
            "email": [faker.email() for _ in range(n_rows)],
            "age": [randint(20, 60) for _ in range(n_rows)],
            "address": [faker.address() for _ in range(n_rows)],
            "salary": [randint(2000, 50000) for _ in range(n_rows)],
            "company": [faker.company() for _ in range(n_rows)]
        }
        if as_df:
            return pd.DataFrame(data)

        return data


dataset = FakeDataset()
print(dataset.simple_dataset(n_rows=9, as_df=True))
