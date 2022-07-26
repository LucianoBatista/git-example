import pandas as pd


def get_data():
    numbers = [7, 8, 9, 10, 11, 12]
    persons = ["guilherme", "pedro", "fernando", "maria", "antônia", "joana"]

    dict_to_df = {"names": persons, "numbers": numbers}

    df = pd.DataFrame(dict_to_df)

    return df
