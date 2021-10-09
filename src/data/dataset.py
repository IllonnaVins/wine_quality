import pandas as pd
import os
import pathlib

def load_dataset(dataset_name='winequalityN.csv', load_dir='raw'):

    '''Loads a Dataset object by name.
    Parameters
    ----------
    dataset_name:
        Name of dataset to load
    load_dir:
        Directory to save the file
    '''

    project_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
    data_path = project_dir / 'data' / load_dir
    df = pd.read_csv(data_path / dataset_name)

    return df

def save_dataset(df, dataset_name, save_dir='intermediate'):

    '''Saves a Dataset object by name.
    Parameters
    ----------
    df: Pandas DataFrame
    dataset_name:
        Name of dataset to save
    save_dir:
        Directory to save the file
    '''

    project_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
    data_path = project_dir / 'data' / save_dir
    df.to_csv(data_path / dataset_name, encoding='utf-8', index=False)
