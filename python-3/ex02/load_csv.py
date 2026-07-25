import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV dataset and return a pandas DataFrame."""
    try:
        assert isinstance(path, str), "The path must be a string"
        assert path.endswith(".csv"), "The path must end with .csv"
        myData = pd.read_csv(path)
        return myData

    except AssertionError as error:
        print("AssertionError:", error)
        return None
    except Exception as error:
        print("Error:", error)
        return None
