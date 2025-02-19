import os
import pandas as pd
from load import Loader
from transform import Transform
from productprocessor import ProductProcessor
 
def main():
    folder_path = "../input/"
    final_df = pd.DataFrame() 
    domain_group_list=[]
    try:
       
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):  
                print(f"Processing file: {file_name}")
 
                loader = Loader(file_path)  
                extracted_data = loader.load_data()
                
                transform = Transform(extracted_data)
                transformed_data = transform.add_column_name()
                transformed_data = transform.drop_column_name()
 
                event_id = 20113
                transformed_data = transform.find_rows_by_event_id(str(event_id))
                transformed_data = transform.expand_product_list(transformed_data)
 
                processor = ProductProcessor()
                new_data = processor.produce_product_info_df(transformed_data)
                new_df_data = transform.impression_count(new_data)
                domain_group_list.append(new_df_data)
 
        final_df = pd.concat(domain_group_list).groupby('Domain_name').sum()
        print(final_df)
 
    except Exception as e:
        print(f"Error processing files: {e}")
 
if __name__ == "__main__":
    main()
 