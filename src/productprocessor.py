import pandas as pd
 
class ProductProcessor:
    def __init__(self):
        self.product_list = []
 
    def make_new_records(self, arr, url):
        product_dict = {"Dealer_Id": '', "Ad_Id": '', "Impression_count": '', 'Domain_name': '', "Product_data": ''}
 
        try:
            product_dict['Domain_name'] = url.split('/')[2].split('.')[1]
            product_dict['Dealer_Id'] = arr[0]
            product_dict['Ad_Id'] = arr[1]
            product_dict['Impression_count'] = arr[4].split('|')[0].split('=')[-1]
            product_dict['Product_data'] = "|".join(arr[4].split('|')[1:]) + ";" + ";".join(arr[5:])
 
            self.product_list.append(product_dict)
        except Exception as e:
            pass  
 
    def produce_product_info_df(self, df):
        df["Post-Product-List"] = df["Post-Product-List"].apply(lambda x: x.split(';'))
        df.apply(lambda x: self.make_new_records(x["Post-Product-List"], x["URL"]), axis=1)
        product_info_df = pd.DataFrame(self.product_list)
        return product_info_df