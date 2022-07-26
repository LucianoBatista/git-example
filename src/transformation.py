import pandas as pd


def get_data():
    numbers = [13, 14, 15, 16, 17, 18]
    persons = ["Manuel", "pedro", "fernando", "maria", "antônia", "joana"]

    dict_to_df = {"names": persons, "numbers": numbers}

    df = pd.DataFrame(dict_to_df)

    return df
