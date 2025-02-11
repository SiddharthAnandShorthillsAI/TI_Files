import pandas as pd

class Transform:
    def __init__(self, df:pd.DataFrame):
        self.df=df
        pd.set_option('display.width',5000)
        pd.set_option('display.max_columns',10)
    
    def add_column_name(self):
        self.df.columns=["Date","Post-Event-List","Post-Product-List","UnknownA","URL","Unknown"]
        self.df.fillna('',inplace=True)
        return self.df
    
    def drop_column_name(self):
        self.df.drop(columns=["UnknownA","Unknown"],axis=1,inplace=True)
        return self.df

    def changing(self, event_id):
        return self.df[self.df["Post-Event-List"].apply(lambda x: event_id in x.split(","))]
    
    def expand_product_list(self,event_filtered_df):
        event_filtered_df["Post-Product-List"]=event_filtered_df["Post-Product-List"].apply(lambda x: x.split(","))
        post_event_filtered_df = event_filtered_df.explode(column=["Post-Product-List"])
        return post_event_filtered_df