import pandas as pd
import os 
class Loader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        combined_df=pd.DataFrame()
        try:
            for file in os.listdir(self.file_path):
                temp_df=pd.read_csv(self.file_path+file,sep="\t",header=None,on_bad_lines="skip",compression="infer")
                combined_df=pd.concat([combined_df,temp_df])   
            return combined_df
        except Exception as e:
            raise e        
    