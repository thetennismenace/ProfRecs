import requests


def sort_json_list(json_list, key_to_sort, n):
    sorted_data = sorted(json_list, key=lambda x: (x[key_to_sort]), reverse=True)
    if(len(sorted_data) < n):
        return sorted_data
    return sorted_data[-n:]


