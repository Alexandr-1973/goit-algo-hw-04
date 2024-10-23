from pathlib import Path

def get_cats_info(path):
    path_file=Path(path)
    try:
        with open(path_file, "r", encoding="utf-8") as data_cats:
            data_cats_list=data_cats.readlines()
            cats_dict_list=[]
            for cat in data_cats_list:
                cat_id, name, age = cat.removesuffix("\n").split(",")
                cats_dict_list.append({"id": cat_id, "name":name , "age":age })
            print(cats_dict_list)
            return cats_dict_list
    except FileNotFoundError:
        print(f"File {path} not found")
        return f"File {path} not found"
    except (OSError, IOError):
        print("File exists but is corrupted or unreadable")
        return "File exists but is corrupted or unreadable"

get_cats_info("cats.txt")


