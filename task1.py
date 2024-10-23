from pathlib import Path

def total_salary(path):
    path_file=Path(path)
    if path_file.exists():
        try:
            with open("salary.txt", "r", encoding="utf-8") as data_file:
                data_list=data_file.readlines()
                salary_sum=0
                for person in data_list:
                    _, person_salary_str=person.removesuffix("\n").split(",")
                    salary_sum+=int(person_salary_str)
            salary_tuple = (salary_sum, int(salary_sum / len(data_list)))
            print(salary_tuple)
            return salary_tuple
        except (OSError, IOError):
            print("File exists but is corrupted or unreadable")
            return "File exists but is corrupted or unreadable"
    else:
        print(f"File {path} not found")
        return f"File {path} not found"

total_salary("salary.txt")


