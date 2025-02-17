from load import Loader
from transform import Transform
from productprocessor import ProductProcessor
import pandas as pd
import gc
def main():
    file_path = "./input/"
    chunk_size = 150000
    loader = Loader(file_path, chunk_size)
    transform = Transform()
    processor = ProductProcessor()
    processed_data = []
    try:
        for chunk in loader.load_data():
            chunk = transform.process_chunk(chunk)
            chunk = transform.find_rows_by_event_id(chunk, str(20113))
            chunk = transform.expand_product_list(chunk)
            processed_chunk = processor.produce_product_info_df(chunk)  
            processed_data.append(processed_chunk)
            del chunk, processed_chunk 
            gc.collect()

        final_df = pd.concat(processed_data, ignore_index=True)
        new_df = transform.impression_count(final_df)
        print(new_df)
        print(final_df)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
