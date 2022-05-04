import pandas as pd

class CSV_Loader():
    """
    
    """
    try:
        def __init__(self, csv_file_path, index_col_name):
            _csv_file_to_df = pd.read_csv(csv_file_path)
            return _csv_file_to_df
            
            
    except Exception as e:
        display("Error occured in initialization of CSV loader due to ", e)
        