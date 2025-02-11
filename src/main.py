from load import Loader 
from transform import Transform
def main():
    file_path="./input/"
    loader = Loader(file_path)
    try:
        extracted_data = loader.load_data()
        transform=Transform(extracted_data)
        
        transformed_data=transform.add_column_name()
        transformed_data=transform.drop_column_name()
        event_id=20113
        transformed_data=transform.changing(str(event_id))
        transformed_data=transform.expand_product_list(transformed_data)
        print(transformed_data)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()