from typing import Dict
from datetime import datetime

# ░░░░░░░█▀█░█░█░█▀▄░█▀█░█▀█░▀█▀░▀█▀░█▀▀░░░░░░
# ░░░░░░░█▀▀░░█░░█░█░█▀█░█░█░░█░░░█░░█░░░░░░░░
# ░░░░░░░▀░░░░▀░░▀▀░░▀░▀░▀░▀░░▀░░▀▀▀░▀▀▀░░░░░░

# ░░░░░░░▀█▀░█▀█░█▄█░█▀▀░░░▀▀█░█▀▀░█▀█░█▀█░░░█▀▄░█░░░█▀█░█▀▄░█▀▀░░░░░░
# ░░░░░░░░█░░█▀█░█░█░█▀▀░░░░░█░▀▀█░█░█░█░█░░░█▀▄░█░░░█░█░█▀▄░▀▀█░░░░░░
# ░░░░░░░░▀░░▀░▀░▀░▀░▀▀▀░░░▀▀░░▀▀▀░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀▀░░▀▀▀░░░░░░

# def calculate_age(dob: str) -> int:
#     dob_date = datetime.strptime(dob, "%Y-%m-%d")
#     today = datetime.today()
#     age = today.year - dob_date.year
#     if (today.month, today.day) < (dob_date.month, dob_date.day):
#         age -= 1
#     return age


def func1(json_blob: Dict) -> None:
    print(f"name is: {json_blob['name']}")
    print(f"age is: {json_blob['age']}")
    # print(f"age is {calculate_age(json_blob['dob'])}")


func1({"name": "John", "age": 30})
# func1({"name": "Herman", "dob": "1997-01-01"})
