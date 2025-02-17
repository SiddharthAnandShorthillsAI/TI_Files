import pandas as pd
import gc
class ProductProcessor:
    def __init__(self, chunk_size=150000):
        self.chunk_size = chunk_size

    def make_new_records(self, row):
        try:
            arr = row["Post-Product-List"].split(';')
            return {
                "Dealer_Id": arr[0],
                "Ad_Id": arr[1],
                "Impression_count": arr[4].split('|')[0].split('=')[-1],
                "Domain_name": row["URL"].split('/')[2].split('.')[1],
                "Product_data": "|".join(arr[4].split('|')[1:]) + ";" + ";".join(arr[5:])
            }
        except Exception:
            return None

    def produce_product_info_df(self, df):
        df["Processed_Data"] = df.apply(self.make_new_records, axis=1)
        processed_chunk = pd.DataFrame(df["Processed_Data"].dropna().tolist())
        del df 
        gc.collect()
        return processed_chunk


