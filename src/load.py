import pandas as pd
 
class Loader:
    def __init__(self, file_path):
        self.file_path = file_path 
 
    def load_data(self):
        try:
            df = pd.read_csv(self.file_path, sep="\t", header=None, on_bad_lines="skip", compression="infer")
            return df
        except Exception as e:
            raise e