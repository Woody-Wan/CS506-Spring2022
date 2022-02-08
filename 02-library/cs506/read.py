import pandas as pd
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    return pd.read_csv(csv_file_path)
