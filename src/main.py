from load import Loader 

def main():
    file_path="./input/"
    loader = Loader(file_path)
    try:
        result = loader.load_data()
        print(result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()