import requests
from urllib.parse import urlencode

GRADE_BASE_URL = "https://api.peterportal.org/rest/v0/grades"


def calculate_mean_gpa(dicts, prof):
    lists = []
    for i in dicts:
        if i['instructor'] == prof:
            lists.append(i['averageGPA'])
    lists = [i for i in lists if i is not None]
    print(sum(lists) / len(lists))


def get_teachers(year_start, year_end, department, number):
    base_url = "https://api.peterportal.org/rest/v0/grades"
    common_params = {
        'department': department,
        'number': number
    }
    year = ""
    for i in range(year_start, year_end):
        year += str(i) + "-" + str((i + 1) % 1000) + ";"
    raw_params = {
        'year': year[:-1]
    }
    # Combine common and raw parameters
    raw_url = f"{GRADE_BASE_URL}/raw?{urlencode({**common_params, **raw_params})}"
    return raw_url


if __name__ == "__main__":
    u = get_teachers(2010, 2023, "I&C SCI", "51")
    d = requests.get(u).json()
    x = {i['instructor'] for i in d if i['instructor'] != 'UNKNOWN, INSTRUCTOR'}
    print(x)
    calculate_mean_gpa(d, "WONG-MA, J.")
    # print(requests.get(u).json())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/