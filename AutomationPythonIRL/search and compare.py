from googlesearch import search

def checking_video(name_of_video):
    query = f"photos.google.com/search/{name_of_video}"
    result = list(search(query, num_results= 1))
    return len(result) > 0 

def main():
    file_path = 'Name of each file.txt'

    try: 
        with open(file_path, 'r') as file:
            for line in file:
                name = line.strip()
                exist = checking_video(name)

                if exist: 
                    print(f"{name} : EXIST")
                else:
                    print(f"{name} : DOESN'T EXIST")
    
    except FileExistsError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"An error occurred : {e}")

if __name__ == '__main__':
    main()