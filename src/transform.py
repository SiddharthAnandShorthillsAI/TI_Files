import pandas as pd

class Transform:
    def __init__(self, df:pd.DataFrame):
        self.df=df
        pd.set_option('display.width',50000)
        pd.set_option('display.max_columns',100)
    
    def add_column_name(self):
        self.df.columns=["Date","Post-Event-List","Post-Product-List","UnknownA","URL","Unknown"]
        self.df.fillna('',inplace=True)
        return self.df
    
    def drop_column_name(self):
        self.df.drop(columns=["UnknownA","Unknown"],axis=1,inplace=True)
        return self.df

    def find_rows_by_event_id(self, event_id):
        return self.df[self.df["Post-Event-List"].apply(lambda x: event_id in x.split(","))]
    
    def expand_product_list(self,event_filtered_df):
        event_filtered_df["Post-Product-List"]=event_filtered_df["Post-Product-List"].apply(lambda x: x.split(","))
        post_event_filtered_df = event_filtered_df.explode(column=["Post-Product-List"])
        return post_event_filtered_df 
    
    def make_new_entries(self, arr, url):
        product_dict = {"Dealer_Id": '', "Ad_Id": '', "Impression_count": '', 'Domain_name': '', "Product_data": ''}

        try:
            product_dict['Domain_name'] = url.split('/')[2].split('.')[1]
            product_dict['Dealer_Id'] = arr[0]
            product_dict['Ad_Id'] = arr[1]
            product_dict['Impression_count'] = arr[4].split('|')[0].split('=')[-1]
            product_dict['Product_data'] = "|".join(arr[4].split('|')[1:]) + ";" + ";".join(arr[5:])

            self.product_list.append(product_dict)
        except Exception:
            pass

    def produce_product_info_df(self, df):
        
        df["Post_product_list"] = df["Post_product_list"].apply(lambda x: x.split(';'))
        df.apply(lambda x: self.make_new_entries(x.Post_product_list, x.URL), axis=1)

        product_info_df = pd.DataFrame(self.product_list)
        return product_info_df
    
    def impression_count(self, product_df):
        product_df["Impression_count"] = pd.to_numeric(product_df["Impression_count"], downcast="float")
        impression_count = (
            product_df.groupby("Domain_name")["Impression_count"]
            .sum()
        )
        
        return impression_count
 