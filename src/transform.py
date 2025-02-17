import pandas as pd
class Transform:
    def __init__(self):
        pd.set_option('display.width', 50000)
        pd.set_option('display.max_columns', 100)
 
    def process_chunk(self, chunk: pd.DataFrame):
        chunk.columns = ["Date", "Post-Event-List", "Post-Product-List", "UnknownA", "URL", "Unknown"]
        chunk.fillna('', inplace=True)
        chunk.drop(columns=["UnknownA", "Unknown"], inplace=True)
        return chunk
 
    def find_rows_by_event_id(self, chunk: pd.DataFrame, event_id):
        return chunk[chunk["Post-Event-List"].apply(lambda x: event_id in x.split(","))]
 
    def expand_product_list(self, chunk: pd.DataFrame):
        chunk["Post-Product-List"] = chunk["Post-Product-List"].apply(lambda x: x.split(","))
        return chunk.explode(column="Post-Product-List")
    
    def impression_count(self, product_df):
        product_df["Impression_count"] = pd.to_numeric(product_df["Impression_count"], downcast="float")
        impression_count = (
            product_df.groupby("Domain_name")["Impression_count"]
            .sum()
        )
        
        return impression_count
 