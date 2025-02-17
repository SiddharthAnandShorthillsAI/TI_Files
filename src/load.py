import pandas as pd
import os
class Loader:
    def __init__(self, file_path, chunk_size):
        self.file_path = file_path
        self.chunk_size = chunk_size

    def load_data(self):
        try:
            for file in os.listdir(self.file_path):
                file_path = os.path.join(self.file_path, file)
                for chunk in pd.read_csv(file_path, sep="\t", header=None, on_bad_lines="skip",
                                         compression="infer", chunksize=self.chunk_size):
                    yield chunk  
        except Exception as e:
            raise e



